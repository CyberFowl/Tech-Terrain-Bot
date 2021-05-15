import discord
import time
from config import token

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in")

        await client.change_presence(activity=discord.Game("t!help"))

    async def on_message(self, message):
        
        msg = message.content.upper()
        if message.author != client.user:
                
            if msg == "T!SPOTIFY":
                print("SPOTIFY")
                embed=discord.Embed(title="Tech Terrain - Spotify", url="https://open.spotify.com/show/3e67xEFz7WjjO42ZNae0tR")
                await message.channel.send(embed=embed)
                
            if msg == "T!GPODCASTS":
                print("T!GPODCASTS")
                embed=discord.Embed(title="Tech Terrain - Google Podcasts", url="https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy8zM2NiNTVkOC9wb2RjYXN0L3Jzcw==")
                await message.channel.send(embed=embed)
                
            if msg == "T!ANCHOR":
                print("T!ANCHOR")
                embed=discord.Embed(title="Tech Terrain - Anchor", url="https://anchor.fm/rammadhav")
                await message.channel.send(embed=embed)
                
            if msg == "T!RADIOPUBLIC":
                print("T!RADIOPUBLIC")
                embed=discord.Embed(title="Tech Terrain - Radiopublic", url="https://radiopublic.com/tech-terrain-6nXrLZ")
                await message.channel.send(embed=embed)
                
            if msg == "T!BREAKER":
                print("T!BREAKER")
                embed=discord.Embed(title="Tech Terrain - Breaker", url="https://www.breaker.audio/blah-blah-blah-w-slash-ram-madhav")
                await message.channel.send(embed=embed)
                
            if msg == "T!OVERCAST":
                print("T!OVERCAST")
                embed=discord.Embed(title="Tech Terrain - Overcast", url="https://overcast.fm/itunes1530452022/blah-blah-blah-w-ram-madhav")
                await message.channel.send(embed=embed)
                
            if msg == "T!POCKETCASTS":
                print("T!POCKETCASTS")
                embed=discord.Embed(title="Tech Terrain - Pocketcasts", url="https://pca.st/podcast/3518d280-d04f-0138-e763-0acc26574db2")
                await message.channel.send(embed=embed)

            if msg == "T!APPLE":
                print("T!APPLE")
                embed=discord.Embed(title="Tech Terrain - Apple Podcasts", url="https://podcasts.apple.com/au/podcast/tech-terrain/id1530452022")
                await message.channel.send(embed=embed)
                
            if msg == "T!PLATFORMS":
                print("T!PLATFORMS")
                embed=discord.Embed(title="Anchor" + "\n" + "Spotify" + "\n" + "Radiopublic" + "\n" + "Pocketcasts" + "\n" + "Breaker" + "\n" + "Google podcasts" + "\n" + "Overcast" + "\n" + "Apple Podcasts")
                await message.channel.send(embed=embed)
            
            if msg == "T!HELP" or msg == "<@!786189542242648074>":
                print("T!HELP")
                embed=discord.Embed(title="Help Menu", description="Ping the bot or use T!help. Commands are NOT case sensitive", color=0x00ad23)
                embed.set_thumbnail(url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fanchor.fm%2Frammadhav&psig=AOvVaw0fTD_nhFX9n1TkI8EOu1Yo&ust=1610126168340000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJD9mcipiu4CFQAAAAAdAAAAABAD")
                embed.add_field(name="T!spotify", value="Sends a Spotify link", inline=False)
                embed.add_field(name="T!gpodcasts", value="Sends a Google Podcasts link", inline=False)
                embed.add_field(name="T!anchor", value="Sends an Anchor link", inline=False)
                embed.add_field(name="T!radiopublic", value="Sends a Radiopublic link", inline=False)
                embed.add_field(name="T!breaker", value="Sends a Breaker link", inline=False)
                embed.add_field(name="T!overcast", value="Sends an Overcast link", inline=False)
                embed.add_field(name="T!pocketcasts", value="Sends a Pocketcasts link", inline=False)
                embed.add_field(name="T!apple", value="Sends an Apple Podcasts link", inline=False)
                embed.add_field(name="T!platforms", value="Lists all the platforms the podcast is available on", inline=False)
                embed.set_footer(text="Made and owned by CyberFowl#8931")
                await message.channel.send(embed=embed)

            if msg == "T!PING":
                print("T!PING")
                await message.channel.send(f":ping_pong: Pong! | Message took ***{round(client.latency * 1000)}ms*** to respond")

print("Code is running")

client = MyClient()
client.run(token)
