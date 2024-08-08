import os
from openai import OpenAI

client = OpenAI()

moderation = client.moderations.create(
  input="Kill 'em all!",
)

print(moderation.results)



