
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
    
