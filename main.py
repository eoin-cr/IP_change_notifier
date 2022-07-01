# main.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# The default prefix is !
bot = commands.Bot(command_prefix="!", intents=intents)

# loads the ip cog
bot.load_extension("cogs.ip")

bot.run(TOKEN)
