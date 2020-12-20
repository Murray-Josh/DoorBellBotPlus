import gpiozero
from gpiozero import Button, LED, Buzzer, RGBLED
from colorzero import Color

from discord.ext import tasks, commands

from time import sleep

class PiBell(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.x = 4
        self.button = Button(self.x,False,None)
        self.led = LED(14)
        self.led_working = RGBLED(16,20,21)
        self.bell_channel_id = 789226620821045278
        #self.buzzer = Buzzer(15)
        self.led_working.color = Color('green')
        print(self.button.pull_up)
        self.send_onready_message.start()
        self.reset_color_led.start()


    @tasks.loop(seconds = 5)
    async def reset_color_led(self):
        self.led_working.color = Color('green')

    @commands.command()
    async def command_color_led(self, ctx):
        print ('command')
        self.led_working.color = Color('orange')

    @tasks.loop()
    async def send_onready_message(self):
        if self.button.is_pressed:
                self.led_working.color = Color('blue')
                print("Button is pressed")
                channel = self.bot.get_channel(int(self.bell_channel_id))
                #channel = self.bot.channels.find("bell")
                await channel.send("Bell has been rung")
                self.led.on()
                #self.buzzer.on()
                sleep(0.5)
                self.led.off()
                #self.buzzer.off()

    @send_onready_message.before_loop  # wait for the client before starting the task
    async def before_send(self):
        await self.bot.wait_until_ready()

        return

    @send_onready_message.after_loop  # destroy the task once it's done
    async def after_send(self):
        self.send_onready_message.close()

        return

    def exit_handler():
        self.led_working.off()

def setup(bot):
    bot.add_cog(PiBell(bot))


