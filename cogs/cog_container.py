import random
import time

import discord
from discord.ext import commands, tasks
from prompts import *
from bot import change_status
from youtube_component import youtube_search

class BotCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game(random.choice(game)))
        change_status.start()
        print("Bot is online.")


    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} has joined a server.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} has left a server.")

    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @commands.command(aliases=["randomquestion"])
    async def question(self, ctx, *, question):
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(rq_response)}")

    @commands.command()
    async def send(self, ctx, *, content):
        if content.startswith("youtube"):
            print("Finding random YouTube video:")
            yt_output = youtube_search()
            await ctx.send(f"https://www.youtube.com/watch?v={yt_output}")
        if content == "it":
            await ctx.send("Are you silly?")
            time.sleep(1.4)
            await ctx.send(f"I'm still gonna send it")
            time.sleep(1.4)
            haiku_random = random.choice(sent_it)
            await ctx.send(haiku_random)
        if content.startswith("reddit"):
            pass
        if content.startswith("imgur"):
            pass
        if content.startswith("spotify"):
            pass

    @commands.command()
    async def urban(self, ctx, *, content):
        await ctx.send(f"https://www.urbandictionary.com/define.php?term={content}")

def setup(client):
    client.add_cog(BotCommands(client))