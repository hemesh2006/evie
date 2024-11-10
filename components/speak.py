import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()
def spk(text,rat=200,vol=0.9):
# Set the speaking rate
    newVoiceRate = 200  # Adjust this value to make the speech faster or slower
    engine.setProperty('rate', rat)

# Set other properties if desired
    engine.setProperty('volume',vol)  # Volume level (0.0 to 1.0)
# Convert text to speech
    engine.say(text)

# Run the speech engine
    engine.runAndWait()

# Ensure to install the library for the method you uncomment below:
# pip install simpleaudio pygame playsound




import pygame

def play_wav(file_path):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"An error occurred while trying to play the .wav file: {e}")
    finally:
        pygame.mixer.quit()
