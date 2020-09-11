import discord, praw
from discord.ext import commands

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.Cog.listener()
async def on_ready(self):
    print("Commands Cog has been loaded\n-------")

reddit = praw.Reddit(client_id="D6gixR5uuwEySQ",
                     client_secret="2CZQlAwFlryos8J6U2hSovqI6xs",
                     redirect_uri="http://localhost:8080",
                     user_agent="testscript by /u/x2Fi")

@commands.command()
async def meme(self, ctx):
    subreddit = reddit.subreddit("memes")
    all_subs = []
    top = subreddit.top(limit = 50)
    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)
    em.set_image(url = url)
    await ctx.send(embed = em)

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
