import os
from openai import OpenAI

client = OpenAI()

prefix = input("Enter some text to complete: ")

completion = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=prefix,
  max_tokens=100,
  temperature=0
)

print("\n" + completion.choices[0].text)
