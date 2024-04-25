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
The bot listens private message using `!r <message>` in the server and converts them into speech.

> **_NOTE:_**  The script will create temp.mp3 and time.mp3 in order to stream it. you can enhance to delete files upon every stream.

#### Dependencies
discord
asyncio
ffmpeg (https://www.gyan.dev/ffmpeg/builds/)
gtts

#### To Install ffmpeg

- Download the FFmpeg build from the official website (https://ffmpeg.org/download.html).
- Extract the downloaded zip file.
- Add the bin folder from the extracted file to your system's PATH.

For the last step, you can follow these instructions:

- Press Win + X and choose System.
- Click on "Advanced system settings".
- In the System Properties window that opens, click on the "Environment Variables" button.
- In the Environment Variables window, under "System variables", find and select the "Path" variable, then click on "Edit".
- In the Edit Environment Variable window, click on "New", then "Browse".
- Navigate to the bin folder in the extracted FFmpeg folder, select it, and click on "OK" in all windows.

###### Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
