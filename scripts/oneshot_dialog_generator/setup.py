import glob

from PIL import Image, ImageDraw
from moviepy.audio.fx.volumex import volumex
from moviepy.editor import *
from numpy import array
from PIL import ImageFont
import numpy as np

class TextBoxData:
    def __init__(self, face_name: str | None = None, text: str = ""):
        self.face_name: str | None = face_name
        self.text: str = text

# character that should have robot sound
robot_names: list[str] = ["en", "bookbot", "kelvin", "prophet", "proto", "gatekeeper", "rowbot", "silver","bot"]

faces: dict[str, Image.Image] | None = {}
font: ImageFont.FreeTypeFont | None = None

# load the sounds and set the volume
textbox_background: Image.Image = Image.open("assets/oneshot_dialog_generator/textbox_background.png")

normal_dialog: AudioFileClip = AudioFileClip("assets/oneshot_dialog_generator/sounds/normal_dialog.wav").fx(volumex, 0.2)

robot_dialog: AudioFileClip = AudioFileClip("assets/oneshot_dialog_generator/sounds/robot_dialog.wav").fx(volumex, 0.2)

silent: AudioFileClip = robot_dialog.fx(volumex, 0)

# get all face name
for path in glob.glob("assets\\oneshot_dialog_generator\\faces\\*.png"):
    faces[path.split("\\")[1].split(".")[0]] = None