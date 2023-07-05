from oneshot_dialog_generator.setup import *
import re

def build_frame(face_name: str | None = None, text: str = "") -> np.ndarray:
    image: Image.Image = paste_face(textbox_background, faces[face_name], (496, 17))

    draw: ImageDraw = ImageDraw.Draw(image)
    draw.multiline_text((20, 14 + (image.size[1] // 2 - textbox_background.size[1] // 2)), text, font=font)
    
    return array(image)


def generate_images_and_audio_clips(textboxdata_list: list[TextBoxData]) -> tuple[list[np.ndarray], list[AudioFileClip]]:
    images: list[np.ndarray] = []
    audio_clips: list[AudioFileClip] = []

    # if the face is not loaded yet then load it but if it's already loaded then don't load it again
    for textboxdata in textboxdata_list:
        try:
            if not textboxdata.face_name in faces.keys():
                faces[textboxdata.face_name] = Image.open(f"assets/oneshot_dialog_generator/faces/{textboxdata.face_name}.png")
        except:
            raise Exception(f"\Face name \"{textboxdata.face_name}\" is not found. Please use command /oneshot_faces to see all of the available faces")
    
    for textboxdata in textboxdata_list:
        # add a little more frames to match the sound
        if len(textboxdata.text) == 1:
            textboxdata.text += "  "
        elif len(textboxdata.text) == 2:
            textboxdata.text += " "
        elif len(textboxdata.text) % 3 == 1:
            textboxdata.text += "  "
        elif len(textboxdata.text) % 3 == 2:
            textboxdata.text += " "


        # add the talking sound corresponding to the type is it a robot or not 
        for _ in range(len(textboxdata.text) // 3):
            if textboxdata.face_name in robot_names:
                audio_clips.append(robot_dialog)
            else:
                audio_clips.append(normal_dialog)
        

        # add frames per character in the text
        text_temp = ""
        for char in textboxdata.text:
            images.append(build_frame(face_name=textboxdata.face_name, text=text_temp))
            text_temp += char
        
        
        # add delay audio
        for _ in range(0, 10):
            audio_clips.append(silent)
        

        # add delay frame
        for _ in range(0, 30):
            images.append(build_frame(face_name=textboxdata.face_name, text=text_temp))
    
    # unload all the images so it doesn't eat up memory
    for textboxdata in textboxdata_list:
        if textboxdata.face_name in faces.keys():
            del faces[textboxdata.face_name]
    

    return images, audio_clips


# paste the face to the textbox in the correct location 
def paste_face(background_image: Image.Image, 
               face_image: Image.Image, 
               box: tuple[int, int]) -> Image.Image:
    
    background_image: Image.Image = background_image.convert("RGBA")
    face_image: Image.Image = face_image.convert("RGBA")

    image: Image.Image = Image.new("RGBA", (background_image.size[0], int(background_image.size[1])))

    image.paste(background_image, (0, image.size[1] // 2 - textbox_background.size[1] // 2), mask=background_image)
    image.paste(face_image, (box[0], box[1] + (image.size[1] // 2 - textbox_background.size[1] // 2)), mask=face_image)

    return image