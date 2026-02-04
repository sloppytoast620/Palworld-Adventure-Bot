import discord
import os
from discord.ext import commands

# Import modules
from characters import create_character_command, character_info_command
from pals import explore_command

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Register commands
bot.add_command(create_character_command)
bot.add_command(character_info_command)
bot.add_command(explore_command)
TOKEN = os.getenv(DISCORD_TOKEN)

# Run the bot
bot.run(TOKEN)
