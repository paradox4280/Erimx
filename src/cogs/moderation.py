import discord
from discord.ext import commands
from discord.utils import get

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def allowed(ctx):
    return ctx.author.id in [414876304668622849, 384050038508093440]

@commands.command()
async def kick(self, ctx, member: discord.Member=None):
    await ctx.message.delete()
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.kick()
    await ctx.send(f"{member.mention} got kicked")

@commands.command()
async def ban(self, ctx, member: discord.Member=None):
    await ctx.message.delete()
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.ban()
    await ctx.send(f"{member.mention} got banned")

@commands.command()
async def mute(self, ctx, member: discord.Member=None):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.add_roles(role)
    await ctx.send(f"{member.mention} got muted")

@commands.command()
async def unmute(self, ctx, member: discord.Member=None):
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.remove_roles(role)
    await ctx.send(f"{member.mention} got unmuted")

def setup(bot):
    bot.add_cog(moderation(bot))
