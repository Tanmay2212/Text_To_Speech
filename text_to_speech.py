from gtts import gTTS
import os

def text_to_speech(file_path, language="en", slow=False):
    """
    Convert text from a file to speech and save as an MP3 file.

    Args:
        file_path (str): Path to the text file.
        language (str, optional): Language of the text. Defaults to "en".
        slow (bool, optional): Whether to speak slowly. Defaults to False.
    """
    try:
        with open(file_path, "r") as f:
            input_text = f.read().replace("\n", " ")
        
        voice = gTTS(text=input_text, lang=language, slow=slow)
        voice.save("txt.mp3")
        
        # Playing the file
        os.system("start txt.mp3")
    except FileNotFoundError:
        print("File not found. Please check the file path.")

# Example usage:
text_to_speech("text.txt")
