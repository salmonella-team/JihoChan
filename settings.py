import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


TOKEN = os.environ.get("TOKEN")
BOT_HelloWorld = os.environ.get("BOT_HelloWorld")
TEST_Channel = os.environ.get("TEST_Channel")
AFK = os.environ.get("AFK")
GUILD = os.environ.get("GUILD")
KIYATAKE = os.environ.get("KIYATAKE")
JIHOU = os.environ.get("JIHOU")
ROOM1 = os.environ.get("ROOM1")


# sound

KEIREN = os.environ.get("KEIREN")
BIRIBIRI = os.environ.get("BIRIBIRI")
JISSYOKU = os.environ.get("JISSYOKU")
AA = os.environ.get("AA")
JIKO = os.environ.get("JIKO")