import discord
import os
from discord.ext import commands

# Import modules
from characters import create_character_command, character_info_command
from pals_commands import explore_command

intents = discord.Intents.default()
intents.message_content = True

intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.tree.sync()

# Register commands
bot.add_command(create_character_command)
bot.add_command(character_info_command)
bot.add_command(explore_command)
TOKEN = os.environ.get("DISCORD_TOKEN")

# Run the bot
bot.run(TOKEN)
