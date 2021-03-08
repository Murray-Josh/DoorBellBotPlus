# Main Author Choco02 https://gist.github.com/Choco02/e40acf5484c72bbf1915cb415b2044cf
import discord
from discord.ext import commands

import sys, traceback

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['>?', 'lol ', '!?', '!']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)



initial_extensions = ['members', 'washer', 'misc', 'loop']

bot = commands.Bot(command_prefix=get_prefix, description='A Rewrite Cog Example')

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
    try:
        bot.load_extension('pistuff')
    except:
        print("No Pi Detected")


@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    print(f'Successfully logged in and booted...!')


def exit_handler():
    print("Fin")
tokenFile = open('token.txt')
token = tokenFile.read()
#bot.bg_task = bot.loop.create_task(my_background_task())
bot.run(token, bot=True, reconnect=True)

#789159233861320727
