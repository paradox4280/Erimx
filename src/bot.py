#ERIMX Made By Paradox4280 aka c2FI, x2Fi, RG9t

import discord, base64, codecs, requests, urllib.parse, datetime, asyncio, sys, praw
import random, aiohttp, io, json, os, string, platform, time, bs4, colorama

from discord.ext import (
    commands
)
from discord.voice_client import VoiceClient
# from discord.ext.commands import bot
from bs4 import BeautifulSoup as bs4
from colorama import Fore, Style
from discord import Permissions
from discord.utils import get
from discord import User
from os import system

paradox = commands.Bot(command_prefix=os.getenv('PREFIX'))
[paradox.load_extension(f"cogs.{cog[:-3]}") for cog in os.listdir("cogs") if cog.endswith(".py")]

@paradox.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Her"))
    print(f'\n{Fore.GREEN}[>] {Fore.RESET}{Fore.CYAN}Logged in as{Fore.RESET} {Fore.YELLOW}{paradox.user.name}#{paradox.user.discriminator}\n')
    print(f'\n{Fore.GREEN}[>]{Fore.RESET} {Fore.CYAN}User ID:{Fore.RESET} {Fore.YELLOW}{paradox.user.id}\n')
    print(f'\n{Fore.GREEN}[>]{Fore.RESET} {Fore.CYAN}Version:{Fore.RESET} {Fore.YELLOW}{discord.__version__}\n')

paradox.run(os.getenv('BOT_TOKEN'))
