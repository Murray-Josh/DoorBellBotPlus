from discord.ext import commands


class Miscellaneous(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='dontdead')
    async def dont_dead(self, ctx):
        await ctx.send('Open inside.')

    @commands.command(name='misc')
    async def misc_function(self, ctx):
        await ctx.send('Well done, you\'ve called a misc function.')


def setup(bot):
    bot.add_cog(Miscellaneous(bot))
