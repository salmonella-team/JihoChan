import discord
from discord.ext import commands
from gtts import gTTS
from message import help_mes
import settings
import message

# 環境変数の読み出しだけど頭わるわるなのであとで変えておく
TOKEN = settings.TOKEN
BOT_HelloWorld = int(settings.BOT_HelloWorld)
TEST_Channel = settings.TEST_Channel
AFK = settings.AFK
GUILD = settings.GUILD
JIHOU = settings.JIHOU
help_mes = message.help_mes

bot = commands.Bot(command_prefix='/jihou ')

# 起動
@bot.event
async def on_ready():
    print("Login OK!")
    await bot.get_channel(BOT_HelloWorld).send("希少な時報ちゃんの起床")


bot.run(TOKEN)

