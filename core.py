import os
import discord
from dotenv import load_dotenv 
from discord.ext import commands
import time

def run_bot():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    bot = commands.Bot(command_prefix="-", intents=discord.Intents.default())
    # logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

    @bot.event
    async def on_ready():
        t = time.localtime()
        t = time.strftime("%H:%M:%S", t)
        hr = int(t[:2])
        if(hr == 0):
            hr = 12
        if (hr > 12):
            hr = hr - 12

        # To make sure this bot is only active in a particular channel in a particular server
        for guild in bot.guilds:
            if (guild.name == '\U0001d610\'\U0001d62e \U0001d62a\U0001d62f'):
                for channel in guild.channels:
                    if channel.name == 'text_channel_mcgee':

                        # once it's verified that it is sending in the correct channel,
                        # determines how many gongs to send
                        gongs = ""

                        for x in range(hr):
                            gongs += "***GONG*** "

                        gongs = gongs[:len(gongs) - 1] # remove final space
                        
                        print(gongs)
                        await channel.send(gongs)

        await bot.close()

    bot.run(TOKEN)