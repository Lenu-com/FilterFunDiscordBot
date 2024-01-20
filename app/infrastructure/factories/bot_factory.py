from discord import Intents
from discord.ext.commands import Bot


class BotFactory:
    @classmethod
    def create(cls) -> Bot:
        intents = Intents.all()
        bot = Bot(
            command_prefix="!",
            intents=intents
        )
        return bot