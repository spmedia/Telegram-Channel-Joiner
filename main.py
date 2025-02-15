#!/usr/bin/env python3

import time
import random
import re
from pyrogram import Client

# Replace these with your own values
api_id = '21923436'
api_hash = '4ad0520f6557039b30a87609ebaf295b'
phone_number = '0468046629'

# Input list of Telegram channels here
channels = [
    "https://t.me/cribfreebot?start=7465422440",
    # Add more channels as needed. These are just some examples bruv.
]

# Function to extract the username/channel name from the URL
def extract_username(url):
    match = re.search(r't\.me\/([a-zA-Z0-9_]+)', url)
    if match:
        return match.group(1)
    return None

# Create a Pyrogram Client
app = Client("my_account", api_id=api_id, api_hash=api_hash, phone_number=phone_number)

async def join_channels():
    async with app:
        for channel_url in channels:
            username = extract_username(channel_url)
            #username = channel_url
            if username:
                try:
                    await app.join_chat(username)
                    print(f"Successfully joined {channel_url}")
                except Exception as e:
                    print(f"Failed to join {channel_url}: {e}")
                delay = random.randint(300, 600) # I made a random delay in between joining channels/groups of 300 to 600 sec
                time.sleep(delay)
            else:
                print(f"Invalid URL format: {channel_url}")

if __name__ == "__main__":
    app.run(join_channels())
