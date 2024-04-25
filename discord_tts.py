import discord
import asyncio
from discord import FFmpegPCMAudio
from discord.ext import commands
from gtts import gTTS
import requests
import os
from datetime import datetime, date
import pytz

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
@bot.event
async def on_voice_state_update(member, before, after):
    specific_member_id = 344131780586110976  # Replace with the ID of the specific member
    member_to_move_id = 804570109498359878  # Replace with the ID of the member to move
    channel_to_move_to_id = 1083441236112834690  # Replace with the ID of the channel to move to

    # If the member who triggered the event is the member to move, do nothing
    if member.id == member_to_move_id:
        return

    if member.id == specific_member_id and after.channel is not None:
        member_to_move = member.guild.get_member(member_to_move_id)
        if member_to_move is not None and member_to_move.voice is not None and member_to_move.voice.channel is not None:
            channel_to_move_to = bot.get_channel(channel_to_move_to_id)
            if channel_to_move_to is not None:
                await member_to_move.move_to(channel_to_move_to)
                await member_to_move.send('Moved to AFK channel due to Member {specific_member_id} joining a voice channel.'.format(specific_member_id=specific_member_id))

# ====================== Time Teller ====================== #

@bot.command()
async def timeil(ctx):
    tz = pytz.timezone('Israel')
    current_time = datetime.now(tz)
    amassage = f"השעה עכשיו היא  {current_time.strftime('%I:%M')} בחור תחת הזה"
    language = 'iw'
    tts = gTTS(text=amassage, lang=language, slow=False)
    tts.save('time.mp3')

    channel_id = 1082952248860102666  # Replace with your voice channel ID
    file_path = 'time.mp3'  # Replace with the actual path to your MP3 file
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

@bot.command()
async def timetx(ctx):
    tz = pytz.timezone('America/Chicago')
    current_time = datetime.now(tz)
    amassage = f"השעה עכשיו היא {current_time.strftime('%H:%M')} אצל שימי."
    language = 'iw'
    tts = gTTS(text=amassage, lang=language, slow=False)
    tts.save('time.mp3')

    channel_id = 1082952248860102666  # Replace with your voice channel ID
    file_path = 'time.mp3'  # Replace with the actual path to your MP3 file
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


# ====================== BOT STREAM ====================== #


token = ""

@bot.event
async def on_ready():
  print(f"Logged in as {bot.user}")

bot.run(token)
