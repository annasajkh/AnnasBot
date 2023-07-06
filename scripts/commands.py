from utilities.utils import *
from utilities.modals import OneshotDialogGeneratorModal


@bot.slash_command(
  name = "urbandict",
  description = "define a word using urban dictionary API",
)
async def urbandict(
  interaction: nextcord.Interaction,
  word: str = nextcord.SlashOption(required = True,
                                   description = "word or symbol to be define")
):
  await interaction.response.defer()

  try:
    embed = construct_embed(title=word,
                            text=get_urbandict_definition(word),
                            color=nextcord.Color.orange())
    
  except Exception as exception:
    embed = construct_exception_embed(exception)

  await interaction.followup.send(embed=embed)



@bot.slash_command(
  name = "random_urbandict",
  description = "get random definition from urban dictionary using urban dictionary API"
)
async def random_urbandict(interaction: nextcord.Interaction):
  await interaction.response.defer()

  try:
    random_definitions = requests.get("https://api.urbandictionary.com/v0/random").json()

    random_definition = random.choice(random_definitions["list"])

    definition_text = random_definition["definition"] + f"\n\nby {random_definition['author']}"

    embed = construct_embed(title=random_definition["word"],
                            text=definition_text,
                            color=nextcord.Color.orange())
    
  except Exception as exception:
    embed = construct_exception_embed(exception)

  await interaction.followup.send(embed=embed)



@bot.slash_command(
  name = "meme",
  description = "get random meme from reddit",
)
async def meme(interaction: nextcord.Interaction,
               subreddit: str = nextcord.SlashOption(required = False,
                                                     description = "subreddit to get the meme from")):
  await interaction.response.defer()

  try:
    random_meme = requests.get(f"https://meme-api.com/gimme/{subreddit}").json()

    embed = construct_embed(title=random_meme["title"] if "title" in random_meme else "",
                            color=nextcord.Color.blue(),
                            text=f"by {random_meme['author']} " if "author" in random_meme else "")
    
    embed.url = random_meme["postLink"]

    embed.set_image(random_meme["url"] if "url" in random_meme else "")

  except Exception as exception:
    embed = construct_exception_embed(exception)

  await interaction.followup.send(embed=embed)



@bot.slash_command(
  name = "niko",
  description = "niko!",
)
async def niko(interaction: nextcord.Interaction):
  await interaction.response.defer()

  try:
    embed = construct_embed(color=nextcord.Color.yellow())
    embed.set_image(url="https://media1.tenor.com/images/0e1c03b54935e214924ab40a8f945372/tenor.gif?itemid=17938358")

  except Exception as exception:
    embed = construct_exception_embed(exception)

  await interaction.followup.send(embed=embed)



@bot.slash_command(
  name = "random_quote",
  description = "get random quote using zenquotes API",
)
async def random_quote(interaction: nextcord.Interaction):
  await interaction.response.defer()

  try:
    embed = construct_embed(text=get_random_quote(),
                            color=nextcord.Color.green())
    
  except Exception as exception:
    embed = construct_exception_embed(exception)

  await interaction.followup.send(embed=embed)



@bot.slash_command(
  name = "number_fact",
  description = "get some fact about numbers using Numbers API",
)
async def number_fact(interaction: nextcord.Interaction,
                      number: int = nextcord.SlashOption(required = True, 
                                                         description = "the number")):

  await interaction.response.defer()

  try:
    embed = construct_embed(text=requests.get(f"http://numbersapi.com/{number}").text,
                            color=nextcord.Color.blue())
    
  except Exception as exception:
    embed = construct_exception_embed(exception)

  await interaction.followup.send(embed=embed)



@bot.slash_command(
  name = "oneshot_dialog_generator",
  description = "oneshot dialog generator",
)
async def oneshot_dialog_generator(
  interaction: nextcord.Interaction
):
  try:
    oneshot_dialog_generator_modal = OneshotDialogGeneratorModal()
    await interaction.response.send_modal(oneshot_dialog_generator_modal)

  except Exception as exception:
    embed = construct_exception_embed(exception)

    await interaction.send(embed=embed)
    return



@bot.slash_command(
  name = "oneshot_faces",
  description = "see all available faces for /oneshot_dialog_gen",
)
async def oneshot_faces(
  interaction: nextcord.Interaction
):
  await interaction.response.defer()

  try:
    await interaction.followup.send(file=nextcord.file.File("assets/oneshot_dialog_generator/all_faces.png"))
  
  except Exception as exception:
    embed = construct_exception_embed(exception)

    await interaction.followup.send(embed=embed)