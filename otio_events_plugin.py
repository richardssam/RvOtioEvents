from __future__ import print_function

import os
import sys
import datetime

try:
    from PySide2 import QtGui, QtCore, QtWidgets
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    from PySide2.QtUiTools import QUiLoader
except ImportError:
  try:
    from PySide6 import QtGui, QtCore, QtWidgets
    from PySide6.QtGui import *
    from PySide6.QtCore import *
    from PySide6.QtWidgets import *
    from PySide6.QtUiTools import QUiLoader
  except ImportError:
    pass

from rv import commands, extra_commands
from rv import rvtypes

import opentimelineio as otio

from otio_writer import get_source_node, create_timeline_from_node, _create_media_reference
from EventSchemaDef import *

class Mode(object):
    sleeping = 1
    loading = 2
    processing = 3


class OTIOEventsPlugin(rvtypes.MinorMode):

    def set_directory(self, event):
        """
        Set the directory for OTIO event logging.
        """
        event.reject()
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.ShowDirsOnly, True)
        dialog.setWindowTitle("Select Directory for OTIO Event Log")
        dialog.setLabelText(QFileDialog.Accept, "Set Directory")
        if dialog.exec_() == QDialog.Accepted:
            directory = dialog.selectedFiles()[0]
            print("Setting OTIO event log directory to:", directory)
            self._logging_directory = directory
            commands.writeSettings("otioevents", "logging_directory", directory)
            print("OTIO event log directory set to:", self._logging_directory)
            self.setup_logging()
    
    def setup_logging(self):
        """
        Set up logging for OTIO events.
        This function can be expanded to include more complex logging mechanisms.
        """
        if self.logging_fh is not None:
            self.logging_fh.close()
            self.logging_fh = None

        if not self._logging_directory:
            print("No logging directory set. Please set it using the plugin menu.")
            return
        if not os.path.exists(self._logging_directory):
            try:
                os.makedirs(self._logging_directory)
            except OSError as e:
                print("Error creating logging directory:", e)
                return
        # Create a log file with a date/time filename
        now = datetime.datetime.now()
        log_filename = now.strftime("otio_events_%Y%m%d_%H%M%S.jsonl")
        self.log_path = os.path.join(self._logging_directory, log_filename)
        self.logging_fh = open(self.log_path, "a")
        print("Logging OTIO events:", self.log_path)

    def __init__(self):
        print("IN EVENTS PLUGIN")
        super(OTIOEventsPlugin, self).__init__()

        self.last_source = None
        self.logging_fh = None
        self._logging_directory = commands.readSettings("otioevents", "logging_directory", "")
        if self._logging_directory == "":
            self._logging_directory = None
        self.init(
            "otioevents",
            [
                ("frame-changed", self.on_frame_changed, "Detect clip switch")
            ],
            None,
            [
                ("Tools",
                [
                        ("Set OTIO Event Log Directory", self.set_directory, None, None),
                        #("OTIO Event Logging", self.enable_event_logging, None, None),
                ]
                )
            ]
        )

        self.setup_logging()


    def on_frame_changed(self, event):
        # Get the current source node for the current frame
        event.reject()  # Reject the event to prevent default handling

        sourceList = [n['node'] for n in commands.sourcesRendered()]

        if sourceList:
            current_source = sourceList[0]  # For a sequence, this is the current clip
            info = commands.sourceMediaInfo(current_source)
            if not info:
                print("No media info found for source node:", current_source)
                return
            current_source_path = info.get("file", current_source)
            if current_source_path != self.last_source:
                nodeGroup = commands.nodeGroup(current_source)
                if nodeGroup is None:
                    print("No node group found for source node:", current_source)
                    return
                active_source = get_source_node(nodeGroup)
                media_ref = _create_media_reference(nodeGroup, active_source)
                media_change = MediaChange(mediaReference=media_ref)
                s = otio.adapters.write_to_string(media_change, adapter_name="otio_json", indent=-1)
                if self.logging_fh is not None:
                    print(s, file=self.logging_fh)
                    self.logging_fh.flush()
                self.last_source = current_source_path




def createMode():
    support_files_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "..", "SupportFiles", "otio_reader"
    )
    #print("About to run:", otio_mu)
    #commands.eval(otio_mu)

    manifest_path = os.environ.get("OTIO_PLUGIN_MANIFEST_PATH", "")
    if manifest_path:
        manifest_path += os.pathsep
    os.environ["OTIO_PLUGIN_MANIFEST_PATH"] = manifest_path + os.path.join(
        support_files_path, "manifest.json"
    )
    sys.path.append(support_files_path)

    return OTIOEventsPlugin()
