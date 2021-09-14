from data_profiler.render.renderer.content_block.expectation_string import (
    ExpectationStringRenderer,
)
from data_profiler.render.types import RenderedBulletListContent


class ExpectationSuiteBulletListContentBlockRenderer(ExpectationStringRenderer):
    _rendered_component_type = RenderedBulletListContent
    _content_block_type = "bullet_list"

    _default_element_styling = {
        "default": {"classes": ["badge", "badge-secondary"]},
        "params": {"column": {"classes": ["badge", "badge-primary"]}},
    }
