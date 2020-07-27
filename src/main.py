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
ROOM1 = settings.ROOM1
help_mes = message.help_mes

bot = commands.Bot(command_prefix='/jihou ')

global vc

# 起動
@bot.event
async def on_ready():
    print("Login OK!")
    await bot.get_channel(BOT_HelloWorld).send("希少な時報ちゃんの起床")

# ボイスチャンネルに誰かいるかみるやつ(
@bot.command()
async def find_voice(ctx):
    channel = discord.utils.get(
        bot.get_all_channels(), id=ROOM1)
    print(len(channel.members))

# 接続～
@bot.command()
async def connect(ctx):
    global vc
    vc = await ctx.author.voice.channel.connect()

# コマンド実行者のボイスチャンネルに移動して読む(TTSチャンネル以外)
@bot.command()
async def ts(ctx, arg):
    global vc
    if vc is None:
        vc = await ctx.author.voice.channel.connect()
        print("ボイスチャンネルに入りま～す")
    else:
        tts = gTTS(text=arg, lang='ja')
        tts.save('a.mp3')
        vc.play(discord.FFmpegPCMAudio(
            'a.mp3'))

# Help
@bot.command()
async def hlp(ctx):
    if ctx.channel.id == int(ROOM1):
        await ctx.send(help_mes)
    else:
        return

# 切断
@bot.command()
async def discon(ctx):
    global vc
    await vc.disconnect()


bot.run(TOKEN)

