import json
import requests
from .k_sync import *
from .k_async import *
from .lib.util import *

__title__ = "k-amino.py"
__description__ = "Amino Bots with python!"
__url__ = "https://github.com/kwel999/K_Amino"
__version__ = "1.5.0"
__author__ = "KWEL"
__author_email__ = "itskwel999@gmail.com"
__license__ = "Apache"

try:
    __newest__ = json.loads(requests.get("https://pypi.python.org/pypi/k-amino.py/json").text)["info"]["version"]
except requests.ConnectionError:
    __newest__ = __version__
finally:
    del json, requests

if __version__ != __newest__:
    print(f"\033[1;31;38mk_amino New Version!: {__newest__} (You are using {__version__})\033[1;36;33m\nDiscord server: \"https://discord.gg/zd8gyFJquT\"\033[1;0m")
else:
    print(f"\033[1;31;32mk_amino version : {__version__}\033[1;36;33m\nDiscord server: \"https://discord.gg/zd8gyFJquT\"\033[1;0m")
