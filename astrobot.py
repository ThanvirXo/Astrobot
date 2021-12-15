import discord
from discord.ext import commands
import requests
from keepalive import keep_alive

client= discord.Client()

bot = commands.Bot(command_prefix='$')

def get_astro(sign,day):
    response =requests.post('https://aztro.sameerkumar.website?sign='+sign+'&day='+day+'')
    json=response.json()
    return (json)
    
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))  


@client.event
async def on_message(message):
    if message.author == client.user:
        return None

    if message.content.startswith('$sign'):
        sign=message.content.split()[1]
        day=message.content.split()[2]
        s=get_astro(sign,day)
        await message.channel.send(s)


keep_alive()
