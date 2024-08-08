import numpy as np
from openai import OpenAI

client = OpenAI()

prompt = input("Enter a string to create an embedding vector for: ")
response = client.embeddings.create(
	input = prompt,
	model = "text-embedding-ada-002")

print("\n")	
print(response)

print("\nLet's find the similarity score between 'potato' and 'rhubarb'.")

response = client.embeddings.create(
	input=["potato", "rhubarb"],
	model="text-embedding-ada-002")
	
potato = response.data[0].embedding
rhubarb = response.data[1].embedding

simScore = np.dot(potato, rhubarb)

print("\nScore is " + str(simScore) + "\n")

print("How about 'potato' and 'The starship Enterprise'")

response = client.embeddings.create(
	input=["potato", "The starship Enterprise"],
	model="text-embedding-ada-002")
	
potato = response.data[0].embedding
enterprise = response.data[1].embedding

simScore = np.dot(potato, enterprise)

print("\nScore is " + str(simScore) + "\n")

