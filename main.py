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

# 音声
KEIREN = settings.KEIREN
BIRIBIRI = settings.BIRIBIRI
JISSYOKU = settings.JISSYOKU
AA = settings.AA
JIKO = settings.JIKO

bot = commands.Bot(command_prefix='/jihou ')

global vc


def main():
    @bot.event
    async def on_ready():
        print("Login OK!")
        await bot.get_channel(BOT_HelloWorld).send("希少な時報ちゃんの起床")

    bot.run(TOKEN)


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

# コマンド版のTTS
@bot.command()
async def ts(ctx, arg):
    global vc
    if not bot.voice_clients:
        vc = await ctx.author.voice.channel.connect()
        tts_start(arg)
    elif bot.voice_clients[0].channel.id == ctx.author.voice.channel.id:
        tts_start(arg)
    else:
        # vc = await vc.move_to(ctx.author.voice.channel)
        await vc.disconnect()
        vc = await ctx.author.voice.channel.connect()
        tts_start(arg)


#痙攣
@bot.command()
async def keiren(ctx):
    vc.play(discord.FFmpegPCMAudio(KEIREN))

#ビリビリ
@bot.command()
async def biribiri(ctx):
    vc.play(discord.FFmpegPCMAudio(BIRIBIRI))

#実食
@bot.command()
async def jissyoku(ctx):
    vc.play(discord.FFmpegPCMAudio(JISSYOKU))

#ああ
@bot.command()
async def aa(ctx):
    vc.play(discord.FFmpegPCMAudio(AA))

#自己紹介
@bot.command()
async def jiko(ctx):
    vc.play(discord.FFmpegPCMAudio(JIKO))

# 切断
@bot.command()
async def discon(ctx):
    global vc
    await vc.disconnect()

# 読み上げ
def tts_start(arg):
    tts = gTTS(text=arg, lang='ja')
    tts.save('a.mp3')
    vc.play(discord.FFmpegPCMAudio(
    'a.mp3', options='-af volume=10dB,atempo=1.2'))


if __name__ == "__main__":
    main()
