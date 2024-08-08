import os
import urllib.request
from openai import OpenAI

client = OpenAI()


newImage = client.images.generate(
  prompt="A UFO abducting a chicken",
  n=2,
  size="1024x1024"
)

print("Here are two generated images of a UFO abducting a chicken:\n")

print(newImage.data[0].url)

print("\n")

print(newImage.data[1].url)

# Download the first one
urllib.request.urlretrieve(newImage.data[0].url, "chicken.png")

# Ask for a variation
newImage = client.images.create_variation(
    image = open("chicken.png", "rb"),
    n=1,
    size="1024x1024"
)

print("\nHere's a variation of the first image:\n")
print(newImage.data[0].url)
