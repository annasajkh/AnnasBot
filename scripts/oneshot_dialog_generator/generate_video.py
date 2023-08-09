import gc
import re
import textwrap

from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from PIL import ImageFont
from moviepy.editor import *

import oneshot_dialog_generator.constructs as constructs
from oneshot_dialog_generator.constructs import TextBoxData


def generate_oneshot_dialog_video(dialog_text: str):
    # if there is arial tag then use arial font else use oneshot font
    if "#arial" in dialog_text:
        constructs.font = ImageFont.truetype("assets/oneshot_dialog_generator/fonts/arial.ttf", 20)
        dialog_text = dialog_text.replace("#arial", "")
    else:
        constructs.font = ImageFont.truetype("assets/oneshot_dialog_generator/fonts/terminus.ttf", 20)
    
    textboxdata_list: list[TextBoxData] = []

    dialog_text = dialog_text.strip()
    
    # find all match of dialog face name -> niko: , niko_sad:, etc and store it on data_faces
    data_faces = re.findall(".*?:",dialog_text)

    # split the dialog data content -> niko:       -> ["\n","hello","oh"]
    #                                  hello
    #                                  niko_sad:
    #                                  oh
    data_dialogs = re.split(".*?:",dialog_text)

    # get rid of that first index
    # ["hello","oh"]
    data_dialogs.pop(0)

    if len(data_dialogs) > 20:
        raise Exception("Too many dialogs! max 20")

    if len(data_faces) != len(data_dialogs):
        raise Exception("data_faces and data_dialogs is not the same length")

    for i in range(0,len(data_dialogs)):
        # replace all whitespaces char with space and split it by space
        data_dialog_arr = re.sub("\s+", " ", data_dialogs[i]).split(" ")
        data_dialog_arr_temp = []

        # if there is a word that has a length greather than 47 then split it and add it to temp array
        for index in range(0,len(data_dialog_arr)):
            if len(data_dialog_arr[index]) > 47:
                for chunk in textwrap.wrap(data_dialog_arr[index], 47):
                    data_dialog_arr_temp.append(chunk)
            else:
                data_dialog_arr_temp.append(data_dialog_arr[index])
        
        # set the final array to the temp array
        data_dialog_arr = data_dialog_arr_temp

        data_dialog_str = ""
        temp_data_dialog = ""

        for word in data_dialog_arr:
            # auto wrap stuff
            if len(temp_data_dialog + word) > 47:
                data_dialog_str += '\n'
                temp_data_dialog = ""
            
            temp_data_dialog += word + " "
            data_dialog_str += word + " "
        
        # maximum text per dialog
        if len(data_dialog_str.rstrip()) > 188:
            raise Exception("dialog is too long! maximum text length for each dialog is 188")

        # just in case strip the string "annas    " -> "annas"
        data_dialogs[i] = data_dialog_str.rstrip()
    
    # build the text data replace the : with nothing and also strip it just in case
    for i in range(0,len(data_faces)):
        textboxdata_list.append(TextBoxData(data_faces[i].replace(":","").strip(),data_dialogs[i].strip()))

    
    # filter text through 2 filters
    # if profanity.contains_profanity(text_combine):
    #     raise Exception("bot detect that there is bad word in your text please delete it")
    # elif predict([text_combine])[0] == 1:
    #     raise Exception("ai detect that there is bad word in your text please delete it")


    # constructs the video
    images, audioclips = constructs.generate_images_and_audio_clips(textboxdata_list)

    textboxdata_list = None
    gc.collect()
    
    try:
        audio = concatenate_audioclips(audioclips)
    except:
        raise Exception("""Wrong format! you have to format it like this
niko:
hello everyone
niko_speak:
i'm a cat
cedric:
wha-""")
    clip: ImageSequenceClip = ImageSequenceClip(images, 30)

    images = None
    audioclips = None
    gc.collect()

    clip.audio = audio
    audio = None
    gc.collect()
    
    # write it to a file
    clip.write_videofile("assets/generated_results/oneshot_dialog_result.mp4")
    
    clip = None
    gc.collect()