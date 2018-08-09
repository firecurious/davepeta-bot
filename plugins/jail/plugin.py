import discord
from discord.ext import commands
import asyncio

class Jail:
    """Jail-related commands"""

    def __init__(self, bot):
        self.bot = bot
        self.reports = {}
        self.bank = {}
        self.people = {}
        self.jobs = ["policeman", "plumber", "meme dealer", "cowboy"]

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

        await self.bot.say("{0} has been reported to the police for {1}".format(p, reason))
        self.jobs[p] = reason

    @commands.command(pass_context=True)
    async def register(self, ctx, *message):
        """register <job>"""
        
        p = ctx.message.author
        
        for job in self.jobs:
            if job in " ".join(message):
                await self.bot.say("okay, you're now a %s." %job)
                self.people[p] = job
                self.bank[p] = 0
                return

        print(message)
        await self.bot.say("you're not qualified to do that")
        
    @commands.command(pass_context=True)
    async def status(self, ctx, *message):
        """see what job you have"""
        
        p = ctx.message.author
        money = self.bank[p] if p in self.bank else 0
        text = "your job is %s. you have %s" %(self.people[p], money) if p in self.people else "you're jobless. jobs are %s" %self.jobs
        await self.bot.say(text)

    @commands.command(pass_context=True)
    async def work(self, ctx):
        """work"""
        
        p = ctx.message.author
        
        if p in self.people:
            text = "you worked for 1 hour as a %s. you make $1/hour" %self.people[p]
            self.bank[p] += 1
            
        
        else:
            text = "you don't have a job."

        await self.bot.say(text)
                                

def setup(bot):
    bot.add_cog(Jail(bot))