import discord
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content:
            await message.channel.send('Hello!')


        filetypes = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')
        for attachment in message.attachments:
            if attachment.filename.lower().endswith(filetypes):
                await message.channel.send(f'You sent {attachment.filename}!')
                print('here')
                break





intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True

client = MyClient(intents=intents)
client.run('')



# message.channel.send('')