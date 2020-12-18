from discord.ext import tasks, commands


class Miscellaneous(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.printer.start()
        # bot.bg_task = bot.loop.create_task(Miscellaneous.my_background_task())

    def cog_unload(self):
        self.printer.cancel()

    @commands.command(name='dontdead')
    async def dont_dead(self, ctx):
        await ctx.send('Open inside.')

    @commands.command(name='misc')
    async def misc_function(self, ctx):
        await ctx.send('Well done, you\'ve called a misc function.')

    @tasks.loop(seconds=5.0)
    async def printer(self):
        print(self.index)
        self.index += 1


def setup(bot):
    bot.add_cog(Miscellaneous(bot))
