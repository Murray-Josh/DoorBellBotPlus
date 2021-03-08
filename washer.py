import time
from discord.ext import tasks, commands


class Washing(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.washing_machine_user = ''
        self.washingMachine = False
        self.washTime = 0
        self.washer_time_to_complete = 10

    @commands.command(name='use')
    async def use_washer(self, ctx):
        self.washingMachine = True
        self.washing_machine_user = ctx.author
        self.washTime = time.time()
        self.is_washer_done.start()

        await ctx.send('Done')

    @commands.command(name='free')
    async def free_washer(self, ctx):
        if self.washingMachine:
            await ctx.send("No, " + str(self.washing_machine_user) + " is using it, " +
                           str(round((self.washer_time_to_complete - (time.time() - self.washTime)) / 60,
                                     1)) + "minutes left")
        else:
            await ctx.send('Yes :)')

    @commands.command(name='test')
    async def washer_test(self, ctx):
        await ctx.send("Testing")

    @commands.command(name='finish')
    async def washer_end(self, ctx):
        self.washingMachine = False
        await ctx.send('Done')

    @tasks.loop(seconds=5)
    async def is_washer_done(self):
        if round((self.washer_time_to_complete - (time.time() - self.washTime)) / 60, 1) <= 0:
            channel = self.bot.get_channel(int(789226620821045278))

            await channel.send(self.washing_machine_user.mention
                               + " your washing is done")
            self.is_washer_done.stop()
            self.washingMachine = False


def setup(bot):
    bot.add_cog(Washing(bot))
