import discord
from discord import app_commands
from services.quotes import QuoteService
import logging

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

GUILD = discord.Object(id=1037471015216885791)
NEW_COMMANDS = False


@client.event
async def setup_hook():
    if not NEW_COMMANDS:
        return
    logging.info("Syncing commands...")
    tree.copy_global_to(guild=GUILD)
    await tree.sync(guild=GUILD)


@client.event
async def on_ready():
    logging.info(f"We have logged in as {client.user}")


@tree.command()
async def ping(interaction: discord.Interaction):
    """Pongs your pings"""
    logging.debug("Received ping")
    await interaction.response.send_message("Pong!")


@tree.command()
async def inspire(interaction: discord.Interaction):
    """Sends a random quote"""
    logging.debug("Received inspire")
    await interaction.response.send_message(QuoteService.get_quote())
