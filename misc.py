from discord.ext import tasks, commands
from tictactoe import print_board


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

    @commands.command(name='tictactoe')
    async def play_tic_tac_toe(self, ctx):
        board = print_board()
        await ctx.send(board)


def setup(bot):
    bot.add_cog(Miscellaneous(bot))
