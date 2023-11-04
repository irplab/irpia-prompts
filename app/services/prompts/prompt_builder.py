from jinja2 import Environment, FileSystemLoader

from app.config import get_app_settings
from app.models.metadata import Metadata
from app.settings.app_settings import AppSettings


class PromptBuilder:
    """
    Utility to build prompts from templates and metadata
    """

    def __init__(self, template: str, engine_settings: dict):
        settings: AppSettings = get_app_settings()
        self.template = template
        self.engine_settings = engine_settings
        self.env = Environment(
            loader=FileSystemLoader(settings.template_directory))

    def build(self, metadata: Metadata) -> str:
        """
        Populate template with metadata values

        :param metadata:
        :return:
        """
        template = self.env.get_template(self.template)
        return template.render(metadata=metadata, settings=self.engine_settings)
