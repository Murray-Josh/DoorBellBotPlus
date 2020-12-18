import discord
import os
import time
import random
from discord.ext import commands
from discord.ext import commands


client = discord.Client()

bot = commands.Bot(command_prefix = '!')
startup_extensions = ["washer", "b99"]
BOT_TOKEN = "NzU4NDE5NzgyOTYxMzMyMjc1.X2urdw.RyvbayO1wgvnTeOZ78mHYMGBQAs"
global washingMachine
global dryer
global washingMachineUser

washingMachine = False
washingMachineUser = ""
dryer = False

@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))


def check_washer():
    global t0
    if washingMachine:
        return "No, " + str(washingMachineUser) + " is using it, " + str(
            round((2700 - (time.time() - t0)) / 60, 1)) + "mins left"
    else:
        return 'Yes :)'


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #doorBell()


@client.event
async def on_message(message):
    global washingMachine
    global washingMachineUser
    global t0

    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!dontdead'):
        await message.channel.send('open inside')

    if message.content.startswith('!dontopen'):
        await message.channel.send('dead inside')

    if message.content.startswith('!castles') :
        await message.channel.send('Are Cool!')

    if message.content.startswith("!use"):
        await message.channel.send('Done')
        washingMachine = True
        # print(message.author)
        washingMachineUser = message.author
        t0 = time.time()

    if message.content.startswith("!free"):
        await message.channel.send(check_washer())

    if message.content.startswith("!finish"):
        await message.channel.send('Done')
        washingMachine = False

bot.load_extension(extension)
# bot.run(BOT_TOKEN)
