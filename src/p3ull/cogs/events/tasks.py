import logging
import aiohttp
from disnake.ext import plugins, tasks



plugin = plugins.Plugin(name="Tasks")

headers = {
    "User-Agent": "Magic Browser"
}

URL = "https://app.playa3ull.games/api/coin/price"



@plugin.register_loop(wait_until_ready=True)
@tasks.loop(minutes=2)
async def price_update():
    async with aiohttp.request("GET", URL, headers=headers) as r:
        data = await r.json()
        price = data["pairs"][0]["priceUsd"]
        guild = plugin.bot.get_guild(928522309596237835)
        await guild.me.edit(nick=f"${price} USD")

        

setup, teardown = plugin.create_extension_handlers()