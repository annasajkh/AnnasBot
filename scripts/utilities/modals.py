import nextcord
import os

from oneshot_dialog_generator.generate_video import generate_oneshot_dialog_video
from utilities.utils import construct_exception_embed

class OneshotDialogGeneratorModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Annas Bot"
        )
    
        self.dialog_text = nextcord.ui.TextInput(
            label="Dialog Text",
            max_length=1024,
            placeholder="Write your dialog text here...",
            style=nextcord.TextInputStyle.paragraph,
        )

        self.add_item(self.dialog_text)
    
    async def callback(self, interaction: nextcord.Interaction) -> None:
        await interaction.response.defer()
        
        wait_message = await interaction.followup.send("Processing your request, please wait...")

        try:
            generate_oneshot_dialog_video(self.dialog_text.value)
            await interaction.followup.send(file=nextcord.file.File("assets/generated_results/oneshot_dialog_result.mp4"))

        except Exception as exception:
            embed = construct_exception_embed(exception)

            await interaction.followup.send(embed=embed)
        
        await wait_message.delete()