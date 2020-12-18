import discord
from discord.ext import commands
import random

class Brooklyn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '99')
    async def nine_nine(self, ctx):
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