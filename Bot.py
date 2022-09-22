import aiohttp
import discord
from discord.ext import commands
from discord import Embed, Color
from discord.utils import get

bot = commands.Bot(command_prefix='?', help_command=None)


@bot.command()
async def fb(ctx, genus, species):
    async with aiohttp.ClientSession() as cs:

        url = "https://fishbase.ropensci.org/species?genus=" + genus + "&Species=" + species + "&fields=genus,species,comments,image&limit=1"
        async with cs.get(url) as r:
            rj = await r.json()

            print(rj)
            print(url)
            try:
                genus = rj['data'][0]["Genus"]
                commonName = rj['data'][0]["FBname"]
                species = rj['data'][0]["Species"]
                comments = rj['data'][0]["Comments"]
                image = rj['data'][0]["image"]
                embed = discord.Embed(title="**" + "I Found Your Fish!" + "**",
                                      description=f"**Common Name**: {commonName}\n**Genus**: {genus} \n"
                                                  f"**Species**: {species} \n"
                                                  f"**Comments**: {comments} \n"
                                      , color=Color.blue())
                await ctx.send(embed=embed)
                imageEmbed = discord.Embed()
                imageEmbed.set_image(url=image)
                imageEmbed.set_footer(text="https://www.fishbase.se/summary/" + genus + "-" + species + ".html")
                await ctx.send(embed=imageEmbed)
                await ctx.send(ctx.author.mention)
            except TypeError:
                await ctx.send(embed=discord.Embed(title="Something Went Wrong...",
                                                   description="No results came up when searching for '" + genus + species + "'. Make sure that you have spelled the name of your fish correctly. You can also do the command `?help` to ensure that you are using the command correctly.",
                                                   color=Color.blue()))
                await ctx.send(ctx.author.mention)


@bot.command()
async def sl(ctx, genus, species):
    async with aiohttp.ClientSession() as cs:

        url = "https://fishbase.ropensci.org/sealifebase/species?genus=" + genus + "&Species=" + species + "&fields=genus,species,comments,image&limit=1"
        async with cs.get(url) as r:
            rj = await r.json()

            print(rj)
            print(url)
            try:
                genus = rj['data'][0]["Genus"]
                commonName = rj['data'][0]["FBname"]
                species = rj['data'][0]["Species"]
                comments = rj['data'][0]["Comments"]
                image = rj['data'][0]["image"]
                embed = discord.Embed(title="**" + "I Found Your Critter!" + "**",
                                      description=f"**Common Name**: {commonName}\n**Genus**: {genus} \n"
                                                  f"**Species**: {species} \n"
                                                  f"**Comments**: {comments} \n"
                                      , color=Color.blue())
                await ctx.send(embed=embed)
                imageEmbed = discord.Embed()
                imageEmbed.set_image(url=image)
                imageEmbed.set_footer(text="https://www.fishbase.se/summary/" + genus + "-" + species + ".html")
                await ctx.send(embed=imageEmbed)
                await ctx.send(ctx.author.mention)
            except TypeError:
                await ctx.send(embed=discord.Embed(title="Something Went Wrong...",
                                                   description="No results came up when searching for '" + genus + species + "'. Make sure that you have spelled the name of your fish correctly. You can also do the command `?help` to ensure that you are using the command correctly.",
                                                   color=Color.blue()))
                await ctx.send(ctx.author.mention)


@bot.command()
async def help(ctx):
    await ctx.send(embed=Embed(title="?search help", description='To search FishBase, use the command **?fb {genus} {species}** and to search SeaLifeBase , use the command **?sl {genus} {species}**!', color=Color.blue()))
    await ctx.send(ctx.author.mention)


@bot.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))

    activity = discord.Game(name="?help", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)


bot.run(TOKEN)
