import time
import os
import discord
from discord.ext import commands
from config.config import Settings

description = "Discord Server Wrapper"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

async def bot_run():
    print(f"Starting bot")
    try:
        await bot.start(Settings().DISCORD_TOKEN)
    except KeyboardInterrupt:
        await bot.logout()
