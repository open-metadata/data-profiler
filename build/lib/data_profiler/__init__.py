# Set up version information immediately
from ._version import get_versions  # isort:skip

__version__ = get_versions()["version"]  # isort:skip
del get_versions  # isort:skip

from data_profiler.data_context import DataContext

from .util import (
    from_pandas,
    get_context,
    measure_execution_time,
    read_csv,
    read_excel,
    read_feather,
    read_json,
    read_parquet,
    read_pickle,
    read_table,
    validate,
)

rtd_url_ge_version = __version__.replace(".", "_")
