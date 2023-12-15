import aiohttp
from disnake.ext import plugins, tasks



plugin = plugins.Plugin(name="Tasks")

headers = {
    "User-Agent": "Magic Browser"
}

URL = "https://api.dexscreener.com/latest/dex/tokens/0xa77e70d0af1ac7ff86726740db1bd065c3566937"



@plugin.register_loop(wait_until_ready=True)
@tasks.loop(minutes=2)
async def price_update():
    logging.info("updating price")
    async with aiohttp.request("GET", URL, headers=headers) as r:
        data = await r.json()
        price = data["pairs"][0]["priceUsd"]
        guild = plugin.bot.get_guild(928522309596237835)
        await guild.me.edit(nick=f"${price} USD")

        

setup, teardown = plugin.create_extension_handlers()