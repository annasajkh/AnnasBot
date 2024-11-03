import nextcord

from scripts.oneshot_dialog_generator.generate_video import generate_oneshot_dialog_video
from scripts.utilities.utils import construct_exception_embed

class OneshotDialogGeneratorModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Annas Bot"
        )
    
        self.dialog_text = nextcord.ui.TextInput(
            label="Dialog Text",
            max_length=1024,
            placeholder="""
niko:
hello everyone
niko_speak:
i'm a cat
cedric:
wha-
            """.strip(),
            style=nextcord.TextInputStyle.paragraph,
        )

        self.add_item(self.dialog_text)
    
    async def callback(self, interaction: nextcord.Interaction) -> None:
        response_message: nextcord.PartialInteractionMessage = await interaction.response.send_message("Processing your request, please wait...")

        try:
            generate_oneshot_dialog_video(self.dialog_text.value)

            await response_message.edit(content=None, file=nextcord.File("assets/generated_results/oneshot_dialog_result.mp4"))

        except Exception as exception:
            embed = construct_exception_embed(exception)

            await response_message.edit(content=None, embed=embed)