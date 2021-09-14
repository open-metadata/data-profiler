from typing import Dict, Optional

from data_profiler.core.expectation_configuration import ExpectationConfiguration
from data_profiler.execution_engine import ExecutionEngine, PandasExecutionEngine
from data_profiler.expectations.util import render_evaluation_parameter_string

from ...render.renderer.renderer import renderer
from ...render.types import RenderedStringTemplateContent
from ...render.util import (
    parse_row_condition_string_pandas_engine,
    substitute_none_for_missing,
)
from ..expectation import ColumnExpectation, InvalidExpectationConfigurationError
from ..metrics.util import parse_value_set


class ExpectColumnDistinctValuesToEqualSet(ColumnExpectation):

    # This dictionary contains metadata for display in the public gallery
    library_metadata = {
        "maturity": "production",
        "package": "data_profiler",
        "tags": ["core expectation", "column aggregate expectation"],
        "contributors": ["@data_profiler"],
        "requirements": [],
    }

    # Setting necessary computation metric dependencies and defining kwargs, as well as assigning kwargs default values\
    metric_dependencies = ("column.value_counts",)
    success_keys = (
        "value_set",
        "parse_strings_as_datetimes",
    )

    # Default values
    default_kwarg_values = {
        "row_condition": None,
        "condition_parser": None,
        "value_set": None,
        "parse_strings_as_datetimes": None,
        "mostly": 1,
        "result_format": "BASIC",
        "include_config": True,
        "catch_exceptions": False,
    }

    def validate_configuration(self, configuration: Optional[ExpectationConfiguration]):
        """Validating that user has inputted a value set and that configuration has been initialized"""
        super().validate_configuration(configuration)
        if configuration is None:
            configuration = self.configuration
        try:
            assert "value_set" in configuration.kwargs, "value_set is required"
            assert isinstance(
                configuration.kwargs["value_set"], (list, set, dict)
            ), "value_set must be a list or a set"
            if isinstance(configuration.kwargs["value_set"], dict):
                assert (
                    "$PARAMETER" in configuration.kwargs["value_set"]
                ), 'Evaluation Parameter dict for value_set kwarg must have "$PARAMETER" key'
        except AssertionError as e:
            raise InvalidExpectationConfigurationError(str(e))
        return True

    @classmethod
    @renderer(renderer_type="renderer.prescriptive")
    @render_evaluation_parameter_string
    def _prescriptive_renderer(
        cls,
        configuration=None,
        result=None,
        language=None,
        runtime_configuration=None,
        **kwargs
    ):
        runtime_configuration = runtime_configuration or {}
        include_column_name = runtime_configuration.get("include_column_name", True)
        include_column_name = (
            include_column_name if include_column_name is not None else True
        )
        styling = runtime_configuration.get("styling")
        params = substitute_none_for_missing(
            configuration.kwargs,
            [
                "column",
                "value_set",
                "parse_strings_as_datetimes",
                "row_condition",
                "condition_parser",
            ],
        )

        if params["value_set"] is None or len(params["value_set"]) == 0:
            values_string = "[ ]"
        else:
            for i, v in enumerate(params["value_set"]):
                params["v__" + str(i)] = v

            values_string = " ".join(
                ["$v__" + str(i) for i, v in enumerate(params["value_set"])]
            )

        template_str = "distinct values must match this set: " + values_string + "."

        if params.get("parse_strings_as_datetimes"):
            template_str += " Values should be parsed as datetimes."

        if include_column_name:
            template_str = "$column " + template_str

        if params["row_condition"] is not None:
            (
                conditional_template_str,
                conditional_params,
            ) = parse_row_condition_string_pandas_engine(params["row_condition"])
            template_str = conditional_template_str + ", then " + template_str
            params.update(conditional_params)

        return [
            RenderedStringTemplateContent(
                **{
                    "content_block_type": "string_template",
                    "string_template": {
                        "template": template_str,
                        "params": params,
                        "styling": styling,
                    },
                }
            )
        ]

    def _validate(
        self,
        configuration: ExpectationConfiguration,
        metrics: Dict,
        runtime_configuration: dict = None,
        execution_engine: ExecutionEngine = None,
    ):
        parse_strings_as_datetimes = self.get_success_kwargs(configuration).get(
            "parse_strings_as_datetimes"
        )
        observed_value_counts = metrics.get("column.value_counts")
        observed_value_set = set(observed_value_counts.index)
        value_set = self.get_success_kwargs(configuration).get("value_set")

        if parse_strings_as_datetimes:
            parsed_value_set = parse_value_set(value_set)
        else:
            parsed_value_set = value_set

        expected_value_set = set(parsed_value_set)

        return {
            "success": observed_value_set == expected_value_set,
            "result": {
                "observed_value": sorted(list(observed_value_set)),
                "details": {"value_counts": observed_value_counts},
            },
        }
