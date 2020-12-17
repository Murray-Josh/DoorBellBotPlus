import discord
import os
import time

client = discord.Client()
BOT_TOKEN = "NzU4NDE5NzgyOTYxMzMyMjc1.X2urdw.RyvbayO1wgvnTeOZ78mHYMGBQAs"
global washingMachine
global dryer
global washingMachineUser

washingMachine = False
washingMachineUser = ""
dryer = False


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


client.run(BOT_TOKEN)
