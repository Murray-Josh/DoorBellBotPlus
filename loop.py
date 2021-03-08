from discord.ext import tasks, commands


class Loop(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.send_onready_message.start()
        self.looping = False

    @tasks.loop(seconds=5)
    async def send_onready_message(self):
        if self.looping:
            channel = self.bot.get_channel(int(789226620821045278))
            await channel.send(self.index)
            self.index += 1

    @send_onready_message.before_loop  # wait for the client before starting the task
    async def before_send(self):
        await self.bot.wait_until_ready()

        return

    # @send_onready_message.after_loop  # destroy the task once it's done
    # async def after_send(self):
    #    self.send_onready_message.close()

    #    return

    @commands.command(name='loop')
    async def misc_function(self, ctx):
        self.looping = not self.looping
        if self.looping:
            await ctx.send('Loop has been enabled')
        else:
            await ctx.send('Loop has been disabled')


def setup(bot):
    bot.add_cog(Loop(bot))
