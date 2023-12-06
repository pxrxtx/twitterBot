# This is designed to be run using crontab to automate the tweeting process (ex. tweeting the name of a random pokemon each day at noon)
# Here is what I have in my crontab file:
# 0 12 * * * cd /home/pxrxtx/twitterBot && /usr/bin/python /home/pxrxtx/twitterBot/tweeter.py

import tweepy
import json
import requests
import random

# twitter_auth.json holds the authentication keys (not in this repo for obvious reasons)
with open('twitter_auth.json') as file:
    secrets = json.load(file)

client = tweepy.Client(
    consumer_key=secrets['consumer_key'],
    consumer_secret=secrets['consumer_secret'],
    access_token=secrets['access_token'],
    access_token_secret=secrets['access_token_secret']
)

randomPokemonID=random.randint(1,1017)

r = requests.get('https://pokeapi.co/api/v2/pokemon/'+str(randomPokemonID))

# pokemon.json stores the information about the pokemon from the above request (not in this repo because it is a placeholder that changes each time tweeter.py is ran)
with open('pokemon.json', 'w') as file:
        file.write(r.text)

with open('pokemon.json') as file:
        pokemon = json.load(file)

pokemonOfTheDay = pokemon['name']

client.create_tweet(text=pokemonOfTheDay, user_auth=True)

# Helpful feedback for executing tweeter.py manually
print("Tweeted: " + pokemonOfTheDay)
