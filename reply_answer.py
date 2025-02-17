import discord

from answer import Answer


class ReplyAnswer(Answer):
    def __init__(self, reply_text, as_reply=True, image=None, **kwargs):
        super().__init__(**kwargs)

        if image is not None:
            image = discord.File(image)

        self.reply_text = reply_text  # Should be either a string or a function returning a string
        self.as_reply = as_reply
        self.image = image

    def get_text(self, message):
        if isinstance(self.reply_text, str):
            return self.reply_text
        else:
            return self.reply_text(message)

    async def send_answer(self, message, client):
        text = self.get_text(message)

        kwargs = {}

        if self.image is not None:
            kwargs["file"] = self.image

        if self.as_reply:
            await message.get_discord_message().reply(text, **kwargs)
        else:
            await message.get_discord_message().channel.send(text, **kwargs)


