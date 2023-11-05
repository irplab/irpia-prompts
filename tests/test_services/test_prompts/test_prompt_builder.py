import pytest

from app.config import get_app_settings
from app.models.metadata import Metadata
from app.services.prompts.prompt_builder import PromptBuilder

settings = get_app_settings()


@pytest.fixture(name="prompt_builder")
def fixture_prompt_builder():
    """
    Provide the most basic prompt builder
    :return:
    """
    return PromptBuilder(template="gpt-3.5-curie-ft-keywords.jinja2",
                         engine_settings=settings.engines.get(settings.engine))


def test_create_basic_prompt(prompt_builder):
    """
    Test create basic prompt

    :param prompt_builder:
    :return:
    """
    prompt = prompt_builder.build(Metadata(title='foo', description='bar'))
    assert prompt == 'Title : foo\nDescription : bar\n\n###\n\n'
