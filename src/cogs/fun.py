import discord, praw
from discord.ext import commands

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.Cog.listener()
async def on_ready(self):
    print("Commands Cog has been loaded\n-------")

 @commands.command(name='wyr', aliases=['wouldyourather', 'would-you-rather'])
    async def _wyr(self, ctx):
      r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
      soup = bs4(r, 'html.parser')
      qa = soup.find(id='qa').text
      qor = soup.find(id='qor').text
      qb = soup.find(id='qb').text
      paradox = discord.Embed(description=f'{qa}\n{qor}\n{qb}', color = 16202876)
      await ctx.send(embed=paradox)

    @commands.command(name='dick', aliases=['dong', 'penis', 'pp'])
    async def _dick(self, ctx, *, user: discord.Member = None):
      if user is None:
        user = ctx.author
        size = random.randint(1, 15)
        dong = ""
        for _i in range(0, size):
          dong += "="
        paradox = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=16202876)
        await ctx.send(embed=paradox)

@commands.command(name='8ball')
async def _teball(ctx, *, question): #x2Fi
    await ctx.message.delete()
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
	  'Maybe',
	  'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(FunCog(bot))
