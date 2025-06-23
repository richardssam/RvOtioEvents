
import opentimelineio as otio
import datetime


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
