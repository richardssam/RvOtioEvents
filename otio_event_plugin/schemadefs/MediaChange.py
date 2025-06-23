
import opentimelineio as otio
import datetime

@otio.core.register_type
class NewPresenter(otio.core.SerializableObject):
    """A schema for my thing."""

    _serializable_label = "NewPresenter.1"
    _name = "NewPresenter"

    def __init__(
            self,
            presenter_hash=None,
    ):
        otio.core.SerializableObject.__init__(self)
        self.presenter_hash = presenter_hash

    presenter_hash = otio.core.serializable_field(
        "presenter_hash",
        doc="The hash of the presenter"
    )

    def __str__(self):
        
        return "NewPresenter({})".format(
            repr(self.presenter_hash)
        )

    def __repr__(self):
        return "otio.schema.NewPresenter(presenter_hash={})".format(
            repr(self.presenter_hash)
        )
    

@otio.core.register_type
class MediaChange(otio.core.SerializableObject):
    """A schema for the event system to denote when media changes.
    mediaReference is an otio.schema.MediaReference
    timestamp is an ISO 8601 formatted string representing the time of the change.
    This is used to track when media changes occur in the timeline.
    """

    _serializable_label = "MediaChange.1"
    _name = "MediaChange"

    def __init__(
            self,
            mediaReference=None,
            timestamp=None # type: Optional[str] =
    ):
        otio.core.SerializableObject.__init__(self)
        #if mediaReference is not None and not isinstance(mediaReference, otio.schema.MediaReference):
        #    raise TypeError("mediaReference must be an otio.schema.MediaReference")
        self.mediaReference = mediaReference
        self.timestamp = timestamp if timestamp is not None else datetime.datetime.now().isoformat()

    mediaReference = otio.core.serializable_field(
        "mediaReference",
        doc="The reference to the media"
    )

    timestamp = otio.core.serializable_field(
        "timestamp",
        doc="The timestamp of the media change, in ISO 8601 format",
    )

    def __str__(self):
        
        return "MediaChange({})".format(
            repr(self.mediaReference)
        )

    def __repr__(self):
        return "otio.schema.MediaChange(mediaReference={})".format(
            repr(self.mediaReference)
        )
    

@otio.core.register_type
class Play(otio.core.SerializableObject):
    """A schema for the event system to define when play is enabled.
    timestamp is an ISO 8601 formatted string representing the time of the change.
    This is used to track when media changes occur in the timeline.
    value is a boolean indicating whether play is enabled or not.
    """

    _serializable_label = "play.1"
    _name = "Play"

    timestamp = otio.core.serializable_field(
        "timestamp",
        doc="The timestamp of the media change, in ISO 8601 format",
    )

    value = otio.core.serializable_field(
        "value",
        required_type=bool,
        doc="The value of the play event",
    )

    def __init__(
            self,
            value,
            timestamp=None # type: Optional[str] = None
    ):
        otio.core.SerializableObject.__init__(self)
        if not isinstance(value, bool):
            raise TypeError("value must be a boolean")
        self.value = value
        self.timestamp = timestamp if timestamp is not None else datetime.datetime.now().isoformat()


    def __str__(self):
        
        return "Play({})".format(
            repr(self.value)
        )

    def __repr__(self):
        return "otio.schema.Play(value={})".format(
            repr(self.value)
        )
    
@otio.core.register_type
class SetCurrentFrame(otio.core.SerializableObject):
    """A schema for the event system to define when the current frame is set.
    time is a RationalTime representing the current frame in the timeline.
    timestamp is an ISO 8601 formatted string representing the time of the change.
    This is used to track when the current frame changes occur in the timeline.
    """

    _serializable_label = "set_current_frame.1"
    _name = "SetCurrentFrame"

    def __init__(
            self,
            time,
            timestamp=None # type: Optional[str] = None
    ):
        otio.core.SerializableObject.__init__(self)

        if not isinstance(time, otio.core.RationalTime):
            raise TypeError("time must be an otio.core.RationalTime")
        self.time = time
        self.timestamp = timestamp if timestamp is not None else datetime.datetime.now().isoformat()


    def __str__(self):
        
        return "SetCurrentFrame({})".format(
            repr(self.time)
        )

    def __repr__(self):
        return "otio.schema.SetCurrentFrame(time={})".format(
            repr(self.time)
        )