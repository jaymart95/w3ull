import asyncio
from p3ull.bot import Playa3ull
import logging
import config

formatter = logging.Formatter(
    fmt="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
)


logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


async def main():
    bot = Playa3ull()
    bot._load_extensions("p3ull.cogs")
    await bot.start(config.TOKEN)


asyncio.run(main())
