from commands import *

import time
import os

try:
    bot.run(os.getenv("BOT_TOKEN"))
except Exception as exception:
    print("Error: {exception}")
