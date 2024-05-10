import discord
from discord.ext import commands

# Importiere die Variable greetings aus der greetings_config.py Datei
from greetings_config import greetings

class MessageHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Begrüßungstext für neues Mitglied
        welcome_message = greetings.get("new_member", "Willkommen {member}! Schön, dass du hier bist.")
        # Ersetze {member} im Begrüßungstext mit dem Namen des Mitglieds
        welcome_message = welcome_message.format(member=member.mention)
        # Sende die Begrüßungsnachricht im entsprechenden Kanal
        channel = member.guild.system_channel  # Hier den gewünschten Kanal anpassen
        await channel.send(welcome_message)

        # Füge das Daumen Hoch-Emote als Reaktion hinzu
        thumbs_up = "👍"
        await member.add_reaction(thumbs_up)  # Nur Daumen Hoch als Reaktion zulassen

    # Event, das beim Empfang einer Reaktion aufgerufen wird
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        # Überprüfe, ob die Reaktion auf die Begrüßungsnachricht war und das Daumen Hoch-Emote ist
        if reaction.message.content == greetings.get("new_member", "default_message") and str(reaction.emoji) == "👍":
            # Sende eine personalisierte Nachricht
            response_message = greetings.get("thumbs_up_response", "{user} heißt dich herzlich in unserer Servercommunity willkommen!")
            response_message = response_message.format(user=user.mention)
            # Sende die personalisierte Nachricht im entsprechenden Kanal
            channel = reaction.message.channel
            await channel.send(response_message)

    # Event, das beim Empfang einer Nachricht aufgerufen wird
    @commands.Cog.listener()
    async def on_message(self, message):
        # Hier kannst du die Logik für die Verarbeitung der Nachrichten einfügen
        pass

def setup(bot):
    bot.add_cog(MessageHandler(bot))
