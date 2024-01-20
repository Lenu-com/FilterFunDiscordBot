from discord.ext.commands import Bot


class DiscordConnector:
    def __init__(self, bot: Bot, api_key: str) -> None:
        self.bot = bot
        self.api_key = api_key
        
    
    def run(self) -> None:
        self.bot.run(self.api_key)
