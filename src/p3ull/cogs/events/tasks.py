import logging
import aiohttp
from disnake.ext import plugins, tasks



plugin = plugins.Plugin(name="Tasks")

URL = "https://app.playa3ull.games/api/coin/price"

@plugin.register_loop(wait_until_ready=True)
@tasks.loop(minutes=2)
async def price_update():
    async with aiohttp.request("GET", "https://app.playa3ull.games/api/coin/price", ) as r:
        data = await r.text()
        data = float(data)
        data = round(float(data), 6)
        logging.info(data)
        for guild in plugin.bot.guilds:
            try:
                await guild.me.edit(nick=f"${data} USD")
            except Exception as e:
                pass
        

setup, teardown = plugin.create_extension_handlers()