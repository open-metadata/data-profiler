import logging

from data_profiler.expectations.metrics.metric_provider import MetricProvider

logger = logging.getLogger(__name__)


class TableMetricProvider(MetricProvider):
    domain_keys = (
        "batch_id",
        "table",
        "row_condition",
        "condition_parser",
    )
