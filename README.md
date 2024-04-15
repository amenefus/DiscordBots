# Discord Text-to-Speech Bot


This repository contains the source code for a Discord bot that uses Google's Text-to-Speech (gTTS) service to convert text messages into speech.

#### Features:
- Converts text messages into speech using Google's Text-to-Speech (gTTS) service.
- Listens to all messages in the server due to the enabled Privileged Message Content intent.
- Can perform voice channel operations due to the enabled voice_states intent.


#### Setup
- Clone this repository to your local machine.
- Install the required dependencies by running `'pip install -r requirements.txt'`.
Set up a bot on the Discord developer portal, and get your bot token. (https://discord.com/developers/applications)
- Replace `'YOUR_BOT_TOKEN'` in discord_tts.py with your actual bot token.
- Run the bot by executing `'python discord_tts.py'`.

#### Usage
The bot listens private message using `!tts <message>` in the server and converts them into speech.

#### Dependencies
discord
asyncio
ffmpeg (https://www.gyan.dev/ffmpeg/builds/)
gtts



###### Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.