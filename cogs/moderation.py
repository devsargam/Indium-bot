import discord
from discord import guild
from discord import reaction
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.core import command


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason="No reason provided"):
        # await user.kick(reason=reason)
        kick = discord.Embed(
            title=f":boot: Kicked {user.name}!",
            description=f"Reason: {reason}\nBy: {ctx.author.mention}"
        )
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send("message aayo?")

        
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason="No reason Provided"):
        await user.ban(reason=reason)
        ban = discord.Embed(
            title=f":hammer: Banned {user.name}!",
            description=f"Reson: {reason}\nBy: {ctx.author.mention}"
        )
        await ctx.send(embed=ban)
        await user.send(embed=ban)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx,  amount=2):
        await ctx.channel.purge(limit=amount + 1)
        purge = discord.Embed(
            title=f"Message deleted",
            description=f"{amount} message deleted by {ctx.author.mention}"
        )
        await ctx.channel.send(embed=purge)






def setup(client):
    client.add_cog(Moderation(client))