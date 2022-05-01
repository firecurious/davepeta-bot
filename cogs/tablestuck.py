import discord
from discord.ext import commands
import asyncio

import os, csv
#import plugins.sburb.classpects as classpects

class Tablestuck(commands.Cog):
    """Tablestuck-related commands"""

    def __init__(self, bot):
        self.bot = bot
        self.items = {}

        files = os.listdir("./cogs/table_data")
        for f in files:
            with open("./cogs/table_data/" + f) as _f:
                reader = csv.reader(_f)
                items = [row for row in reader]
            for i in items:
                self.items[i[0]] = {"code": i[1], "tier": i[2]}

    @commands.command()
    async def item(self, ctx):
        """item lookup"""

        channel = ctx.message.channel

        print(ctx.message.content)
        item = ctx.message.content.split("<item ")[1]
        await channel.send(self.items[item])

    @commands.command()
    async def stats(self, ctx, char):
        """stat lookup
        <stats name"""

        chan = ctx.message.channel
        await chan.send(char)


def setup(bot):
    bot.add_cog(Tablestuck(bot))