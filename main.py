import discord
import os

client = discord.Client()
washingMachine = False
washingMachineUser = ''
dryer = False

def checkWasher():
        if washingMachine == True:
            return 'NO!'+ washingMachineUser + "is using it"
        else:
            return 'Yes :)'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!dontdead'):
        await message.channel.send('open inside')

    if message.content.startswith('!dontopen') :
        await message.channel.send('dead inside')

    if message.content.startswith("!usewasher"):
        await message.channel.send('Done')
        washingMachine = True
        washingMachineUser = message.author
    
    if message.content.startswith("!washerfree"):
        await message.channel.send(checkWasher())

    if message.content.startswith("!finishwasher"):
        await message.channel.send('Done')
        washingMachine = False
  


        




client.run("NzU4NDE5NzgyOTYxMzMyMjc1.X2urdw.i2M1uF_wuCwaanweMNaK4ZRmT2E")