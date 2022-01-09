TOKEN = "ENTER YOUR DISCORD TOKEN HERE"

# Used when adding letter-per-letter emoji reactions on a message
letter_emojis = {"a": "🇦🅰🔼👖🙈🩳🦑", "b": "🇧🅱️", "c": "🇨◀️", "d": "🇩▶👂🦻", "e": "🇪💶🎼📧🟦", "f": "🇫🤏",
                 "g": "🇬",
                 "h": "🇭🦕", "i": "🇮ℹ❕️❗", "j": "🇯☂️", "k": "🇰◀️🎋", "l": "🇱🦾💪📃", "m": "🇲📧👑", "n": "🇳🟦📰",
                 "o": "🇴🅾⭕🟠", "p": "🇵", "q": "🇶", "r": "🇷🎗🎋", "s": "🇸🪱", "t": "🇹✝️", "u": "🇺👅",
                 "v": "🇻🔽🔻🥇🥈🥉", "w": "🇼🗑️", "x": "🇽", "y": "🇾", "z": "🇿"}

# A list containing motivational quotes
with open("quotes.txt") as f:
    quotes = f.read().splitlines()

# A list containing motivational quotes
with open("motivation.txt") as f:
    motivation = f.read().splitlines()