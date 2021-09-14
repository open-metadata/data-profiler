import json

from data_profiler.execution_engine import (
    PandasExecutionEngine,
    SparkDFExecutionEngine,
)
from data_profiler.expectations.metrics.import_manager import F, sparktypes
from data_profiler.expectations.metrics.map_metric_provider import (
    ColumnMapMetricProvider,
    column_condition_partial,
)


class ColumnValuesJsonParseable(ColumnMapMetricProvider):
    condition_metric_name = "column_values.json_parseable"

    @column_condition_partial(engine=PandasExecutionEngine)
    def _pandas(cls, column, **kwargs):
        def is_json(val):
            try:
                json.loads(val)
                return True
            except:
                return False

        return column.map(is_json)

    @column_condition_partial(engine=SparkDFExecutionEngine)
    def _spark(cls, column, json_schema, **kwargs):
        def is_json(val):
            try:
                json.loads(val)
                return True
            except:
                return False

        is_json_udf = F.udf(is_json, sparktypes.BooleanType())

        return is_json_udf(column)
