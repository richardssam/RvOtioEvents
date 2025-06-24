
import opentimelineio as otio
import datetime



class SyncEvent(otio.core.SerializableObject):
    """A schema for the event system to define when play is enabled.
    timestamp is an ISO 8601 formatted string representing the time of the change.
    This is used to track when media changes occur in the timeline.
    value is a boolean indicating whether play is enabled or not.
    """


    timestamp = otio.core.serializable_field(
        "timestamp",
        doc="The timestamp of the media change, in ISO 8601 format",
    )

    def __init__(
            self,
            timestamp=None 
    ):
        otio.core.SerializableObject.__init__(self)

        self.timestamp = timestamp if timestamp is not None else datetime.datetime.now().isoformat()


@otio.core.register_type
class Play(SyncEvent):
    """A schema for the event system to define when play is enabled.
    timestamp is an ISO 8601 formatted string representing the time of the change.
    This is used to track when media changes occur in the timeline.
    value is a boolean indicating whether play is enabled or not.
    """

    _serializable_label = "play.1"
    _name = "Play"

    value = otio.core.serializable_field(
        "value",
        required_type=bool,
        doc="The value of the play event",
    )

    def __init__(
            self,
            value=True,
            timestamp=None 
    ):
        SyncEvent.__init__(self, timestamp)
        if not isinstance(value, bool):
            raise TypeError("value must be a boolean")
        self.value = value


    def __str__(self):
        
        return "Play({})".format(
            repr(self.value)
        )

    def __repr__(self):
        return "otio.schemadef.SyncEvent.Play(value={})".format(
            repr(self.value)
        )
    

@otio.core.register_type
class SetCurrentFrame(SyncEvent):
    """A schema for the event system to define when the current frame is set.
    time is a RationalTime representing the current frame in the timeline.
    timestamp is an ISO 8601 formatted string representing the time of the change.
    This is used to track when the current frame changes occur in the timeline.
    """

    _serializable_label = "set_current_frame.1"
    _name = "SetCurrentFrame"


    time = otio.core.serializable_field(
        "time",
        required_type=otio.opentime.RationalTime,
        doc="The current time in the timeline"
    )

    def __init__(
            self,
            time=None,
            timestamp=None 
    ):
        SyncEvent.__init__(self, timestamp)

        if time is not None and not isinstance(time, otio.opentime.RationalTime):
            raise TypeError("time must be an otio.core.RationalTime")
        self.time = time


    def __str__(self):
        
        return "SetCurrentFrame({})".format(
            repr(self.time)
        )

    def __repr__(self):
        return "otio.schemadef.SyncEvent.SetCurrentFrame(time={})".format(
            repr(self.time)
        )
    

@otio.core.register_type
class NewPresenter(SyncEvent):
    """A schema for my thing."""

    _serializable_label = "NewPresenter.1"
    _name = "NewPresenter"

    def __init__(
            self,
            presenter_hash=None,
            timestamp=None 
    ):
        SyncEvent.__init__(self, timestamp)
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
        return "otio.schemadef.SyncEvent.NewPresenter(presenter_hash={})".format(
            repr(self.presenter_hash)
        )


@otio.core.register_type
class NewParticipant(SyncEvent):
    """A schema for my thing."""

    _serializable_label = "NewPresenter.1"
    _name = "NewPresenter"

    def __init__(
            self,
            timestamp=None 
    ):
        SyncEvent.__init__(self, timestamp)

    def __str__(self):
        
        return "NewParticipant({})".format(
            repr()
        )

    def __repr__(self):
        return "otio.schemadef.SyncEvent.NewParticipant()"


@otio.core.register_type
class SharedKeyRequest(SyncEvent):
    """A schema for my thing."""

    _serializable_label = "SharedKeyRequest.1"
    _name = "SharedKeyRequest"

    def __init__(
            self,
            key=None,
            timestamp=None
    ):
        SyncEvent.__init__(self, timestamp)
        self.key = key

    key = otio.core.serializable_field(
        "key",
        doc="The shared key"
    )

    def __str__(self):

        return "SharedKeyRequest({})".format(
            repr(self.key)
        )

    def __repr__(self):
        return "otio.schemadef.SyncEvent.SharedKeyRequest(key={})".format(
            repr(self.key)
        )



@otio.core.register_type
class SharedKeyResponse(SyncEvent):
    """A schema for my thing."""

    _serializable_label = "SharedKeyResponse.1"
    _name = "SharedKeyResponse"

    def __init__(
            self,
            key=None,
            timestamp=None
    ):
        SyncEvent.__init__(self, timestamp)
        self.key = key

    key = otio.core.serializable_field(
        "key",
        doc="The shared key"
    )

    def __str__(self):

        return "SharedKeyResponse({})".format(
            repr(self.key)
        )

    def __repr__(self):
        return "otio.schemadef.SyncEvent.SharedKeyResponse(key={})".format(
            repr(self.key)
        )


@otio.core.register_type
class GetSession(SyncEvent):
    """A schema for my thing."""

    _serializable_label = "GetSession.1"
    _name = "GetSession"

    def __init__(
            self,
            user=None,
            app=None,
            timestamp=None
    ):
        SyncEvent.__init__(self, timestamp)
        self.user = user
        self.app = app

    user = otio.core.serializable_field(
        "user",
        doc="The user making the request"
    )

    app = otio.core.serializable_field(
        "app",
        doc="The app making the request"
    )

    def __str__(self):

        return "GetSession({})".format(
            repr(self.user) + ", " + repr(self.app)
        )

    def __repr__(self):
        return "otio.schemadef.SyncEvent.GetSession(user={}, app={})".format(
            repr(self.user), repr(self.app)
        )

@otio.core.register_type
class RequestSyncPlayback(SyncEvent):
    """A schema for my thing."""

    _serializable_label = "RequestSyncPlayback.1"
    _name = "RequestSyncPlayback"

    def __init__(
            self,
            timestamp=None
    ):
        SyncEvent.__init__(self, timestamp)

    def __str__(self):

        return "RequestSyncPlayback({})".format(
            repr(self.user) + ", " + repr(self.app)
        )

    def __repr__(self):
        return "otio.schemadef.SyncEvent.RequestSyncPlayback(user={}, app={})".format(
            repr(self.user), repr(self.app)
        )


@otio.core.register_type
class SyncPlayback(SyncEvent):
    """A schema for my thing."""

    _serializable_label = "SyncPlayback.1"
    _name = "SyncPlayback"

    def __init__(
            self,
            looping=None,
            playing=None,
            muted=None,
            scrubbing=None,
            playback_range=None, # Missing enabled, zoomed
            current_time=None,
            output_bounds=None,
            source=None,
            source_index=0,
            timestamp=None
    ):
        SyncEvent.__init__(self, timestamp)
        self.looping = looping
        self.playing = playing
        self.muted = muted
        self.scrubbing = scrubbing
        self.playback_range = playback_range
        self.current_time = current_time
        self.output_bounds = output_bounds
        self.source = source
        self.source_index = source_index

    looping = otio.core.serializable_field(
        "looping",
        required_type=bool,
        doc="Whether the playback is looping"
    )

    playing = otio.core.serializable_field(
        "playing",
        required_type=bool,
        doc="Whether the playback is currently playing"
    )

    muted = otio.core.serializable_field(
        "muted",
        required_type=bool,
        doc="Whether the playback is muted"
    )

    playback_range = otio.core.serializable_field(
        "playback_range",
        required_type=otio.opentime.TimeRange,
        doc="The range of playback"
    )

    scrubbing = otio.core.serializable_field(
        "scrubbing",
        required_type=bool,
        doc="Whether the playback is currently scrubbing"
    )
    current_time = otio.core.serializable_field(
        "current_time",
        required_type=otio.opentime.RationalTime,
        doc="The current time in the playback"
    )
    output_bounds = otio.core.serializable_field(
        "output_bounds",
        required_type=otio.schema.box2d,
        doc="The output bounds of the playback")
    source = otio.core.serializable_field(
        "source",
        doc="The source of the playback")
    source_index = otio.core.serializable_field(
        "source_index",
        required_type=int,
        doc="The index of the source in the playback, used for multi-source playback"
    )

    def __str__(self):

        return "SyncPlayback({})".format(
            repr(self.looping) + ", " + repr(self.playing) + ", " + repr(self.muted) + ", " + repr(self.playback_range)
        )

    def __repr__(self):
        return "otio.schemadef.SyncEvent.SyncPlayback(looping={}, playing={}, muted={}, playback_range={})".format(
            repr(self.looping), repr(self.playing), repr(self.muted), repr(self.playback_range)
        )

@otio.core.register_type
class MediaChange(SyncEvent):
    """A schema for the event system to denote when media changes.
    mediaReference is an otio.core.MediaReference
    timestamp is an ISO 8601 formatted string representing the time of the change.
    This is used to track when media changes occur in the timeline.
    """

    _serializable_label = "MediaChange.1"
    _name = "MediaChange"

    def __init__(
            self,
            mediaReference=None,
            timestamp=None 
        ):
        SyncEvent.__init__(self, timestamp)
        if mediaReference is not None and not isinstance(mediaReference, otio.core.MediaReference):
            raise TypeError("mediaReference must be an otio.core.MediaReference")
        self.mediaReference = mediaReference

    mediaReference = otio.core.serializable_field(
        "mediaReference",
        required_type=otio.core.MediaReference,
        doc="The reference to the media"
    )

    def __str__(self):
        
        return "MediaChange({})".format(
            repr(self.mediaReference)
        )

    def __repr__(self):
        return "otio.schemadef.SyncEvent.MediaChange(mediaReference={})".format(
            repr(self.mediaReference)
        )


@otio.core.register_type
class PaintStart(SyncEvent):
    """A schema for the event system to denote when painting starts.
    timestamp is an ISO 8601 formatted string representing the time of the change.
    This is used to track when media changes occur in the timeline.
    """

    _serializable_label = "PaintStart.1"
    _name = "PaintStart"

    def __init__(
            self,
            source_index=0,
            uuid=None,
            friendly_name=None,
            participant_hash=None,
            rgba=None,
            type="color",
            brush="circle",
            visible=True,
            name=None,
            effect_name=None,
            layer_range=None,
            hold=None,
            ghost=None,
            ghost_before=None,
            ghost_after=None,
            timestamp=None 
        ):
        SyncEvent.__init__(self, timestamp)
        self.source_index = source_index
        self.uuid = uuid
        self.friendly_name = friendly_name
        self.participant_hash = participant_hash
        self.rgba = rgba
        self.type = type
        self.brush = brush
        self.visible = visible
        self.name = name
        self.effect_name = effect_name
        self.layer_range = layer_range
        self.hold = hold
        self.ghost = ghost
        self.ghost_before = ghost_before
        self.ghost_after = ghost_after

        if not isinstance(source_index, int):
            raise TypeError("source_index must be an integer")

        if not isinstance(rgba, list) or len(rgba) != 4 or not all(isinstance(x, (int, float)) for x in rgba):
            raise TypeError("rgba must be an list of numbers")

    source_index = otio.core.serializable_field(
        "source_index",
        required_type=int,
        doc="The index of the source media for the paint."
    )
    uuid = otio.core.serializable_field(
        "uuid",
        doc="The unique identifier for the paint event"
    )
    friendly_name = otio.core.serializable_field(
        "friendly_name",
        doc="The friendly artist name for the paint event creator"
    )
    participant_hash = otio.core.serializable_field(
        "participant_hash",
        doc="The unique identifier for the participant"
    )
    rgba = otio.core.serializable_field(
        "rgba",
        required_type=list,
        doc="The color of the paint event in RGBA format"
    )
    type = otio.core.serializable_field(
        "type",
        doc="The type of the paint event"
    )
    brush = otio.core.serializable_field(
        "brush",
        doc="The brush type of the paint event"
    )
    visible = otio.core.serializable_field(
        "visible",
        required_type=bool,
        doc="The visible type of the paint event"
    )
    layer_range = otio.core.serializable_field(
        "layer_range",
        required_type=otio.opentime.TimeRange,
        doc="The range of the layer for the paint event"
    )
    hold = otio.core.serializable_field(
        "hold",
        required_type=bool,
        doc="The hold of the paint event"
    )
    ghost = otio.core.serializable_field(
        "ghost",
        required_type=bool,
        doc="Is ghosting of the paint strokes enabled"
    )
    ghost_before = otio.core.serializable_field(
        "ghost_before",
        required_type=bool,
        doc="Number of frames to ghost before the current frame"
    )
    ghost_after = otio.core.serializable_field(
        "ghost_after",
        required_type=bool,
        doc="Number of frames to ghost after the current frame"
    )

    def __str__(self):
        
        return "MediaChange({})".format(
            repr(self.mediaReference)
        )

    def __repr__(self):
        return "otio.schemadef.SyncEvent.MediaChange(mediaReference={})".format(
            repr(self.mediaReference)
        )
    



@otio.core.register_type
class PaintVertex(otio.core.SerializableObject):
    """A schema for the definition of a point vertex in a paint stroke."""

    _serializable_label = "PaintVertex.1"
    _name = "PaintVertex"

    def __init__(
            self,
            x=0.0,
            y=0.0,
            size=1.0
        ):
        otio.core.SerializableObject.__init__(self)
        self.x = x
        self.y = y
        self.size = size

        if not isinstance(x, float):
            raise TypeError("x must be an float")
        if not isinstance(y, float):
            raise TypeError("y must be an float")
        if not isinstance(size, float):
            raise TypeError("size must be an float")
    x = otio.core.serializable_field(
        "x",
        required_type=float,
        doc="The x coordinate of the point vertex"
    )
    y = otio.core.serializable_field(
        "y",
        required_type=float,
        doc="The y coordinate of the point vertex"
    )
    size = otio.core.serializable_field(
        "size",
        required_type=float,
        doc="The size of the point vertex"
    )

    def __str__(self):
        
        return "PaintVertex({})".format(
            repr(self.x) + ", " + repr(self.y) + ", " + repr(self.size)
        )

    def __repr__(self):
        return "otio.schemadef.SyncEvent.PaintVertex(mediaReference={})".format(
            repr(self.mediaReference)
        )

@otio.core.register_type
class PaintPoint(SyncEvent):
    """A schema for the event system to denote when painting starts.
    timestamp is an ISO 8601 formatted string representing the time of the change.
    This is used to track when media changes occur in the timeline.
    """

    _serializable_label = "PaintPoint.1"
    _name = "PaintPoint"

    def __init__(
            self,
            source_index=0,
            uuid=None,
            layer_range=None,
            point=None,
            timestamp=None 
        ):
        SyncEvent.__init__(self, timestamp)
        self.source_index = source_index
        self.uuid = uuid
        self.layer_range = layer_range
        self.point = point

        if not isinstance(source_index, int):
            raise TypeError("source_index must be an integer")

        if not isinstance(point, PaintVertex):
            print("Point type: ", type(point))
            raise TypeError("point must be an PaintVertex")

    source_index = otio.core.serializable_field(
        "source_index",
        required_type=int,
        doc="The index of the source media for the paint."
    )
    uuid = otio.core.serializable_field(
        "uuid",
        doc="The unique identifier for the paint event"
    )
    layer_range = otio.core.serializable_field(
        "layer_range",
        required_type=otio.opentime.TimeRange,
        doc="The range of the layer for the paint event"
    )
    point = otio.core.serializable_field(
        "point",
        required_type=PaintVertex,
        doc="The vertex of the paint event"
    )

    def __str__(self):
        
        return "PaintPoint({})".format(
            repr(self.point)
        )

    def __repr__(self):
        return "otio.schemadef.SyncEvent.MediaChange(point={})".format(
            repr(self.point)
        )
    

@otio.core.register_type
class PaintEnd(SyncEvent):
    """A schema for the event system to denote when painting ends.
    timestamp is an ISO 8601 formatted string representing the time of the change.
    This is used to track when media changes occur in the timeline.
    """

    _serializable_label = "PaintEnd.1"
    _name = "PaintEnd"

    def __init__(
            self,
            uuid=None,
            point=None,
            timestamp=None
        ):
        SyncEvent.__init__(self, timestamp)
        self.uuid = uuid
        self.point = point


        if point is not None and not isinstance(point, list):
            raise TypeError("point must be a list of PaintVertex")

    uuid = otio.core.serializable_field(
        "uuid",
        doc="The unique identifier for the paint event"
    )

    point = otio.core.serializable_field(
        "point",
        required_type=PaintVertex,
        doc="The vertex of the paint event"
    )

    def __str__(self):
        return "PaintEnd({})".format(
            repr(self.point)
        )

    def __repr__(self):
        return "otio.schemadef.SyncEvent.PaintEnd(point={})".format(
            repr(self.point)
        )