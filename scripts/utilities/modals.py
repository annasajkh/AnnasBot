import nextcord

from oneshot_dialog_generator.generate_video import generate_oneshot_dialog_video
from utilities.utils import construct_exception_embed

class OneshotDialogGeneratorModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Annas Bot"
        )
    
        self.dialog_text = nextcord.ui.TextInput(
            label="Dialog Text",
            min_length=2,
            max_length=2048,
            placeholder="Write your dialog text here...",
            style=nextcord.TextInputStyle.paragraph,
        )

        self.add_item(self.dialog_text)
    
    async def callback(self, interaction: nextcord.Interaction) -> None:
        self.dialog_text.value

        try:
            generate_oneshot_dialog_video(self.dialog_text.value)
            await interaction.send(file=nextcord.file.File("assets/generated_results/oneshot_dialog_result.mp4"))

        except Exception as exception:
            embed = construct_exception_embed(exception)

            await interaction.send(embed=embed)