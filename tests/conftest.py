from unittest import mock

import pytest

from app.models.keywords import Keywords
from app.services.llm.gpt.gpt_chat_kw_suggestion_engine import GptChatKwSuggestionEngine


@pytest.fixture(autouse=True, scope='session')
def mock_gpt_engine():
    """
    Mandatory fixture to prevent OpenAI API calls during tests

    :return: fake suggestion engine
    """
    with mock.patch.object(GptChatKwSuggestionEngine, 'suggest', autospec=True,
                           return_value=Keywords(keywords=['foo', 'bar'])) as mock_engine:
        yield mock_engine
