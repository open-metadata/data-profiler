from data_profiler.core.usage_statistics.anonymizers.anonymizer import Anonymizer
from data_profiler.execution_engine import (
    ExecutionEngine,
    PandasExecutionEngine,
    SparkDFExecutionEngine,
    SqlAlchemyExecutionEngine,
)


class ExecutionEngineAnonymizer(Anonymizer):
    def __init__(self, salt=None):
        super().__init__(salt=salt)

        # ordered bottom up in terms of inheritance order
        self._ge_classes = [
            PandasExecutionEngine,
            SparkDFExecutionEngine,
            SqlAlchemyExecutionEngine,
            ExecutionEngine,
        ]

    def anonymize_execution_engine_info(self, name, config):
        anonymized_info_dict = {}
        anonymized_info_dict["anonymized_name"] = self.anonymize(name)

        self.anonymize_object_info(
            anonymized_info_dict=anonymized_info_dict,
            ge_classes=self._ge_classes,
            object_config=config,
        )

        return anonymized_info_dict
