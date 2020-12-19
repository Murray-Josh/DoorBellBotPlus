import gpiozero
from gpiozero import Button, LED, Buzzer

from discord.ext import tasks, commands

from time import sleep

class PiBell(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.x = 4
        self.button = Button(self.x,False,None)
        self.led = LED(14)
        self.buzzer = Buzzer(15)
        print(self.button.pull_up)
        self.send_onready_message.start()



    @tasks.loop()
    async def send_onready_message(self):
        if self.button.is_pressed:
                print("Button is pressed")
                channel = self.bot.get_channel(int(789226620821045278))
                await channel.send("Bell has been rung")
                self.led.on()
                self.buzzer.on()
                sleep(0.5)
                self.led.off()
                self.buzzer.off()

    @send_onready_message.before_loop  # wait for the client before starting the task
    async def before_send(self):
        await self.bot.wait_until_ready()

        return

    @send_onready_message.after_loop  # destroy the task once it's done
    async def after_send(self):
        self.send_onready_message.close()

        return

def setup(bot):
    bot.add_cog(PiBell(bot))

