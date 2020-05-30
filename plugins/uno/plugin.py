import discord
from discord.ext import commands
import asyncio

from random import *

class Card(object):
    """TODO"""

    def __init__(self, color, number, category):
        self.color = color #red, green, blue, yellow, none
        self.number = number #0-9 or none
        self.category = category
        #regular, draw two, skip, reverse, wild, wild draw 4

    def __repr__(self):
        if self.category == "regular":
            return "{0} {1}".format(self.color, self.number)
        elif "wild" in self.category:
            return self.category
        else:
            return "{0} {1}".format(self.color, self.category)
        

class Game(object):
    """TODO: write this docstring"""

    def __init__(self):
        self.players =  {}
        self.deck = []

        self._build()

    def _build(self):

        for color in ["red", "green", "blue", "yellow"]:
            for i in range(0, 9+1):
                n = 1 if i == 0 else 2 #only one 0 card, two of others

                for x in range(0, n):
                    self.deck.append(Card(color, i, "regular"))

            for x in range(0, 2):
                for category in ["draw two", "reverse", "skip"]:
                    self.deck.append(Card(color, None, category))

        for x in range(0, 4):
            for category in ["wild", "wild draw four"]:
                self.deck.append(Card(None, None, category))

        
#TODO: multiple game objects
class Uno(commands.Cog):
    """Uno-related commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def uno(self, ctx):
        """blah"""

        game = Game()
        print(game.deck)
        print(len(game.deck))
        print(ctx.message)

        await self.bot.say(game.deck)
        await self.bot.say("#" + repr(ctx.message.channel.id))


def setup(bot):
    bot.add_cog(Uno(bot))