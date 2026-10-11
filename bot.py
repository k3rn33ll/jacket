import io
import textwrap
from datetime import datetime

import discord
from discord import app_commands
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
