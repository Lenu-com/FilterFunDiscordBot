import os
from app.infrastructure.factories.bot_factory import BotFactory
from app.infrastructure.discord_connector import DiscordConnector


class DiscordConnectorFactory:
    @classmethod
    def create(cls) -> DiscordConnector:
        bot = BotFactory.create()
        api_key = os.environ["DISCORD_API_KEY"]
        return DiscordConnector(bot, api_key)