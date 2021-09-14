from data_profiler.util import verify_dynamic_loading_support

from .store import Store  # isort:skip
from .store_backend import (  # isort:skip
    StoreBackend,
    InMemoryStoreBackend,
)
from .ge_cloud_store_backend import GeCloudStoreBackend  # isort:skip
from .tuple_store_backend import (  # isort:skip
    TupleFilesystemStoreBackend,
    TupleGCSStoreBackend,
    TupleS3StoreBackend,
    TupleStoreBackend,
    TupleAzureBlobStoreBackend,
)
from .database_store_backend import DatabaseStoreBackend  # isort:skip
from .configuration_store import ConfigurationStore  # isort:skip
from .checkpoint_store import CheckpointStore  # isort:skip
from .metric_store import (  # isort:skip
    EvaluationParameterStore,
    MetricStore,
)
from .expectations_store import ExpectationsStore  # isort:skip
from .validations_store import ValidationsStore  # isort:skip
from .query_store import SqlAlchemyQueryStore  # isort:skip
from .html_site_store import HtmlSiteStore  # isort:skip


for module_name, package_name in [
    (".store", "data_profiler.data_context.store"),
    (".validations_store", "data_profiler.data_context.store"),
    (".configuration_store", "data_profiler.data_context.store"),
    (".expectations_store", "data_profiler.data_context.store"),
    (".html_site_store", "data_profiler.data_context.store"),
    (".metric_store", "data_profiler.data_context.store"),
    (".checkpoint_store", "data_profiler.data_context.store"),
    (".store_backend", "data_profiler.data_context.store"),
    (".tuple_store_backend", "data_profiler.data_context.store"),
    (".database_store_backend", "data_profiler.data_context.store"),
    (".ge_cloud_store_backend", "data_profiler.data_context.store"),
]:
    verify_dynamic_loading_support(module_name=module_name, package_name=package_name)
