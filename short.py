#!/usr/bin/env python3

# imports
import asyncio
# pip install google-genai
from google import genai

# create an array to hold message history
history = 6
memory = []

# generate a response from google api
async def generate(prompt):

    client = genai.Client(api_key="AIzaSyBOjBGtGaFJurlpcEe4MwVqhAL5MZbG5wE")

    response = await client.aio.models.generate_content(
        model="gemma-3-27b-it",
        contents=prompt,
    )
    
    return response.text

# run the program
if __name__ == "__main__":
    
    try:

        while prompt := input(">>> "):
            
            response = asyncio.run(
                generate(
                    f"<CONVERSATION HISTORY>:\n{"\n".join(memory)}\n<NEW MESSAGE>:\n{prompt}"
                )
            )
            
            memory.append(prompt)
            memory.append(response)

            memory = memory[-history:]
            print(response)

    except Exception as error:
        print(f"An error occured: {error}")