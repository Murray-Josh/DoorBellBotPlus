import asyncio

import gpiozero
from gpiozero import Button, LED, Buzzer, RGBLED
from colorzero import Color

from discord.ext import tasks, commands
import discord
import time
from datetime import date
import datetime

from time import sleep


class PiBell(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.x = 4
        self.button = Button(self.x, False, None)
        self.led = LED(14)
        self.led_working = RGBLED(16, 20, 21)
        self.bell_channel_id = 758425852001255486
        # self.buzzer = Buzzer(15)
        self.led_working.color = Color('green')
        print(self.button.pull_up)
        self.send_onready_message.start()
        self.reset_color_led.start()
        self.wait = 0
        self.fTime = open("SwanData.txt", "a")

    @tasks.loop(seconds=5)
    async def reset_color_led(self):
        self.led_working.color = Color('green')
        # channel = self.bot.get_channel(int(self.bell_channel_id))
        # with open('/media/pi/8bcf7aa7-4478-493c-a2e9-d0bb42a49e45/Images/saved_img-final.jpg', 'rb') as fp:
        #    await channel.send(file=discord.File(fp, 'new_filename.png'))

    @commands.command()
    async def command_color_led(self, ctx):
        print('command')
        self.led_working.color = Color('orange')

    @tasks.loop()
    async def send_onready_message(self):
        print(date.today())
        print(datetime.time())
        if date.today().weekday() == 4:
            if datetime.time() == datetime.time(18,40):
                channel = self.bot.get_channel(int(self.bell_channel_id))
                await channel.send("@everyone have the bins been done")

        if self.button.is_pressed and time.time() > self.wait + 30:
            self.fTime = open("SwanData.txt", "a")
            self.led_working.color = Color('blue')
            print("@everyone Someone is at the door!")
            channel = self.bot.get_channel(int(self.bell_channel_id))
            ringTime = str(round(time.time()))
            self.fTime.write("\n" + ringTime)
            self.fTime.close()
            await channel.send("@everyone Someone is at the door! - " + ringTime)
            # with open('/media/pi/8bcf7aa7-4478-493c-a2e9-d0bb42a49e45/Images/saved_img-final.jpg', 'rb') as fp:
            #    await channel.send(file=discord.File(fp, 'new_filename.png'))
            self.led.on()
            self.led.off()
            self.wait = time.time()

    @send_onready_message.before_loop  # wait for the client before starting the task
    async def before_send(self):
        await self.bot.wait_until_ready()

        return

    def exit_handler(self):
        self.led_working.off()


def setup(bot):
    bot.add_cog(PiBell(bot))
