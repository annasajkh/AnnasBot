from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot()


@bot.event
async def on_ready():
    print(f"logged as {bot.user}")