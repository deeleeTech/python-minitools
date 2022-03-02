from dis import disco
from urllib import response
import discord
import random
import apiFunctions

TOKEN = '' #from discord

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username} : {user_message} ({channel})')

    if message.author == client.user:
        return
    if message.channel.name == 'bots-house':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Goodbye {username}....')
        elif user_message.lower() == '!ye says':
            myResponse = apiFunctions.kanye_quotes()
            await message.channel.send(f'"{myResponse}..."')
    
client.run(TOKEN)