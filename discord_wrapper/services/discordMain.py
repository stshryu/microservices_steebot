import time
import os
import discord
import json
from collections import namedtuple
from discord.ext import commands
from config.config import Settings
from services.utils.discord_formatted_messages import *
from tasks.toxic_ticket_queue import *
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
    username = await validate_and_strip_username(username)
    if username:
        await add_ticket_to_user({
            "username": username,
            "ticket_type": "toxic_ticket",
            "amount": amount,
            "issuer": str(ctx.author.id),
            "channel": str(ctx.message.channel.id)
        })
    else:
        await send_message(
            discord_formatted_messages['invalid_username'],
            ctx.message.channel.id
        )

@bot.command()
async def tt(ctx, username: str):
    username = await validate_and_strip_username(username)
    if username:
        await get_user_statistics({
            "retrieval": "True",
            "username": username,
            "channel": ctx.channel.id
        })
    else:
        await send_message(
            discord_formatted_messages['invalid_username'],
            ctx.message.channel.id
        )

@bot.command()
async def tthelp(ctx):
    await send_message(
        discord_formatted_messages['help'],
        ctx.message.channel.id
    )

async def validate_and_strip_username(username: str):
    # Ensure that a valid username is being passed in (soft validation, not hardened to manually wrapper values)
    username_tag = username[:2] + username[-1]
    # Discord wraps a <@ ... > around the username so we strip it away
    username = username[2:-1]
    return username if username_tag == "<@>" else False

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
