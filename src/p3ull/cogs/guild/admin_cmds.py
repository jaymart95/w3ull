
import disnake
from disnake.ext import plugins


plugin = plugins.Plugin(name="Admin Commands")


@plugin.slash_command_check
async def perms_check(inter: disnake.ApplicationCommandInteraction):
    if any(
        role.id == 932555792396218408
        for role in inter.author.roles
    ):
        return True
    else:
        return await inter.send(
            "You do not have permission to use this command.", ephemeral=True
        )


setup, teardown = plugin.create_extension_handlers()
