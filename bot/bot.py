import discord
import os
import aiohttp

insert_url = "http://127.0.0.1:8000/submissions"
home_url = 'http://127.0.0.1:8000/'
all_submissions_url = 'http://127.0.0.1:8000/list_submissions'

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content == "Send all":
            async with aiohttp.ClientSession() as session:
                async with session.get(all_submissions_url,) as response:
                    print('Status: ', response.status)
                    if(response.status == 200):
                        await message.channel.send('Here are all the submissions: ')
                    result = await response.json()
                    await message.channel.send(result)

        if message.attachments:
            for attachment in message.attachments:
                filepath = f'files/{attachment.filename}'
                name, type = os.path.splitext(attachment.filename)

                payload = {
                    "user_id": str(message.author.id),
                    "file_name": attachment.filename,
                    "file_type": type
                }

                async with aiohttp.ClientSession() as session:
                    async with session.post(insert_url, json=payload ) as response:
                        print("Status: ", response.status)
                        if(response.status == 200):
                            await message.channel.send("File succesfully uploaded to fastAPI database.")
                            await attachment.save(filepath)
                        result = await response.json()
                        print(result)

intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True

client = MyClient(intents=intents)
client.run('')

# message.channel.send('')