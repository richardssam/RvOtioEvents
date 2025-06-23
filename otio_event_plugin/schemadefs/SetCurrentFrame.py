
import opentimelineio as otio
import datetime


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