import os
import discord
from dotenv import load_dotenv 
from discord.ext import commands

def run_bot():
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    bot = commands.Bot(command_prefix="-", intents=discord.Intents.default())
    # logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

    @bot.event
    async def on_ready():

        # To make sure this bot is only active in a particular channel in a particular server
        for guild in bot.guilds:
            if (guild.name == '\U0001d610\'\U0001d62e \U0001d62a\U0001d62f'):
                for channel in guild.channels:
                    if channel.name == 'text_channel_mcgee':
                        await channel.send('tembstb') # channel.send('***GONG***')

        await bot.close()

    bot.run(TOKEN)