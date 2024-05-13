import time
import os
import discord
import json
from collections import namedtuple
from discord.ext import commands
from config.config import Settings
from tasks.toxic_ticket_queue import *
from services.subscriber import *
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
async def addtt(ctx, amount: int, username: str):
    # discord usernames come with a <@ ... > wrapped around the string so we splice it away
    username = username[2:-1]
    await add_ticket_to_user({
        "username": username,
        "ticket_type": "toxic_ticket",
        "amount": amount,
        "issuer": str(ctx.author.id),
        "channel": str(ctx.message.channel.id)
    })

async def send_message(message: str, channel: str):
    channel = bot.get_channel(int(channel))
    await channel.send(message)

async def start_bot():
    async with bot:
        await bot.start(Settings().DISCORD_TOKEN)

async def main_loop():
    tasks = [
        asyncio.create_task(start_bot())
    ]
    await asyncio.wait(tasks)
