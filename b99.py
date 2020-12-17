import discord
import os
import time
import random
from discord.ext import commands
class Brooklyn():
    def __init__(self, bot):
        self.bot = bot
    @bot.command(name='99')
    async def nine_nine(ctx):
        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]

        response = random.choice(brooklyn_99_quotes)
        await ctx.send(response)

def setup(bot):
    bot.add_cog(Brooklyn(bot))