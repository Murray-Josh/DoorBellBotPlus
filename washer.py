import discord
import os
import time
import random
from discord.ext import commands
#bot = commands.Bot(command_prefix='!')
#BOT_TOKEN = "NzU4NDE5NzgyOTYxMzMyMjc1.X2urdw.RyvbayO1wgvnTeOZ78mHYMGBQAs"

@bot.command(name='test')
async def washer_test(ctx):
    await ctx.send("Testing")

#bot.run(BOT_TOKEN)
