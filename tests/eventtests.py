import unittest

import os
import opentimelineio as otio

class TestOTIOEvents(unittest.TestCase):
    def setUp(self):
        otio.schema.schemadef.module_from_name('SyncEvent') # Ensure the SyncEvents schema is loaded



        self.test_dir = os.path.dirname(__file__)
        #self.otio_file_path = os.path.join(self.test_dir, "test_otio_events.otio")
        #self.timeline = otio.adapters.read_from_file(self.otio_file_path)

    def testEventCreation(self):
        """Test the creation of event objects."""
        play_event = otio.schemadef.SyncEvent.Play(value=True)
        self.assertIsInstance(play_event, otio.schemadef.SyncEvent.Play)
        print(f"Play Event: {play_event}")

        set_frame_event = otio.schemadef.SyncEvent.SetCurrentFrame(time=otio.opentime.RationalTime(1, 24))
        self.assertIsInstance(set_frame_event, otio.schemadef.SyncEvent.SetCurrentFrame)
        print(f"SetCurrentFrame Event: {set_frame_event}")

        new_presenter_event = otio.schemadef.SyncEvent.NewPresenter(presenter_hash="abc123")
        self.assertIsInstance(new_presenter_event, otio.schemadef.SyncEvent.NewPresenter)
        print(f"NewPresenter Event: {new_presenter_event}")


        mr = otio.schema.ExternalReference(
                    target_url="/path/to/media/file.mov",
                    #available_range=available_range,
                )

        media_change_event = otio.schemadef.SyncEvent.MediaChange(mediaReference=mr)
        self.assertIsInstance(media_change_event, otio.schemadef.SyncEvent.MediaChange)
        print(f"MediaChange Event: {media_change_event}")

        events = [play_event, set_frame_event, new_presenter_event, media_change_event]
        for event in events:
            string = otio.adapters.write_to_string(event, adapter_name="otio_json", indent=-1)
            newevent = otio.adapters.read_from_string(string, adapter_name="otio_json")
            self.assertEqual(type(event), type(newevent), f"Type mismatch for event: {event}")
            self.assertIsInstance(newevent, otio.schemadef.SyncEvent.SyncEvent, f"Event is not a SyncEvent: {newevent}")

    def testAnnotations(self):
        """Test the annotations on event objects."""
        events = []
        paint_start = otio.schemadef.SyncEvent.PaintStart(source_index=0, 
                                                          uuid="test1234",
                                                          friendly_name="Sam Richards",
                                                          participant_hash="hash1234",
                                                          rgba=[1.0, 0.0, 0.0, 1.0],
                                                          type="color",
                                                          brush="circle",
                                                          name="paint",
                                                          effect_name="paint_effect",
        )
        events.append(paint_start)
        self.assertIsInstance(paint_start, otio.schemadef.SyncEvent.PaintStart)
        coords = [[0,0,1], [0,1,1], [1,1,1], [0,1,1], [0,0,1]]
        for coord in coords:
            c = otio.schemadef.SyncEvent.PaintVertex(x=float(coord[0]), y=float(coord[1]), size=float(coord[2]))
            event = otio.schemadef.SyncEvent.PaintPoint(uuid="test1234", point=c)
            events.append(event)

        events.append(otio.schemadef.SyncEvent.PaintEnd(uuid="test1234"))
        for e in events:
            print(otio.adapters.write_to_string(e, adapter_name="otio_json"))

        
    def Xtest_set_current_frame(self):
        """Test the SetCurrentFrame schema."""
        for event in self.timeline.each_child():
            if isinstance(event, otio.schemadef.SyncEvent.SetCurrentFrame):
                self.assertIsInstance(event.time, otio.core.RationalTime)
                self.assertIsInstance(event.timestamp, str)
                print(f"SetCurrentFrame: {event}")

    def Xtest_new_presenter(self):
        """Test the NewPresenter schema."""
        for event in self.timeline.each_child():
            if isinstance(event, otio.schema.NewPresenter):
                self.assertIsInstance(event.presenter_hash, str)
                print(f"NewPresenter: {event}") 


if __name__ == '__main__':
    unittest.main()