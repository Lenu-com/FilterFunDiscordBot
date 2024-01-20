from app.infrastructure.factories.discord_connector_factory import DiscordConnectorFactory


def main() -> None:
    discord_connector = DiscordConnectorFactory.create()
    discord_connector.run()
    
    
if __name__ == "__main__":
    main()