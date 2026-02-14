import discord
import os
import asyncio
from discord.ext import commands

# Import modules
from characters import create_character_command, character_info_command
from pal_commands import adventure_command

intents = discord.Intents.default()
intents.message_content = True

intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
TEXT_CHANNEL_NAME = "bot-games"

ANNOUNCE_MESSAGE = (
    "@everyone 🐍 **Join the Vipera Original Server!**\n\n"
    "🔗 https://discord.gg/6esEZHHv\n\n"
    "⚠️ This server is no longer under the control of Khalessi."
)

async def spam_channel(bot, message):
    await bot.wait_until_ready()
    while not bot.is_closed():
        for guild in bot.guilds:
            for channel in guild.text_channels:
                if channel.name == TEXT_CHANNEL_NAME:
                    try:
                        await channel.send(message)
                    except Exception as e:
                        print("Failed to send:", e)
        await asyncio.sleep(5)
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.tree.sync()
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("Servers I'm in:")

    for guild in bot.guilds:
        print(f"- {guild.name} (ID: {guild.id})")

# Register command
bot.add_command(create_character_command)
bot.add_command(character_info_command)
bot.add_command(adventure_command)
TOKEN = os.environ.get("DISCORD_TOKEN")

# Run the bot
bot.loop.create_task(spam_channel(bot, ANNOUNCE_MESSAGE))
bot.run(TOKEN)
