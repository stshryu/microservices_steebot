import time
import os
import discord
from discord.ext import commands
from config.config import Settings
import asyncio

description = "Discord Server Wrapper"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("-------")

@bot.command()
async def foo(ctx, arg):
    print(f"{arg=}")
    await ctx.send(arg)

async def start_bot():
    async with bot:
        await bot.start(Settings().DISCORD_TOKEN)

async def main_loop():
    tasks = [
        asyncio.create_task(start_bot())
    ]
    await asyncio.wait(tasks)
