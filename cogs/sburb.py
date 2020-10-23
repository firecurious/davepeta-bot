import discord
from discord.ext import commands
import asyncio

from random import *
#import plugins.sburb.classpects as classpects

class Sburb(commands.Cog):
    """Sburb-related commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, dice : str):
        """write something like 3d20 to roll dice"""

        channel = ctx.message.channel

        print(ctx.message.content)
        dice = ctx.message.content.split(" ")[1]
        print(dice)

        dice = [int(x) if x else 1 for x in dice.split("d")]
        numbers = [randint(1, dice[1]) for i in range(0, dice[0])]
        await channel.send("🎲 {0} = {1}".format(numbers, sum(numbers)))

    @commands.command()
    async def strife(self, action:str):
        """aggrieve or whatever"""
        chan = action.message.channel
        action = action.message.content.split(" ")[1]

        m = "this action is not implemented"

        if action == "aggrieve":
            m = "cost 2 damage 1, reuse ok"
        if action == "ok":
            m = "what"

        await chan.send(m)
            

    @commands.command()
    async def flip(self, ctx):
        """flips a single coin"""

        coins = ["heads", "tails"]
        shuffle(coins)
        await ctx.message.channel.send(coins[0])

    @commands.command()
    async def ball(self, ctx):
        """shitty 8ball knockoff"""

        choices = ["most likely", "no", "never", "no way",
                    "definitely", "yes", "it is certain",
                    "reply hazy", "i don't want to answer that",
                    "idk"]

        shuffle(choices)
        await ctx.message.channel.send(choices[0])

    @commands.command()
    async def secret(self, ctx, text:str):
        """secret"""

        cipher = "~!@#$%^&*()_+`1234567890-="
        abc = "abcdefghijklmnopqrstuvwxyz"

        english_table = text.maketrans(cipher, abc) #cipher to abc
        cipher_table = text.maketrans(abc, cipher) #abc to cipher

        for char in abc:
            if char in text:
                await ctx.message.channel.send(text.translate(cipher_table))
                return

        await ctx.message.channel.send(text.translate(english_table))

def setup(bot):
    bot.add_cog(Sburb(bot))