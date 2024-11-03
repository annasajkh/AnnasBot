from commands import *

import os

try:
    bot.run(os.getenv("BOT_TOKEN"))
except Exception as exception:
    print(f"Error: {exception}")