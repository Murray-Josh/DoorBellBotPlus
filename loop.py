from discord.ext import tasks, commands

class Loop(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.send_onready_message.start()

    @tasks.loop(seconds = 5)
    async def send_onready_message(self):
        channel = self.bot.get_channel(int(789159233861320727))
        await channel.send(self.index)
        self.index += 1


    @send_onready_message.before_loop  # wait for the client before starting the task
    async def before_send(self):
        await self.bot.wait_until_ready()

        return

    @send_onready_message.after_loop  # destroy the task once it's done
    async def after_send(self):
        self.send_onready_message.close()

        return

def setup(bot):
    bot.add_cog(Loop(bot))
