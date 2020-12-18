import time
from discord.ext import commands


class Washing(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.washingMachineUser = ''
        self.washingMachine = False
        self.washTime = 0

    @commands.command(name='use')
    async def use_washer(self, ctx):
        self.washingMachine = True
        self.washingMachineUser = ctx.author
        self.washTime = time.time()
        await ctx.send('Done')

    @commands.command(name='free')
    async def free_washer(self, ctx):
        if self.washingMachine:
            await ctx.send("No, " + str(self.washingMachineUser) + " is using it, " + str(
                round((2700 - (time.time() - self.washTime)) / 60, 1)) + "minutes left")
        else:
            await ctx.send('Yes :)')

    @commands.command(name='test')
    async def washer_test(self, ctx):
        await ctx.send("Testing")

    @commands.command(name='finish')
    async def washer_end(self, ctx):
        self.washingMachine = False
        await ctx.send('Done')


def setup(bot):
    bot.add_cog(Washing(bot))
