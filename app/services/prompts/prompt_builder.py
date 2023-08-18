from jinja2 import Environment, FileSystemLoader

from app.models.metadata import Metadata
from app.settings.app_settings import AppSettings


class PromptBuilder:
    """
    Utility to build prompts from templates and metadata
    """

    def __init__(self, template: str, settings: AppSettings):
        self.template = template
        self.settings = settings
        self.env = Environment(
            loader=FileSystemLoader(settings.template_directory))

    def build(self, metadata: Metadata) -> str:
        """
        Populate template with metadata values

        :param metadata:
        :return:
        """
        template = self.env.get_template(self.template)
        return template.render(metadata=metadata, settings=self.settings)
