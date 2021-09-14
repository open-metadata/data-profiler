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
from data_profiler.expectations.metrics.import_manager import F, sa


class ColumnMax(ColumnAggregateMetricProvider):
    metric_name = "column.max"

    @column_aggregate_value(engine=PandasExecutionEngine)
    def _pandas(cls, column, **kwargs):
        return column.max()

    @column_aggregate_partial(engine=SqlAlchemyExecutionEngine)
    def _sqlalchemy(cls, column, **kwargs):
        return sa.func.max(column)

    @column_aggregate_partial(engine=SparkDFExecutionEngine)
    def _spark(cls, column, **kwargs):
        return F.max(column)
