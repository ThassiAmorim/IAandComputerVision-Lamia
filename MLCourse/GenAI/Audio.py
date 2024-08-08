import os
from openai import OpenAI

client = OpenAI()


audio_file = open("hi.mp3", "rb")
transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

print("Transcribing hi.mp3:\n")
print(transcript)

print("\nTranslating french.mp3:\n")

audio_file = open("french.mp3", "rb")
transcript = client.audio.translations.create(model="whisper-1", file=audio_file)

#Will it actually work?
print(transcript)