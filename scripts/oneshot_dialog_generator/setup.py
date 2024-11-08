
from PIL import Image
from moviepy.audio.fx.volumex import volumex
from moviepy.editor import *
from PIL import ImageFont

class TextBoxData:
    def __init__(self, face_name: str | None = None, text: str = ""):
        self.face_name: str | None = face_name
        self.text: str = text

# character that should have robot sound
robot_names: list[str] = ["en", "bookbot", "kelvin", "prophet", "proto", "gatekeeper", "rowbot", "silver","bot"]

faces: dict[str, Image.Image] = {}
font: ImageFont.FreeTypeFont | None = None

# load resources
textbox_background: Image.Image = Image.open("assets/oneshot_dialog_generator/textbox_background.png")
normal_dialog: AudioFileClip = AudioFileClip("assets/oneshot_dialog_generator/sounds/normal_dialog.wav").fx(volumex, 0.2)
robot_dialog: AudioFileClip = AudioFileClip("assets/oneshot_dialog_generator/sounds/robot_dialog.wav").fx(volumex, 0.2)
silent: AudioFileClip = robot_dialog.fx(volumex, 0)