import re
import discord
from random import random

TOKEN = "ENTER YOUR DISCORD TOKEN HERE"
client = discord.Client()

linux_copy_pasta = "I'd just like to interject for a moment. What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.\nMany computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called \"Linux\", and many of its users are not aware that it is basically the GNU system, developed by the GNU Project.\nThere really is a Linux, and these people are using it, but it is just a part of the system they use. Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called \"Linux\" distributions are really distributions of GNU/Linux."

# Non case sensitive, keys must be words
word_responses = {"slapen": "Slaapwel!",
                  "kat": "Miauw",
                  "hond": "Woef",
                  "haan": "Kukeleku",
                  "vis": "Blub",
                  "linux": linux_copy_pasta}
# Multiple keys with same value
word_responses.update(dict.fromkeys(
    ['eten', 'lunchen', 'dinner', 'voedsel', 'lunch', 'ontbijt', 'breakfast', 'brunch', 'snack', 'snacken'],
    "Smakelijk!"))
word_responses.update(dict.fromkeys(['vos', 'fox'], "Ring-ding-ding-ding-dingeringeding!"))
word_responses.update(dict.fromkeys(['aescu', 'aesculapia'], "ieuw"))

phrase_responses = {"slok of gene slok": "WINOK"}

emoji_reactions = {",p leave": "👋",
                   "succes": "❤",
                   "you have been unsubscribed due to inactivity!": "😢",
                   "dood": "🔫",
                   "Bollekebot": "👀",
                   "tea": "🍵",
                   "cupcake": "🧁",
                   "good bot": "😘",
                   "bad bot": "😠"}
emoji_reactions.update(dict.fromkeys(['SE', 'Software Engineering'], "🤮"))
emoji_reactions.update(dict.fromkeys(['birthday', "Birthday", "verjaardag", 'Verjaardag'], "🥳"))
emoji_reactions.update(dict.fromkeys(['love', 'liefde', 'hou van'], "😍"))


async def add_reactions(message, reactions):
    for reaction in reactions:
        await message.add_reaction(reaction)


@client.event
async def on_ready():
    print(f'Active on: ')
    for guild in client.guilds:
        print(f'- {guild.name}')


@client.event
async def on_message(message):
    # Whoever you are, wherever you are, never say WINAK with lowercase letters
    if "winak" in message.content:
        await message.reply("*WINAK")

    # Don't react to my own messages (except in my own bot test channel), only react to messages in the Pomodoro channel
    # and don't react to messages from this bot
    if message.channel.name != "pomodoro" or \
            (message.author.display_name == "Arno Deceuninck" and message.guild.name != "Bot Tests") or \
            message.author == client.user:
        return

    # Get the lowercase message without special symbol
    lower_message = message.content.lower().replace(',', '').replace('!', '').replace('?', '').replace('.', '')
    # Get the words (split the spaces), a set is faster to search in
    words = set(lower_message.split())

    global phrase_responses, emoji_reactions, word_responses

    # Phrase responses
    for key in phrase_responses:
        if key in lower_message:
            await message.reply(phrase_responses[key])

    # word responses
    for word in words:
        if word in word_responses:
            await message.reply(word_responses[word])

    # emoji reactions
    for key in emoji_reactions:
        if key in message.content:
            await add_reactions(message, emoji_reactions[key])
            # await message.add_reaction(emoji_reactions[key])

    # Special cases
    if ("help" in words or "helpen" in words or "fix" in message.content) and "?" in message.content:
        await message.reply("Have you tried turning it off and on again?")
    if pattern := re.match("[iI]k ben (.*)", message.content):
        await message.reply(f"Hey {pattern.group(1)}, ik ben Bollekebot!")
    if message.author.display_name == "Alexander" and random() < 0.1:
            await message.add_reaction("🥴")
    if "69" in message.content and not message.author.bot:
        await add_reactions(message, "🇳🇮🇨🇪")
    if "mateo" in lower_message and message.guild.name == "WINAK" and not message.author.bot:
        await message.add_reaction(discord.utils.get(message.guild.emojis, name="mateo"))

@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.content == "try me":
        await reaction.remove(user)

client.run(TOKEN)