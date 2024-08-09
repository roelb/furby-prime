"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="Wie vandaag in de auto stapte om op vakantie te gaan, had een grote kans om in de file terecht te komen. Het was tot nu toe de drukste dag op de Europese wegen deze zomer, meldt de ANWB.")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
            language_code="nl-NL", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL, name="nl-NL-Standard-C"
            )

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3, pitch=13, speaking_rate=0.44
            )

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
            )

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

from pygame import mixer
mixer.init()
mixer.music.load('output.mp3')
mixer.music.play()
import time
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)
