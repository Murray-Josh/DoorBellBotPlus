import gpiozero
from time import sleep
async def ringbell():
    x = 2
    button = Button(x)
    try:  
        while True:      
            if button.is_pressed:
                print("Button is pressed"
                await asyncio.sleep(1)
                await ctx.send("Bell has been rung")       