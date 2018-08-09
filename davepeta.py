import discord
from discord.ext import commands
import os

from settings import token
import random

description = '''Davepeta bot'''

bot = commands.Bot(command_prefix="<", description=description)

@bot.event
async def on_ready():
    print("logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")
    bot.change_presence(game=discord.Game(name='by themself'))

#TODO: move chatter to a plugin
@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith("hello"):
        phrases = ["hi", "shh", "hello"]
        phrase = random.choice(phrases)
        msg = phrase.format(message)
        await bot.send_message(message.channel, msg)

    if message.content.startswith("blah blah blah"):
        msg = "[some stuff]".format(message)
        await bot.send_message(message.channel, msg)

    await bot.process_commands(message)
    
@bot.command()
async def reload(name):
    plugin = "plugins." + name + ".plugin"
    try:
        bot.unload_extension(plugin)
        bot.load_extension(plugin)
        text = 'reloaded {}'.format(name)
    except Exception as e:
        text = '{}: {}'.format(type(e).__name__, e)
               
    print(text)
    await bot.say(text)


#TODO: put this into a function so it looks neater?
#load plugins
for folder in os.listdir("plugins"):
    try:
        print("loading %s" %folder)
        bot.load_extension("plugins.%s.plugin" %folder)
    except ImportError as e:
        print("failed to load %s; check if there's a plugin.py" %folder)
        print(e)

#TODO: move token to external file and blacklist it with git
bot.run(token)