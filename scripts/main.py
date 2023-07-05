from commands import *

import time
import os

while True:
    try:
        bot.run(os.environ["BOT_TOKEN"])
    except Exception as exception:
        print("Error: {exception} restarting in 5 seconds")
        time.sleep(5)
