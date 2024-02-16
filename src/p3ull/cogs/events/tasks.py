import logging
import aiohttp
from disnake.ext import plugins, tasks



plugin = plugins.Plugin(name="Tasks")

headers = {
    "User-Agent": "Magic Browser"
}

URL = "https://app.playa3ull.games/api/coin/price"



@plugin.register_loop(wait_until_ready=True)
@tasks.loop(seconds=3)
async def price_update():
    async with aiohttp.request("GET", URL, headers=headers) as r:
        data = await r.json()
        logging.info(data)
        guild = plugin.bot.get_guild(928522309596237835)
        await guild.me.edit(nick=f"${data} USD")

        

setup, teardown = plugin.create_extension_handlers()