
import os
import discord
import requests 

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  if message.author == client.user:
    return
  if message.content.startswith('ascend me pls'):
    await message.channel.send('no')
    
client.run('MTAwMjkyNTYzMjEzODc4ODg3NA.GW8pM1.kqOHDdhXCQ2kelj-YeTBj5Ilz2Vax67fMQrvQY')