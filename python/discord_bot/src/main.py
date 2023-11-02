import os
from bot.client import client
import logging
from discord.utils import setup_logging

if __name__ == "__main__":
    setup_logging(level=logging.INFO)

    discord_logger = logging.getLogger("discord")
    discord_logger.setLevel(logging.INFO)

    asyncio_logger = logging.getLogger("asyncio")
    asyncio_logger.setLevel(logging.INFO)

    client.run(os.environ["TOKEN"], log_handler=None)
