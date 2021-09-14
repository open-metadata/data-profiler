from data_profiler.expectations.expectation import TableExpectation
from data_profiler.expectations.util import render_evaluation_parameter_string
from data_profiler.render.renderer.renderer import renderer
from data_profiler.render.types import (
    RenderedStringTemplateContent,
    RenderedTableContent,
)
from data_profiler.render.util import num_to_str, substitute_none_for_missing


class ExpectColumnParameterizedDistributionKsTestPValueToBeGreaterThan(
    TableExpectation
):
    # This expectation is a stub - it needs migration to the modular expectation API

    # This dictionary contains metadata for display in the public gallery
    library_metadata = {
        "maturity": "production",
        "package": "data_profiler",
        "tags": [
            "core expectation",
            "column aggregate expectation",
            "needs migration to modular expectations api",
        ],
        "contributors": ["@data_profiler"],
        "requirements": [],
    }

    metric_dependencies = tuple()
    success_keys = ()
    default_kwarg_values = {}

    @classmethod
    @renderer(renderer_type="renderer.prescriptive")
    @render_evaluation_parameter_string
    def _prescriptive_renderer(
        cls,
        configuration=None,
        result=None,
        language=None,
        runtime_configuration=None,
        **kwargs,
    ):
        pass

    @classmethod
    @renderer(renderer_type="renderer.diagnostic.observed_value")
    def _diagnostic_observed_value_renderer(
        cls,
        configuration=None,
        result=None,
        language=None,
        runtime_configuration=None,
        **kwargs,
    ):
        pass
