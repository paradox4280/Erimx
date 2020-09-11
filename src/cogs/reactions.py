from discord.ext import commands

from discord import Embed
from discord.ext.commands import Cog
from datetime import date, timedelta
from discord.ext.commands import command, has_permissions

class Reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
@commands.has_permissions(manage_guild=True)
async def create_giveaway(self, ctx, mins: int, *, description: str):
    embed = discord.Embed(title="Giveaway",
                      description=description,
                      colour=ctx.author.colour,
                      timestamp=datetime.utcnow())
    fields = [("End time", f"{datetime.utcnow()+timedelta(seconds=mins*60)} UTC", False)]
    for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
    message = await ctx.send(embed=embed)
    await message.add_reaction("✅")
    self.giveaways.append((message.channel.id, message.id))
    self.bot.scheduler.add_job(self.complete_giveaway, "date", run_date=datetime.now()+timedelta(seconds=mins),
                                args=[message.channel.id, message.id])
async def complete_poll(self, channel_id, message_id):
    message = await self.bot.get_channel(channel_id).fetch_message(message_id)
    most_voted = max(message.reactions, key=lambda r: r.count)
    await message.channel.send(f"The results are in and option {most_voted.emoji} was the most popular with {most_voted.count-1:,} votes!")
    self.polls.remove((message.channel.id, message.id))
async def complete_giveaway(self, channel_id, message_id):
    message = await self.bot.get_channel(channel_id).fetch_message(message_id)
    if len((entrants := [u for u in await message.reactions[0].users().flatten() if not u.bot])) > 0:
        winner = choice(entrants)
        await message.channel.send(f"Congratulations {winner.mention} - you won the giveaway!")
        self.giveaways.remove((message.channel.id, message.id))
    else:
        await message.channel.send("Giveaway ended - no one entered!")
        self.giveaways.remove((message.channel.id, message.id))

def setup(bot):
    bot.add_cog(Reactions(bot))
