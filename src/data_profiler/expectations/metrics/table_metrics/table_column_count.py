from typing import Any, Dict, Optional, Tuple

from data_profiler.core import ExpectationConfiguration
from data_profiler.execution_engine import (
    ExecutionEngine,
    PandasExecutionEngine,
    SparkDFExecutionEngine,
)
from data_profiler.execution_engine.execution_engine import MetricDomainTypes
from data_profiler.execution_engine.sqlalchemy_execution_engine import (
    SqlAlchemyExecutionEngine,
)
from data_profiler.expectations.metrics.metric_provider import metric_value
from data_profiler.expectations.metrics.table_metric_provider import (
    TableMetricProvider,
)
from data_profiler.validator.validation_graph import MetricConfiguration


class TableColumnCount(TableMetricProvider):
    metric_name = "table.column_count"

    @metric_value(engine=PandasExecutionEngine)
    def _pandas(
        cls,
        execution_engine: "ExecutionEngine",
        metric_domain_kwargs: Dict,
        metric_value_kwargs: Dict,
        metrics: Dict[Tuple, Any],
        runtime_configuration: Dict,
    ):
        columns = metrics.get("table.columns")
        return len(columns)

    @metric_value(engine=SqlAlchemyExecutionEngine)
    def _sqlalchemy(
        cls,
        execution_engine: "ExecutionEngine",
        metric_domain_kwargs: Dict,
        metric_value_kwargs: Dict,
        metrics: Dict[Tuple, Any],
        runtime_configuration: Dict,
    ):
        columns = metrics.get("table.columns")
        return len(columns)

    @metric_value(engine=SparkDFExecutionEngine)
    def _spark(
        cls,
        execution_engine: "ExecutionEngine",
        metric_domain_kwargs: Dict,
        metric_value_kwargs: Dict,
        metrics: Dict[Tuple, Any],
        runtime_configuration: Dict,
    ):
        columns = metrics.get("table.columns")
        return len(columns)

    @classmethod
    def _get_evaluation_dependencies(
        cls,
        metric: MetricConfiguration,
        configuration: Optional[ExpectationConfiguration] = None,
        execution_engine: Optional[ExecutionEngine] = None,
        runtime_configuration: Optional[dict] = None,
    ):
        dependencies: dict = super()._get_evaluation_dependencies(
            metric=metric,
            configuration=configuration,
            execution_engine=execution_engine,
            runtime_configuration=runtime_configuration,
        )
        table_domain_kwargs: dict = {
            k: v for k, v in metric.metric_domain_kwargs.items() if k != "column"
        }
        dependencies["table.columns"] = MetricConfiguration(
            metric_name="table.columns",
            metric_domain_kwargs=table_domain_kwargs,
            metric_value_kwargs=None,
            metric_dependencies=None,
        )
        return dependencies
