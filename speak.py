import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Function to set the voice, rate, and volume
def speak_with_tone(text, rate, volume):
    engine.setProperty('rate', rate)      # Speed of the speech
    engine.setProperty('volume', volume)  # Volume of the speech (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

# Examples with different tones
tones = [
    {"text": "Hello, I'm speaking with a normal tone.", "rate": 150, "volume": 1.0},
    {"text": "Now I'm speaking very quickly!", "rate": 250, "volume": 1.0},
    {"text": "I can also speak slowly and calmly.", "rate": 100, "volume": 0.9},
    {"text": "I'm speaking softly, almost like a whisper.", "rate": 150, "volume": 0.5},
    {"text": "This is my loud and clear tone.", "rate": 180, "volume": 1.0},
]

# Loop through each tone and make it speak
for tone in tones:
    speak_with_tone(tone["text"], tone["rate"], tone["volume"])
