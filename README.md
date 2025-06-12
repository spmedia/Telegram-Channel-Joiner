# Telegram-Channel-Joiner

<img src="https://raw.githubusercontent.com/spmedia/Telegram-Channel-Joiner/main/wizard3.jpg" style="width: 75%; height: 75%" />

# About 

A python bot 🤖 that uses the [Pyrogram API Framework](https://docs.pyrogram.org/) to take a list of Telegram channels and groups and joins them. I really made this to help people doing CTI and OSINT on Telegram to make growing your sock puppet accounts a lot easier.

A free Telegram account can be in 500 channels/groups max. A paid Telegram Premium account can be in 1000 channels/groups max.

You will first need to first log into https://my.telegram.org/ and grab your account api id and hash.

This bot takes a list of Telegram channels and groups like:

```
https://t.me/ButusovPlus
https://t.me/brigade_14
https://t.me/xaron14ombr
etc.
```
and joins your Telegram account to them.  (to join private channels, comment line 34 and uncomment line 35)


# Dependencies 
python3 -m pip install pyrogram tgcrypto

# Notes
I put a random delay in between joins of 300 seconds to 600 seconds just so you aint hitting rate limits and shit. If you try to join too many channels/groups at once it will timeout and make you wait. Slow and steady wins the race 🐢. This is made to just setup and leave it running overnight and you wake up to being in a ton of channels. You can change the rate limit if you want but you'll hit rate limits if you make it too fast. This is like an EZ Bake oven but for lazy CTI nerds like me who like Telegram.

# Greetz 

Happy hunting and hacking my fellow CTI wizards 🧙‍♂️ 🎯
