import pytest

from app.config import get_app_settings
from app.models.metadata import Metadata
from app.services.llm.gpt.gpt_chat_kw_suggestion_service_factory \
    import GptChatKwSuggestionServiceFactory

settings = get_app_settings()


@pytest.fixture(name="suggestion_service")
def fixture_gpt_chat_suggestion_service():
    """
    Provide GPT chat suggestion service
    :return: GPT chat suggestion service
    """
    return GptChatKwSuggestionServiceFactory.suggestion_service(settings=settings)


@pytest.mark.asyncio
async def test_empty_metadata(suggestion_service):
    """
    Test that empty metadata return no keyword

    :param suggestion_service: GPT chat suggestion service fixture
    """
    keywords = await suggestion_service.suggest(Metadata(title='', description=''))
    assert len(keywords.keywords) == 0
