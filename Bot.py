# ---IMPORT LIBRAIRIES---

# For Discord
import discord 
from discord.utils import get
from discord.ext import commands

#For Web Scraping
import requests
from bs4 import BeautifulSoup

#---------------------------------------------------BOT-------------------------------------------------------------------------------

# Permet de paramétrer le bot
bot = commands.Bot(command_prefix='/yt', description="Bot pour YouTube")

# Savoir quand le bot est pret
@bot.event
async def pret(): # Défini une commande
    print("Bot YT pret !") # Affiche la valeur dans le terminal

# Créer la commande definition (exemple: /yt definition coder)
@bot.command()
async def definition(ctx, mot): # Défini une commande avec comme argument ctx et mot
    url = "https://www.le-dictionnaire.com/definition/{}".format(mot) 
    reponse = requests.get(url) # ermet de 'tester' le site
    if reponse.ok: # Si la response que l'url renvoi est fonctionnelle
        s = BeautifulSoup(response.text, 'html.parser')
        trouve = s.find('ul').get_text() # Cherche le texe à l'intérieur des balises 'ul'
        await ctx.send("``` {} ```".format(trouve)) # Renvoi sur le serveur le texte trouvé

#---------------------------------------------------RUN-----------------------------------------------------------------------------------

print("Lancement du bot")

bot.run("Token")
