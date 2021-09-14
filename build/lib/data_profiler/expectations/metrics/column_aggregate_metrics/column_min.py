from data_profiler.execution_engine import (
    PandasExecutionEngine,
    SparkDFExecutionEngine,
)
from data_profiler.execution_engine.sqlalchemy_execution_engine import (
    SqlAlchemyExecutionEngine,
)
from data_profiler.expectations.metrics.column_aggregate_metric_provider import (
    ColumnAggregateMetricProvider,
    column_aggregate_partial,
    column_aggregate_value,
)
from data_profiler.expectations.metrics.column_aggregate_metric_provider import (
    sa as sa,
)
from data_profiler.expectations.metrics.import_manager import F


class ColumnMin(ColumnAggregateMetricProvider):
    metric_name = "column.min"

    @column_aggregate_value(engine=PandasExecutionEngine)
    def _pandas(cls, column, **kwargs):
        return column.min()

    @column_aggregate_partial(engine=SqlAlchemyExecutionEngine)
    def _sqlalchemy(cls, column, **kwargs):
        return sa.func.min(column)

    @column_aggregate_partial(engine=SparkDFExecutionEngine)
    def _spark(cls, column, **kwargs):
        return F.min(column)
