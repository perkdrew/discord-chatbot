import os
import random

import discord
from discord.ext import commands, tasks
from prompts import game

client = commands.Bot(command_prefix='.')

@tasks.loop(minutes=60.0)
async def change_status():
    await client.change_presence(activity=discord.Game(random.choice(game)))

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run('COPY TOKEN HERE')
