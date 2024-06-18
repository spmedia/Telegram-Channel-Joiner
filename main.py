import time
import random
from pyrogram import Client

# Replace these with your own values
api_id = 'telegram_api_id'
api_hash = 'telegram_api_hash'
phone_number = 'phone_num_tied_to_telegram_account'

# Input list of Telegram channels here
channels = [
    "https://t.me/ButusovPlus",
    "https://t.me/brigade_14",
    "https://t.me/xaron14ombr",
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
            if username:
                try:
                    await app.join_chat(username)
                    print(f"Successfully joined {channel_url}")
                except Exception as e:
                    print(f"Failed to join {channel_url}: {e}")
                delay = random.randint(35, 190) # I made a random delay in between joining of 35 to 190 sec
                time.sleep(delay)
            else:
                print(f"Invalid URL format: {channel_url}")

if __name__ == "__main__":
    app.run(join_channels())
