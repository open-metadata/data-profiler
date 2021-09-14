from distutils.version import LooseVersion

from data_profiler.marshmallow__shade.decorators import (
    post_dump,
    post_load,
    pre_dump,
    pre_load,
    validates,
    validates_schema,
)
from data_profiler.marshmallow__shade.exceptions import ValidationError
from data_profiler.marshmallow__shade.schema import Schema, SchemaOpts
from data_profiler.marshmallow__shade.utils import (
    EXCLUDE,
    INCLUDE,
    RAISE,
    missing,
    pprint,
)

from . import fields

__version__ = "3.7.1"
__version_info__ = tuple(LooseVersion(__version__).version)
__all__ = [
    "EXCLUDE",
    "INCLUDE",
    "RAISE",
    "Schema",
    "SchemaOpts",
    "fields",
    "validates",
    "validates_schema",
    "pre_dump",
    "post_dump",
    "pre_load",
    "post_load",
    "pprint",
    "ValidationError",
    "missing",
]
