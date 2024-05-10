# main.py
import asyncio
import discord
from discord.ext import commands
import json # Importiert das json-Modul

#Lade die Konfiguration aus der config.json-Datei
with open('config.json', 'r') as f:
    config = json.load(f)

# Erhalte den Token aus der geladenen Konfiguration
TOKEN = config.get('token')

intents = discord.Intents.default()
intents.messages = True  # Nachrichtenintents aktivieren
intents.guilds = True  # Guild-Intents aktivieren

bot = commands.Bot(command_prefix='!', intents=intents)

# Laden der Cogs/Module
initial_extensions = ['message_handler']

async def load_extensions():
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
            print(f"Extension '{extension}' loaded successfully.")
        except Exception as e:
            print(f"Failed to load extension '{extension}': {e}")

async def start_bot():
    await load_extensions()
    await bot.start(TOKEN)  # Token des Bots hier einfügen

if __name__ == "__main__":
    asyncio.run(start_bot())
