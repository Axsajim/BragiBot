import discord
import os
import requests
import json
from faker import Faker
import random
from random import randint
import translators as ts
from keep_alive import keep_alive


client = discord.Client()


def Metmuseum():
  departmentId = randint(1, 15)
  url = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/search?hasImages=true&medium=Paintings&departmentId={}&q=Painting'.format(departmentId))
  json_data = json.loads(url.text)
  picked = json_data["objectIDs"]
  value = random.choice(picked)
  url2 = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/{}'.format(value))
  json_data2 = json.loads(url2.text)
  picked2 = json_data2["primaryImage"]
  artwork = (picked2)
  print('{}\n{}\n{}\n{}'.format(url, value, url2, artwork))
  return(artwork)

def fake_info():
  fake = Faker('en_US')
  for _ in range(10):
      life = randint(0, 100)
      name = fake.name()
      luck = float(random.randrange(155, 389))/100

      my_dict = "**Name:** {} \n**Life:** {} \n**Luck:** {}".format(name, life, luck)
  return(my_dict)
  

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/artwork'):
        artwork = Metmuseum()
        await message.channel.send(artwork)
        print(artwork)

    if message.content.startswith('/fake'):
      my_dict = fake_info()
      await message.channel.send(my_dict)
    
    if message.content.startswith('/poem'):
      for _ in range(1):
        fake1 = Faker('en_US')
        fake2 = fake1.text()
        fake1 = '{}'.format(fake2)
        replica = '{}'.format(fake2)
        norwegian = ts.google(replica, 'en', 'no')
        msg = '**Drømmeaktig Edda**\n{}\n\n**Oneiric Edda**\n{}'.format(norwegian, fake1)
        print(norwegian, '\n\n', fake1)
        
      await message.channel.send(msg)

      
keep_alive()

client.run(os.getenv('TOKEN'))
