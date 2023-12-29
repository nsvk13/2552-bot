import os
import disnake

from disnake.ext import commands
from dotenv import load_dotenv
from colorama import Fore, Style

os.system('color')

load_dotenv()

token = os.getenv('BOT_TOKEN')

if token is None:
    print(f"Bot token not found in .env file")
    exit(1)

bot = commands.Bot(command_prefix=('.'), intents=disnake.Intents.all())

def load_cogs(cogs_dir):
    for root, _, files in os.walk(cogs_dir):
        for filename in files:
            if filename.endswith('.py'):
                cog_path = os.path.join(root, filename)
                cog_module = os.path.relpath(cog_path, 'cogs').replace(os.sep, '.')[:-3]
                bot.load_extension(f'cogs.{cog_module}')
                print(f"{Fore.GREEN}Loaded extension: {cog_module}{Style.RESET_ALL}")

cogs_directory = 'cogs'
load_cogs(cogs_directory)

bot.run(token)