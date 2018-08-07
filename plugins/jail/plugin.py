import discord
from discord.ext import commands
import asyncio

class Jail:
    """Jail-related commands"""

    def __init__(self, bot):
        self.bot = bot
        self.reports = {}

    @commands.command()
    async def quit(self):
        await self.bot.say("shutting down")
        exit()

    @commands.command()
    async def report(self, *message):
        """>report user for reason"""

        text = " ".join([word for word in message])

        if "for" not in text:
            await self.bot.say("please state a reason")

        text = text.split(" for ")
        p = text[0]
        reason = text[1]

        await self.bot.say("{0} has been reported to the police for {1}".                       format(p, reason))

    @commands.command()
    async def register(self, *message):
        """register <job>"""

        await self.bot.say("you're not qualified to do that")

    @commands.command()
    async def bank(self):
        """bank"""

        await self.bot.say("you have $0")

    @commands.command()
    async def work(self):
        """work"""
        await self.bot.say("you don't have a job")
                                

def setup(bot):
    bot.add_cog(Jail(bot))