from hatchling.plugin import hookimpl
from .builder import FooBuilder

@hookimpl
def hatch_register_builder():
    return FooBuilder
