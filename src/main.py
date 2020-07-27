import discord
from discord.ext import commands
from gtts import gTTS
import schedule
import time
import settings

# 環境変数の読み出しだけど頭わるわるなのであとで変えておく
TOKEN = settings.TOKEN
BOT_HelloWorld = int(settings.BOT_HelloWorld)
TEST_Channel = settings.TEST_Channel
AFK = settings.AFK
GUILD = settings.GUILD
KIYATAKE = settings.KIYATAKE
JIHOU = settings.JIHOU
ROOM1 = settings.ROOM1

bot = commands.Bot(command_prefix='/jihou ')

global vc



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

# @bot.event
# async def on_voice_state_update(member, before, after):
#     # AFKに移動しない
#     global vc
#     if member.id == JIHOU or member.id == KIYATAKE:
#         print("除外")
#         return
#     elif vc:
#         print("移動！")
#         await vc.move_to(after.channel)
#     elif after.channel.id == AFK:
#         return
#     elif after.channel.id == None:
#         vc.disconnect()
#     else:
#         vc = await after.channel.connect()
#     # elif vc == None:
#     # vc = await after.channel.connect()
#     # else:
#     # vc = await vc.move_to(after.channel)

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

# 切断

@bot.command()
async def discon(ctx):
    global vc
    await vc.disconnect()

bot.run(TOKEN)

