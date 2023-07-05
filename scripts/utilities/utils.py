from utilities.setup import *

import nextcord
import requests
import random

def construct_embed(
  title: str = None,
  text: str = None,
  image_url: str = None,
  color: nextcord.Color = nextcord.Color.blue()
) -> nextcord.Embed:
  embed: nextcord.Embed = nextcord.Embed(title=title if title else "")

  if image_url:
    embed.set_image(image_url)

  if text:
    embed.set_footer(text=text)

  embed.color = color

  return embed


def get_urbandict_definition(word: str) -> str:
  results = requests.get(
    f"http://api.urbandictionary.com/v0/define?term={word}").json()["list"]

  if len(results) == 0:
    raise Exception(
      f"sorry i can't find definition of \"{word}\" on urban dictionary")
  else:
    result = random.choice(results)

  return result["definition"] + f"\n\nby {result['author']}"

def get_random_quote():
    response = requests.get("https://zenquotes.io/api/random").json()
    return response[0]["q"] + "\n\n-" + response[0]["a"]