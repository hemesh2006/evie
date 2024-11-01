import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Function to set the voice, rate, and volume
def speak(text, rate, volume):
    engine.setProperty('rate', rate)      # Speed of the speech
    engine.setProperty('volume', volume)  # Volume of the speech (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

