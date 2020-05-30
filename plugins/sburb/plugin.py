import discord
from discord.ext import commands
import asyncio

from random import *
import plugins.sburb.classpects as classpects

class Sburb(commands.Cog):
    """Sburb-related commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def blah_blah_blah(self):
        """blah"""

        await self.bot.say("[some stuff]")

    @commands.command()
    async def roll(self, dice : str):
        """write something like 3d20 to roll dice"""

        channel = dice.message.channel

        print(dice.message.content)
        dice = dice.message.content.split(" ")[1]
        print(dice)

        dice = [int(x) if x else 1 for x in dice.split("d")]
        numbers = [randint(1, dice[1]) for i in range(0, dice[0])]
        await channel.send("🎲 {0} = {1}".format(numbers, sum(numbers)))

    @commands.command()
    async def flip(self):
        """write something like 3d20 to roll dice"""

        coins = ["heads", "tails"]
        shuffle(coins)
        await self.bot.say(coins[0])

    @commands.command()
    async def ball(self):
        """shitty 8ball knockoff"""

        choices = ["most likely", "no", "never", "no way",
                    "definitely", "yes", "it is certain",
                    "reply hazy", "i don't want to answer that",
                    "idk"]

        shuffle(choices)
        await self.bot.say(choices[0])

    @commands.command()
    async def secret(self, text:str):
        """secret"""

        cipher = "~!@#$%^&*()_+`1234567890-="
        abc = "abcdefghijklmnopqrstuvwxyz"

        english_table = string.maketrans(cipher, abc) #cipher to abc
        cipher_table = string.maketrans(abc, cipher) #abc to cipher

        for char in abc:
            if char in text:
                await self.bot.say(text.translate(cipher_table))
                return

        await self.bot.say(text.translate(english_table))

def setup(bot):
    bot.add_cog(Sburb(bot))