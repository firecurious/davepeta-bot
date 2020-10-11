import discord
import os
from discord.ext import commands
from settings import token

bot = commands.Bot(command_prefix="<")

@bot.event
async def on_ready():
    print("ready", bot.user)

@bot.command()
async def load(ctx, extension):
    print("l")
    bot.load_extension(f"cogs.{extension}")
    await ctx.send("loaded")

@bot.command()
async def unload(ctx, extension):
    print("u")
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send("unloaded")

for filename in os.listdir("cogs"):
    if ".py" in filename:
        f = filename.replace(".py", "")
        bot.load_extension(f"cogs.{f}")
        print(f"loaded {f}")

#@bot.command()
#unload

bot.run(token)