from discord.ext import tasks, commands
from tictactoe import print_board
import fileinput

class Miscellaneous(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        # bot.bg_task = bot.loop.create_task(Miscellaneous.my_background_task())

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

    @commands.command(name='setring')
    async def set_ring(self, ctx,arg, arg2):
        ftime = open("SwanData.txt.txt", "r")
        found = False
        lineNum = 0
        listOfLines = []
        for line in ftime:
            listOfLines.append(line)
            lineNum += 1
            values = line.split()
            if values[0] == arg:
                found = True
                listOfLines[lineNum] = str(values[0] +" " +arg2)
        if found:
            ftime.writelines(listOfLines)
            ftime.close()
            await ctx.send("Found and renamed")

        else:
            await ctx.send("Time not found :(")



def setup(bot):
    bot.add_cog(Miscellaneous(bot))
