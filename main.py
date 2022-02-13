import discord
import os
import random


with open("My Clippings.txt", "r+") as digest:
       digest_content = digest.read()
       digest_list = digest_content.split('==========')
       digest_count = len(digest_list)
       random_num = random.randint(0, digest_count) 
       one_message = (digest_list[random_num])

kindle = digest_content

client = discord.Client()

@client.event
async def on_ready():
  print("{0.user} has logged in".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("$kindle"):
    await message.channel.send(one_message)

client.run(os.getenv('TOKEN'))