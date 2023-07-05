from nextcord.ext import commands

bot = commands.Bot()


@bot.event
async def on_ready():
  print(f"logged as {bot.user}")