from utilities.utils import *
import traceback


@bot.slash_command(
  name="urbandict",
  description="define a word using urban dictionary API",
)
async def urbandict(
  interaction: nextcord.Interaction,
  word: str = nextcord.SlashOption(required=True,
                                   description="word or symbol to be define")):

  await interaction.response.defer()

  try:
    embed = construct_embed(title=word,
                            text=get_urbandict_definition(word),
                            color=nextcord.Color.orange())
  except Exception as e:
    if type(e) == Exception:
      embed = construct_embed(title="Exception",
                              text=str(e),
                              color=nextcord.Color.red())
    else:
      embed = construct_embed(title=f"Exception: {type(e)}",
                              text=traceback.format_exc(),
                              color=nextcord.Color.red())

  await interaction.followup.send(embed=embed)


@bot.slash_command(
  name="random_urbandict",
  description=
  "get random definition from urban dictionary using urban dictionary API",
)
async def random_urbandict(interaction: nextcord.Interaction):
  await interaction.response.defer()
  try:
    random_definitions = requests.get(
      "https://api.urbandictionary.com/v0/random").json()

    random_definition = random.choice(random_definitions["list"])

    definition_text = random_definition[
      "definition"] + f"\n\nby {random_definition['author']}"

    embed = construct_embed(title=random_definition["word"],
                            text=definition_text,
                            color=nextcord.Color.orange())
  except Exception as e:
    if type(e) == Exception:
      embed = construct_embed(title="Exception",
                              text=str(e),
                              color=nextcord.Color.red())
    else:
      embed = construct_embed(title=f"Exception: {type(e)}",
                              text=traceback.format_exc(),
                              color=nextcord.Color.red())

  await interaction.followup.send(embed=embed)


@bot.slash_command(
  name="meme",
  description="get random meme from reddit",
)
async def meme(interaction: nextcord.Interaction):
  await interaction.response.defer()

  try:
    random_meme = requests.get("https://meme-api.com/gimme").json()

    embed = construct_embed(
      title=random_meme["title"] if "title" in random_meme else "",
      color=nextcord.Color.blue(),
      text="by " + random_meme["author"] if "author" in random_meme else "")
    embed.set_image(random_meme["url"] if "url" in random_meme else "")

  except Exception as e:
    if type(e) == Exception:
      embed = construct_embed(title="Exception",
                              text=str(e),
                              color=nextcord.Color.red())
    else:
      embed = construct_embed(title=f"Exception: {type(e)}",
                              text=traceback.format_exc(),
                              color=nextcord.Color.red())

  await interaction.followup.send(embed=embed)


@bot.slash_command(
  name="niko",
  description="niko!",
)
async def niko(interaction: nextcord.Interaction):
  await interaction.response.defer()

  try:
    embed = construct_embed(color=nextcord.Color.yellow())
    embed.set_image(
      url=
      "https://media1.tenor.com/images/0e1c03b54935e214924ab40a8f945372/tenor.gif?itemid=17938358"
    )

  except Exception as e:
    if type(e) == Exception:
      embed = construct_embed(title="Exception",
                              text=str(e),
                              color=nextcord.Color.red())
    else:
      embed = construct_embed(title=f"Exception: {type(e)}",
                              text=traceback.format_exc(),
                              color=nextcord.Color.red())

  await interaction.followup.send(embed=embed)


@bot.slash_command(
  name="random_quote",
  description="get random quote using zenquotes API",
)
async def random_quote(interaction: nextcord.Interaction):
  await interaction.response.defer()

  try:
    embed = construct_embed(text=get_random_quote(),
                            color=nextcord.Color.green())
  except Exception as e:
    if type(e) == Exception:
      embed = construct_embed(title="Exception",
                              text=str(e),
                              color=nextcord.Color.red())
    else:
      embed = construct_embed(title=f"Exception: {type(e)}",
                              text=traceback.format_exc(),
                              color=nextcord.Color.red())

  await interaction.followup.send(embed=embed)


@bot.slash_command(
  name="number_fact",
  description="get some fact about numbers using Numbers API",
)
async def number_fact(interaction: nextcord.Interaction,
                      number: int = nextcord.SlashOption(
                        required=True, description="the number")):

  await interaction.response.defer()

  try:
    embed = construct_embed(
      text=requests.get(f"http://numbersapi.com/{number}").text,
      color=nextcord.Color.blue())
  except Exception as e:
    if type(e) == Exception:
      embed = construct_embed(title="Exception",
                              text=str(e),
                              color=nextcord.Color.red())
    else:
      embed = construct_embed(title=f"Exception: {type(e)}",
                              text=traceback.format_exc(),
                              color=nextcord.Color.red())

  await interaction.followup.send(embed=embed)
