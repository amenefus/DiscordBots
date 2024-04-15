import discord
import asyncio
from discord import FFmpegPCMAudio
from discord.ext import commands
from gtts import gTTS
import requests
import os
from datetime import datetime, date


# Initialize the bot with intents
intents = discord.Intents.default()
intents.message_content = True  # Enable Privileged Message Content intent
intents.voice_states = True  # Add voice_states intent for voice channel operations
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def tts(ctx, *, message):
    # Save the message in a variable
    tts_message = message
    language = 'iw'
    tts = gTTS(text=message, lang=language, slow=False)
    tts.save('temp.mp3')

    channel_id = 1082952248860102666  # Replace with your voice channel ID
    file_path = 'temp.mp3'  # Replace with the actual path to your MP3 file
    channel = bot.get_channel(channel_id)
    if not channel:
        return print('Invalid voice channel ID.')
    voice_client = discord.utils.get(bot.voice_clients, guild=channel.guild)
    if voice_client is not None and voice_client.is_connected():
        await voice_client.move_to(channel)
    else:
        voice_client = await channel.connect()

    source = discord.FFmpegPCMAudio(file_path)
    if not voice_client.is_playing():
        voice_client.play(source, after=lambda e: print('done', e))
    else:
        print("The bot is already playing audio.")
        await ctx.send("תמתין קצת באמאשך. אני עובדת גם בשביל אחרים. תקווה שאני לא עובדת על דברים שלא קשורים לך. תודה על ההבנה.")
    # Wait for the sound to finish playing
    while voice_client.is_playing():
        await asyncio.sleep(1)
    
    # Disconnect after playing the sound
    while voice_client.is_playing():
        await asyncio.sleep(1)
    
    # Check if the bot is connected before disconnecting
    if voice_client.is_connected():
        await voice_client.disconnect()
        
# ====================== END TTS COMMAND ====================== #
# ====================== VOICE CHANNEL OPERATIONS ====================== #
@bot.command()
async def shoulder(ctx):
    start_date = date(2021, 5, 1)
    today = date.today()
    delta = today - start_date
    amassage = "{delta.days} ימים מאז הכתף הפסיקה לעבוד".format(delta=delta)
    language = 'iw'
    tts = gTTS(text=amassage, lang=language, slow=False)
    tts.save('temp.mp3')

    channel_id = 1082952248860102666  # Replace with your voice channel ID
    file_path = 'temp.mp3'  # Replace with the actual path to your MP3 file
    channel = bot.get_channel(channel_id)
    if not channel:
        return print('Invalid voice channel ID.')
    voice_client = await channel.connect()
    source = discord.FFmpegPCMAudio(file_path)
    voice_client.play(source, after=lambda e: print('done', e))
    # Wait for the sound to finish playing
    while voice_client.is_playing():
        await asyncio.sleep(1)
    
    # Disconnect after playing the sound
    while voice_client.is_playing():
        await asyncio.sleep(1)
    
    # Check if the bot is connected before disconnecting
    if voice_client.is_connected():
        await voice_client.disconnect()


# ====================== END VOICE CHANNEL OPERATIONS ====================== #
# ====================== BOT STREAM ====================== #


token = ""

@bot.event
async def on_ready():
  print(f"Logged in as {bot.user}")

bot.run(token)
