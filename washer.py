import discord
import os
import time
import random
from discord.ext import commands
class Washing():
    def __init__(self, bot):
        self.bot = bot
    @bot.command(name='test')
    async def washer_test(ctx):
        await ctx.send("Testing")

def setup(bot):
    bot.add_cog(Washing(bot))


