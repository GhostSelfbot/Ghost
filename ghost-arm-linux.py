#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import ssl 

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

import os
from re import T

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
printSpaces = " "

if os.name == "nt":
    os.system("cls")
    # os.system("mode 100,25")
    os.system("title Ghost")
if os.name == "posix":
    os.system("clear")

print(" ")
print(f"{printSpaces}Loading Ghost...")
print(" ")

import sys
import subprocess
import logging

if not os.path.exists('logs/'): 
    os.makedirs('logs/')
    print(printSpaces+"Made logs folder.")

open("logs/info.log", "w").write(" ")
print(printSpaces+"Resetting info log.")
open("logs/warning.log", "w").write(" ")
print(printSpaces+"Resetting warning log.")
open("logs/error.log", "w").write(" ")
print(printSpaces+"Resetting error log.")
open("logs/critical.log", "w").write(" ")
print(printSpaces+"Resetting critical log.")
print(" ")

logging.basicConfig(filename="logs/info.log", level=logging.INFO)
logging.basicConfig(filename="logs/warning.log", level=logging.WARNING)
logging.basicConfig(filename="logs/error.log", level=logging.ERROR)
logging.basicConfig(filename="logs/critical.log", level=logging.CRITICAL)

try: 
    # pythonVersion = float(str(sys.version_info[0])+"."+str(sys.version_info[1]))
    # if pythonVersion < 3.8:
    #     input("You're not using a supported Python version.")
    #     exit()

    # else:
    #     print("You're using a supported python version, " + str(pythonVersion))

    def install(package):
        if os.name == "nt":
            os.system(f"{sys.executable} -m pip install {package}")
        if os.name == "posix":
            os.system(f"pip3.9 install {package}")

    def uninstall(package):
        if os.name == "nt":
            os.system(f"{sys.executable} -m pip uninstall {package}")
        if os.name == "posix":
            os.system(f"pip3.9 uninstall {package}")

    if "discord.py" in sys.modules:
        uninstall("discord.py")

    if "discordselfbot" in sys.modules:
        uninstall("discordselfbot")

    try:
        import discord
    except ModuleNotFoundError:
        install("discord.py-self")

    try:
        import pyPrivnote as pn
    except ModuleNotFoundError:
        install("pyPrivnote")

    try:
        import names
    except ModuleNotFoundError:
        install("names")

    try:
        import simplejson
    except ModuleNotFoundError:
        install("simplejson")

    try:
        import aiohttp
    except ModuleNotFoundError:
        install("aiohttp")

    try:
        from colour import Color
    except ModuleNotFoundError:
        install("colour")

    try:
        from termcolor import colored
    except ModuleNotFoundError:
        install("termcolor")

    try:
        from faker import Faker
    except ModuleNotFoundError:
        install("Faker")

    if os.name == "nt":
        try:
            import plyer
        except ModuleNotFoundError:
            install("plyer")

    try:
        from sty import fg, bg, ef, rs, Style, RgbFg
    except ModuleNotFoundError:
        install("sty==1.0.0rc0")

    try:
        import discord_rpc
    except ModuleNotFoundError:
        install("discord-rpc.py")

    try:
        import requests
    except ModuleNotFoundError:
        install("requests")

    try:
        import uwuify
    except ModuleNotFoundError:
        install("uwuify")

    try:
        import numpy as np
    except ModuleNotFoundError:
        install("numpy")

    try:
        import discum
    except ModuleNotFoundError:
        install("discum")

    try:
        from discord_webhook import DiscordWebhook, DiscordEmbed
    except ModuleNotFoundError:
        install("discord-webhook")

    try:
        from random_user_agent.user_agent import UserAgent
        from random_user_agent.params import SoftwareName, OperatingSystem
    except ModuleNotFoundError:
        install("random_user_agent")    


    try:
        import GPUtil
    except ModuleNotFoundError:
        install("gputil")    

    try:
        import psutil
    except ModuleNotFoundError:
        install("psutil")

    try:
        import PIL
    except ModuleNotFoundError:
        install("pillow")

    try:
        import pygame
    except ModuleNotFoundError:
        install("pygame")        

    # if os.name == "posix":
    #     if str(subprocess.check_output(["apt-cache", "policy", "libportaudio2"])).split("\\n")[1][2:].split(": ")[1] == "(none)":
    #         os.system("sudo apt-get install libportaudio2")

    try:
        import sounddevice
    except ModuleNotFoundError:
        install("sounddevice")

    try:
        import discord_emoji
    except ModuleNotFoundError:
        install("discord-emoji")

    if os.name == "nt":
        try:
            import wmi
        except ModuleNotFoundError:
            install("WMI")

        import wmi

    if os.name == "nt":
        import plyer
    if os.name == "nt":
        import tkinter
    import discord_emoji
    import threading
    import pygame
    import PIL
    from random_user_agent.user_agent import UserAgent
    from random_user_agent.params import SoftwareName, OperatingSystem
    from discord_webhook import DiscordWebhook, DiscordEmbed
    import discum
    if os.name == "nt":
        import winshell
    import uwuify
    import getpass
    import mimetypes
    import discord_rpc
    from sty import fg, bg, ef, rs, Style, RgbFg
    import discord
    import json
    import pyPrivnote as pn
    import random
    import asyncio
    import requests
    import aiohttp
    import names
    import string
    import simplejson
    import base64
    import math
    import time
    import urllib
    import urllib.request
    import codecs
    import platform
    import psutil
    import re
    import ctypes
    import ctypes.util
    import GPUtil
    from urllib.request import Request, urlopen
    from colour import Color
    from discord.ext import commands
    from discord.utils import get
    from termcolor import colored, cprint
    from os.path import dirname, basename, isfile, join
    from datetime import datetime, timedelta
    import numpy as np
    from faker import Faker

    def update_config():
        configJson = json.load(open("config.json"))
        configFile = open("config.json", "r").read()

        if ("riskmode" not in configFile):
            print(f"{printSpaces}Adding risk mode to config.")
            configJson["riskmode"] = bool(False)

        if ("load_on_startup" not in configFile):
            print(f"{printSpaces}Adding load on startup to config.")
            configJson["load_on_startup"] = bool(False)

        if ("giveaway_join_delay" not in configFile):
            print(f"{printSpaces}Adding giveaway join delay to config.")
            configJson["giveaway_join_delay"] = 15

        if ("giveaway_sniper_ui" not in configFile):
            print(printSpaces+"Adding giveaway sniper ui to config.")
            configJson["giveaway_sniper_ui"] = False

        if ("snipers" not in configFile):
            configJson["snipers"] = {}
            print(printSpaces+"Adding nitro sniper to config.")
            configJson["snipers"]["nitro"] = bool(True)
            print(printSpaces+"Adding privnote sniper to config.")
            configJson["snipers"]["privnote"] = bool(True)
            print(printSpaces+"Adding giveaway sniper to config.")
            configJson["snipers"]["giveaway"] = bool(True)

        if ("webhooks" not in configFile):
            configJson["webhooks"] = {}
            print(printSpaces+"Adding nitro webhook to config.")
            configJson["webhooks"]["nitro"] = ""
            print(printSpaces+"Adding privnote webhook to config.")
            configJson["webhooks"]["privnote"] = ""
            print(printSpaces+"Adding giveaway webhook to config.")
            configJson["webhooks"]["giveaway"] = ""

        if ("motd" not in configFile):
            configJson["motd"] = {}
            configJson["motd"]["custom"] = bool(False)
            print(printSpaces+"Adding custom motd option to config.")
            configJson["motd"]["custom_text"] = "Super Cool Custom MOTD"  
            print(printSpaces+"Adding custom motd text to config.")

        if ("selfbot_detect" in configFile):
            configJson.pop("selfbot_detect")
            print(printSpaces+"Removing selfbot detect from config.")

        if ("ghostping_detect" in configFile):
            configJson.pop("ghostping_detect")
            print(printSpaces+"Removing ghostping detect from config.")

        if ("ghostping" not in configJson["webhooks"]):
            configJson["webhooks"]["ghostping"] = ""
            print(printSpaces+"Adding ghostping webhook to config.")

        if ("friendsupdate" not in configJson["webhooks"]):
            configJson["webhooks"]["friendsupdate"] = ""
            print(printSpaces+"Adding friends update webhook to config.")            

        if ("dmtyping" not in configJson["webhooks"]):
            configJson["webhooks"]["dmtyping"] = ""
            print(printSpaces+"Adding DM typing webhook to config.")       

        if ("guildleave" not in configJson["webhooks"]):
            configJson["webhooks"]["guildleave"] = ""
            print(printSpaces+"Adding guild leave webhook to config.")  

        if ("selfbot" not in configJson["webhooks"]):
            configJson["webhooks"]["selfbot"] = ""
            print(printSpaces+"Adding selfbot webhook to config.")  

        if ("tickets" not in configJson["webhooks"]):
            configJson["webhooks"]["tickets"] = ""
            print(printSpaces+"Adding tickets webhook to config.")  

        if ("sounds" not in configFile):
            configJson["sounds"] = bool(True)
            print(printSpaces+"Adding sounds toggle to config.")

        if ("detections" not in configFile):
            configJson["detections"] = {}
            configJson["detections"]["selfbot"] = bool(True)
            print(printSpaces+"Adding selfbot detection to config.")
            configJson["detections"]["ghostping"] = bool(True)
            print(printSpaces+"Adding ghostping detection to config.")
            configJson["detections"]["bans"] = bool(True)
            print(printSpaces+"Adding ban detection to config.")

        if ("deletedmessages" not in configJson["detections"]):
            configJson["detections"]["deletedmessages"] = bool(False)
            print(printSpaces+"Adding deleted messages detection to config.")
        
        if ("webhookmodification" not in configJson["detections"]):
            configJson["detections"]["webhookmodification"] = bool(True)
            print(printSpaces+"Adding webhook modification detection to config.")

        if ("friendsupdate" not in configJson["detections"]):
            configJson["detections"]["friendsupdate"] = bool(True)
            print(printSpaces+"Adding friends update detection to config.")            

        if ("dmtyping" not in configJson["detections"]):
            configJson["detections"]["dmtyping"] = bool(True)
            print(printSpaces+"Adding DM typing detection to config.")       

        if ("guildleave" not in configJson["detections"]):
            configJson["detections"]["guildleave"] = bool(True)
            print(printSpaces+"Adding guild leave detection to config.")     

        if ("embed_mode" not in configFile):
            configJson["embed_mode"] = bool(False)
            print(printSpaces+"Adding embed mode to config.")

        if ("ignored_servers" not in configFile):
            configJson["ignored_servers"] = {}
            configJson["ignored_servers"]["nitro"] = []
            print(printSpaces+"Adding nitro ignored servers to config.")
            configJson["ignored_servers"]["privnote"] = []
            print(printSpaces+"Adding privnote ignored servers to config.")
            configJson["ignored_servers"]["giveaways"] = []
            print(printSpaces+"Adding giveaways ignored servers to config.")
            configJson["ignored_servers"]["ghostpings"] = []
            print(printSpaces+"Adding ghostpings ignored servers to config.")
            configJson["ignored_servers"]["selfbots"] = []
            print(printSpaces+"Adding selfbots ignored servers to config.")
            configJson["ignored_servers"]["bans"] = []
            print(printSpaces+"Adding bans ignored servers to config.")
            configJson["ignored_servers"]["deletedmessages"] = []
            print(printSpaces+"Adding deletedmessages ignored servers to config.")

        if ("webhookmodifications" not in configJson["ignored_servers"]):
            configJson["ignored_servers"]["webhookmodifications"] = []
            print(printSpaces+"Adding webhook modification ignored servers to config.")

        if ("tickets" not in configJson["snipers"]):
            configJson["snipers"]["tickets"] = bool(True)
            print(printSpaces+"Adding ticket sniper to config.")

        if ("tickets" not in configJson["ignored_servers"]):
            configJson["ignored_servers"]["tickets"] = []
            print(printSpaces+"Adding tickets ignored servers to config.")    

        if ("guildleave" not in configJson["ignored_servers"]):
            configJson["ignored_servers"]["guildleave"] = []
            print(printSpaces+"Adding guild leave ignored servers to config.")     

        if ("api_keys" not in configFile):
            print(printSpaces+"Adding api keys to config.")
            configJson["api_keys"] = {}
            configJson["api_keys"]["tenor"] = ""

        if ("alexflipnote" not in configJson["api_keys"]):
            print(printSpaces+"Adding alexflipnote to api keys.")
            configJson["api_keys"]["alexflipnote"] = ""

        if ("afkmode" not in configFile):
            print(printSpaces+"Adding afkmode to config.")
            configJson["afkmode"] = {}
            configJson["afkmode"]["enabled"] = False
            configJson["afkmode"]["replymessage"] = "im currently afk :/"

        json.dump(configJson, open("config.json", "w"), sort_keys=False, indent=4) 

        configJson = json.load(open("config.json"))
        configFile = open("config.json", "r").read()

        if ("load_on_startup" in configFile):
            configJson.pop("load_on_startup")
            print(printSpaces+"Removing load on startup from config.")

        json.dump(configJson, open("config.json", "w"), sort_keys=False, indent=4) 

    if not os.path.exists('pytoexe/'): os.makedirs('pytoexe/');
    if not os.path.exists('privnote-saves/'): os.makedirs('privnote-saves/');
    if not os.path.exists('scripts/'): os.makedirs('scripts/');
    if not os.path.exists('data/'): os.makedirs('data/');
    if not os.path.exists('themes/'): os.makedirs('themes/');
    if not os.path.exists('sounds/'): os.makedirs('sounds/');
    # if not os.path.isfile('icon.ico'): open('icon.ico', 'wb').write(requests.get('https://ghost.cool/favicon.ico', allow_redirects=True).content);  
    # if not os.path.isfile('sounds/connected.mp3'): open('sounds/connected.mp3', 'wb').write(requests.get('https://ghost.cool/assets/sounds/connected.mp3', allow_redirects=True).content);  
    # if not os.path.isfile('sounds/error.mp3'): open('sounds/error.mp3', 'wb').write(requests.get('https://ghost.cool/assets/sounds/error.mp3', allow_redirects=True).content);  
    # if not os.path.isfile('sounds/notification.mp3'): open('sounds/notification.mp3', 'wb').write(requests.get('https://ghost.cool/assets/sounds/notification.mp3', allow_redirects=True).content);  
    # if not os.path.isfile('sounds/success.mp3'): open('sounds/success.mp3', 'wb').write(requests.get('https://ghost.cool/assets/sounds/success.mp3', allow_redirects=True).content);  
    # if not os.path.isfile('sounds/giveaway-win.mp3'): open('sounds/giveaway-win.mp3', 'wb').write(requests.get('https://ghost.cool/assets/sounds/giveaway-win.mp3', allow_redirects=True).content);  
    # if not os.path.exists('trump-tweets/'): os.makedirs('trump-tweets/');
    # if not os.path.exists('trump-tweets/assets'): os.makedirs('trump-tweets/assets');
    # if not os.path.isfile('trump-tweets/assets/bg.png'):
    #     dtrumpbg = 'https://bennyware.xyz/files/dtrumptweetbg.png'
    #     dtrumpbg_r = requests.get(dtrumpbg, allow_redirects=True)
    #     open('trump-tweets/assets/bg.png', 'wb').write(dtrumpbg_r.content)
    # if not os.path.isfile('trump-tweets/assets/roboto.ttf'):
    #     font = 'https://bennyware.xyz/files/roboto.ttf'
    #     font_r = requests.get(font, allow_redirects=True)
    #     open('trump-tweets/assets/roboto.ttf', 'wb').write(font_r.content)
    # open('data/icon.png', 'wb').write(requests.get('http://ghost.cool/assets/icon.png', allow_redirects=True).content)
    if not os.path.isfile('config.json'):
        f = open('config.json', "w")
        f.write("""
{
    "token": "",
    "prefix": ".",
    "delete_timeout": 15,
    "theme": "Ghost"
}
        """)
        f.close()
    if not os.path.isfile('giveawaybots.json'):
        f = codecs.open('giveawaybots.json', "w", encoding="UTF-8")
        f.write("""
{
    "294882584201003009": "🎉"
}
        """)
        f.close()        
    if not os.path.isfile('customcommands.json'):
        f = open('customcommands.json', "w")
        f.write("""
{
    "cmd1": "this is cmd1",
    "cmd2": "this is cmd2"
}
        """)
        f.close()
    if not os.path.isfile('richpresence.json'):
        f = open('richpresence.json', 'w')
        f.write("""
{
    "enabled": true,
    "client_id": 807369019744059403,
    "details": "Using Ghost selfbot...",
    "state": "",
    "large_image_key": "icon",
    "large_image_text": "ghost.cool"
}
        """)
        f.close()

    if os.path.isfile("richpresence.json"):
        jsonFile = json.load(open("richpresence.json"))
        if jsonFile["client_id"] == 807369019744059403:
            jsonFile["client_id"] = 877223591828136006
        if jsonFile["details"] == "Using Ghost selfbot...":
            jsonFile["details"] = "Using Ghost..."
        if "small_image_key" not in jsonFile:
            jsonFile["small_image_key"] = "small"
        if "small_image_text" not in jsonFile:
            jsonFile["small_image_text"] = "best sb for £2"
        json.dump(jsonFile, open("richpresence.json", "w"), sort_keys=False, indent=4)

    if not os.path.isfile('themes/Ghost.json'):
        f = open('themes/Ghost.json', "w")
        f.write("""
{
    "embedtitle": "Ghost",
    "embedcolour": "#3B79FF",
    "consolecolour": "#3B79FF",
    "embedfooter": "ghost.cool",
    "embedfooterimage": "https://ghost.cool/assets/icon.gif",
    "globalemoji": ":blue_heart:",
    "embedimage": "https://ghost.cool/assets/icon.gif"
}
        """)
        f.close()
    if not os.path.isfile('data/personal-pins.json'):
        f = open('data/personal-pins.json', "w")
        f.write("{}")
        f.close()
    if not os.path.isfile('data/tokens.txt'):
        f = open('data/tokens.txt', "w")
        f.close()
    if not os.path.isfile('data/rickroll.txt'):
        f = open('data/rickroll.txt', "w")
        f.write("""We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
And if you ask me how I'm feeling
Don't tell me you're too blind to see
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give, never gonna give
(Give you up)
(Ooh) Never gonna give, never gonna give
(Give you up)
We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt...""")
        f.close()
    if not os.path.isfile('scripts/example.py'):
        f = open('scripts/example.py', "w")
        f.write('''
@Ghost.command(name="example", description="Example custom script.", usage="example")
async def example(Ghost):
    exampleEmbed = discord.Embed(
        title="Example Embed",
        description="""
        An example embed to display what you can do in scripts.
        Check `scripts/example.py` to see the code!
        ** **
        Ghost scripts are all created in python using discord.py so you can use any feature from discord.py.
        """,
        color=__embedcolour__
    )
    exampleEmbed.add_field(name="Variables", value="""
    **\_\_embedtitle\_\_** : Theme's embed title.
    **\_\_embedcolour\_\_** : Theme's embed colour.
    **\_\_embedfooter\_\_** : Theme's embed footer.
    **\_\_embedimage\_\_** : Theme's embed image url.
    **\_\_embedfooterimage\_\_** : Theme's embed footer image url.
    
    **\_\_embedemoji\_\_** : Theme's global emoji.
    **\_\_deletetimeout\_\_** : Config delete timeout (seconds).
    """)
    exampleEmbed.set_thumbnail(url=__embedimage__)
    exampleEmbed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)

    await Ghost.send("Hello World!", embed=exampleEmbed)
    ''')
        f.close()
    if json.load(open("config.json"))["token"] == "":
        os.system("cls")
        os.system("clear")
        print("")
        print("Please input your Discord token below.".center(os.get_terminal_size().columns))
        print("")
        token = input()

        config = json.load(open("config.json"))
        config["token"] = (token)
        json.dump(config, open('config.json', 'w'), sort_keys=False, indent=4)

    ccmd_file = open('customcommands.json')
    ccmd = json.load(ccmd_file)

    for theme in os.listdir("themes"):
        if theme.endswith(".json"):
            themeJson = json.load(open(f"themes/{theme}"))
            if "consolecolour" not in themeJson:
                themeJson["consolecolour"] = "#3B79FF"
            if "consolemode" not in themeJson:
                themeJson["consolemode"] = "new"
            if "embedlargeimage" not in themeJson:
                themeJson["embedlargeimage"] = "https://ghost.cool/assets/animatedbanner.gif"
            json.dump(themeJson, open(f"themes/{theme}", "w"), sort_keys=False, indent=4)    

    update_config()

    CONFIG = json.load(open("config.json"))
    GIVEAWAYBOTS = json.load(codecs.open("giveawaybots.json", encoding="UTF-8"))

    __token__ = CONFIG["token"]
    __prefix__ = CONFIG["prefix"]
    # __loadonstartup__ = CONFIG["load_on_startup"]
    __deletetimeout__ = CONFIG["delete_timeout"]
    __theme__ = CONFIG["theme"]
    __sounds__ = CONFIG["sounds"]
    __riskmode__ = CONFIG["riskmode"]

    __nitrosniper__ = CONFIG["snipers"]["nitro"]
    __privnotesniper__ = CONFIG["snipers"]["privnote"]
    __giveawaysniper__ = CONFIG["snipers"]["giveaway"]
    __giveawaysniperui__ = CONFIG["giveaway_sniper_ui"]
    __ticketsniper__ = CONFIG["snipers"]["tickets"]

    __nitrowebhook__ = CONFIG["webhooks"]["nitro"]
    __privnotewebhook__ = CONFIG["webhooks"]["privnote"]
    __giveawaywebhook__ = CONFIG["webhooks"]["giveaway"]
    __ghostpingwebhook__ = CONFIG["webhooks"]["ghostping"]
    __friendsupdatewebhook__ = CONFIG["webhooks"]["friendsupdate"]
    __dmtypingwebhook__ = CONFIG["webhooks"]["dmtyping"]
    __guildleavewebhook__ = CONFIG["webhooks"]["guildleave"]
    __selfbotwebhook__ = CONFIG["webhooks"]["selfbot"]
    __ticketswebhook__ = CONFIG["webhooks"]["tickets"]    

    __giveawayjoindelay__ = CONFIG["giveaway_join_delay"]

    __custommotd__ = CONFIG["motd"]["custom"]
    __custommotdtext__ = CONFIG["motd"]["custom_text"]

    __selfbotdetect__ = CONFIG["detections"]["selfbot"]
    __ghostpingdetect__ = CONFIG["detections"]["ghostping"]
    __bandetect__ = CONFIG["detections"]["bans"]
    __deletedmessagesdetect__ = CONFIG["detections"]["deletedmessages"]
    __webhookmodificationdetect__ = CONFIG["detections"]["webhookmodification"]
    __friendsupdatedetect__ = CONFIG["detections"]["friendsupdate"]
    __dmtypingdetect__ = CONFIG["detections"]["dmtyping"]
    __guildleavedetect__ = CONFIG["detections"]["guildleave"]

    THEME = json.load(open(f"themes/{__theme__}.json"))

    __embedtitle__ = THEME["embedtitle"]
    __embedcolour__ = int(THEME["embedcolour"].replace('#', '0x'), 0)
    __embedcolourraw__ = THEME["embedcolour"]
    __embedfooter__ = THEME["embedfooter"]
    __embedemoji__ = THEME["globalemoji"]
    __embedimage__ = THEME["embedimage"]
    __embedlargeimage__ = THEME["embedlargeimage"]
    __embedfooterimage__ = THEME["embedfooterimage"]
    __embedmode__ = CONFIG["embed_mode"]
    __consolemode__ = THEME["consolemode"]

    __ignoredservers__ = CONFIG["ignored_servers"]

    __consolecolour__ = THEME["consolecolour"]
    __ghostloaded__ = False

    __guildleaveignoredservers__ = CONFIG["ignored_servers"]["guildleave"]

    nsfwTypes = ["boobs", "ass", "hentai", "porngif", "pussy", "tits", "tittydrop", "tittypop", "titty", "femboy"]
    now = datetime.now()
    fake = Faker()
    def getCurrentTime():
        return datetime.now().strftime("%H:%M:%S")
    def print_important(message):
        print(f"{printSpaces}{fg.cGrey}[{getCurrentTime()}] {fg.cPurple}[IMPORTANT] {fg.cWhite}{message}")    
    def print_info(message):
        print(f"{printSpaces}{fg.cGrey}[{getCurrentTime()}] {fg.cYellow}[INFORMATION] {fg.cWhite}{message}")
    def print_cmd(command):
        print(f"{printSpaces}{fg.cGrey}[{getCurrentTime()}] {fg.consoleColour}[COMMAND] {fg.cWhite}{command}")
    def print_sharecmd(author, command):
        print(f"{printSpaces}{fg.cGrey}[{getCurrentTime()}] {fg.consoleColour}[SHARE COMMAND] {fg.cWhite}({author}) {command}")
    def print_error(error):
        print(f"{printSpaces}{fg.cGrey}[{getCurrentTime()}] {fg.cRed}[ERROR] {fg.cWhite}{error}")
    def print_detect(message):
        print(f"{printSpaces}{fg.cGrey}[{getCurrentTime()}] {fg.cPink}[DETECT] {fg.cWhite}{message}")
    def print_sniper(message):
        print(f"{printSpaces}{fg.cGrey}[{getCurrentTime()}] {fg.cOrange}[SNIPER] {fg.cWhite}{message}")
    def print_sniper_info(firstmessage, secondmessage):
        spaces = ""
        # for i in range(len(f"[{getCurrentTime()}]")):
        #     spaces += " "
        print(f"{printSpaces}{spaces} {fg.cYellow}{firstmessage}: {fg.cGrey}{secondmessage}")
    def is_me(m):
        return m.author == Ghost.user
    def restart_bot():
        python = sys.executable
        os.execl(python, python, * sys.argv)
    def close_bot():
        os.system("taskkill /IM Ghost.exe")
    def is_windows():
        return os.name == "nt"
    def is_linux():
        return os.name == "posix"
    def GetUUID():
        if is_windows():
            cmd = 'wmic csproduct get uuid'
            uuid = str(subprocess.check_output(cmd))
            pos1 = uuid.find("\\n")+2
            uuid = uuid[pos1:-15]
        elif is_linux():
            uuid = str(subprocess.Popen(["dmidecode", "-s", "system-uuid"], stdout=subprocess.PIPE).communicate()[0]).replace("b'", "").replace("\\n'", "")
        return uuid
    # Found: https://stackoverflow.com/a/64676639
    def hex_to_rgb(hex_string):
        r_hex = hex_string[1:3]
        g_hex = hex_string[3:5]
        b_hex = hex_string[5:7]

        red = int(r_hex, 16)
        green = int(g_hex, 16)
        blue = int(b_hex, 16)

        return red, green, blue
    def get_nsfw(type):
        types = nsfwTypes
        if type not in types:
            return "Invalid type."
        else:
            for type2 in types:
                if type == type2:
                    request = requests.get(f"https://www.reddit.com/r/{type2}/random.json", headers={'User-agent': get_random_user_agent()}).json()
                    url = request[0]["data"]["children"][0]["data"]["url"]
                    if "redgifs" in str(url):
                        url = request[0]["data"]["children"][0]["data"]["preview"]["reddit_video_preview"]["fallback_url"]
                    return url
    def get_nsfw_custom_type(type):
        request = requests.get(f"https://www.reddit.com/r/{type}/random.json", headers={'User-agent': get_random_user_agent()}).json()
        url = request[0]["data"]["children"][0]["data"]["url"]
        if "redgifs" in str(url):
            url = request[0]["data"]["children"][0]["data"]["preview"]["reddit_video_preview"]["fallback_url"]
        return url    
    def send_notification(title, message, duration):
        try:
            plyer.notification.notify(
                title=title,
                message=message,
                app_name="Ghost",
                app_icon="icon.ico",
                timeout=duration,
                toast=True
            )

        except:
            pass   
    def claim_nitro(code, userToken):
        URL = f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem'
        result = requests.post(URL, headers={'Authorization': userToken}).text
        if 'nitro' in result:
            return "Valid Code"
        else:
            return "Invalid Code"
    def read_privnote(url):
        content = pn.read_note(link=url)
        return content
    def get_random_user_agent():
        userAgents = ["Mozilla/5.0 (Windows NT 6.2;en-US) AppleWebKit/537.32.36 (KHTML, live Gecko) Chrome/56.0.3075.83 Safari/537.32", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 8.0; WOW64) AppleWebKit/536.24 (KHTML, like Gecko) Chrome/32.0.2019.89 Safari/536.24", "Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.41 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2599.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.139 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/67.0.3387.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.355.0 Safari/533.3", "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.4 Safari/532.0", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3057.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36 TC2", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2531.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2264.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2714.0 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1864.6 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Avast/70.0.917.102", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1615.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3608.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2427.7 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.61 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.104 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) Chrome/27.0.1453 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.45 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.45", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.102 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2419.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.68 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.114 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64; 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/17.0.1410.63 Safari/537.31", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2583.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/536.36 (KHTML, like Gecko) Chrome/67.2.3.4 Safari/536.36", "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.69 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36 EdgA/41.0.0.1662", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1"]
        userAgent = random.choice(userAgents)
        return userAgent
    def avatarUrl(id, avatar):
        url = ""
        if not str(avatar).startswith("http"):
            if str(avatar).startswith("a_"):
                url =  f"https://cdn.discordapp.com/avatars/{id}/{avatar}.gif?size=1024"
            else:
                url =  f"https://cdn.discordapp.com/avatars/{id}/{avatar}.png?size=1024"

            return url
        else:
            return avatar
    def iconUrl(id, icon):
        url = ""
        if str(icon).startswith("a_"):
            url = f"https://cdn.discordapp.com/avatars/{id}/{icon}.gif?size=1024"
        else:
            url = f"https://cdn.discordapp.com/avatars/{id}/{icon}.png?size=1024"   
        return icon

    def resource_path(relative_path):
        # try:
        #     base_path = sys._MEIPASS
        # except Exception:
        #     base_path = os.path.abspath(".")

        # return os.path.join(base_path, relative_path)
        return relative_path
    def get_friends(token):
        request = requests.get("https://discord.com/api/users/@me/relationships", headers={"Authorization": token})
        json = request.json()
        friends = []
        for item in json:
            if item["type"] == 1:
                friends.append(item["user"])
        return friends

    class Config():
        def __init__(self):
            self.json = json.load(open("config.json"))
            self.token = self.json["token"]
            self.prefix = self.json["prefix"]
            self.deleteTimeout = self.json["delete_timeout"]
            self.theme = self.json["theme"]
            self.giveawayJoinDelay = self.json["giveaway_join_delay"]

        def getConfig():
            return json.load(open("config.json"))

        def saveConfig(data):
            return json.dump(data, open("config.json", "w"), indent=4, sort_keys=False)

        def changeToken(newToken):
            global __token__
            __token__ = newToken
            cfg = Config.getConfig()
            cfg["token"] = newToken
            Config.saveConfig(cfg)
        def changePrefix(newPrefix):
            global __prefix__
            __prefix__ = newPrefix
            Ghost.command_prefix = newPrefix
            cfg = Config.getConfig()
            cfg["prefix"] = newPrefix
            Config.saveConfig(cfg)
        def changeDeleteTimeout(newDeleteTimeout: int):
            global __deletetimeout__
            __deletetimeout__ = newDeleteTimeout
            cfg = Config.getConfig()
            cfg["delete_timeout"] = newDeleteTimeout
            Config.saveConfig(cfg)
        def changeGiveawayJoinDelay(newJoinDelay: int):
            global __giveawayjoindelay__
            __giveawayjoindelay__ = newJoinDelay
            cfg = Config.getConfig()
            cfg["giveaway_join_delay"] = newJoinDelay
            Config.saveConfig(cfg)
        def changeTheme(newTheme):
            global __embedtitle__, __embedcolour__, __embedfooter__, __embedemoji__, __embedimage__, __embedfooterimage__, __embedcolourraw__, __theme__, __embedlargeimage__
            __embedtitle__ = json.load(open(f"themes/{newTheme}.json"))["embedtitle"]
            __embedcolour__ = int(json.load(open(f"themes/{newTheme}.json"))["embedcolour"].replace('#', '0x'), 0)
            __embedcolourraw__ = json.load(open(f"themes/{newTheme}.json"))["embedcolour"]
            __embedfooter__ = json.load(open(f"themes/{newTheme}.json"))["embedfooter"]
            __embedemoji__ = json.load(open(f"themes/{newTheme}.json"))["globalemoji"]
            __embedimage__ = json.load(open(f"themes/{newTheme}.json"))["embedimage"]
            __embedfooterimage__ = json.load(open(f"themes/{newTheme}.json"))["embedfooterimage"]
            __embedlargeimage__ = json.load(open(f"themes/{newTheme}.json"))["embedlargeimage"]
            __theme__ = newTheme
            cfg = Config.getConfig()
            cfg["theme"] = newTheme
            Config.saveConfig(cfg)

    ccolourred, ccolourgreen, ccolourblue = hex_to_rgb(__consolecolour__)
    fg.consoleColour = Style(RgbFg(ccolourred, ccolourgreen, ccolourblue))

    fg.cRed = Style(RgbFg(255, 81, 69))
    fg.cOrange = Style(RgbFg(255, 165, 69))
    fg.cYellow = Style(RgbFg(255, 255, 69))
    fg.cGreen = Style(RgbFg(35, 222, 57))
    fg.cBlue = Style(RgbFg(69, 119, 255))
    fg.cPurple = Style(RgbFg(177, 69, 255))
    fg.cPink = Style(RgbFg(255, 69, 212))

    fg.cGrey = Style(RgbFg(207, 207, 207))
    fg.cBrown = Style(RgbFg(199, 100, 58))
    fg.cBlack = Style(RgbFg(0, 0, 0))
    fg.cWhite = Style(RgbFg(255, 255, 255))

    if is_windows():
        os.system("cls")
        os.system(f"title Ghost")
    elif is_linux():
        os.system("clear")

    if requests.get("https://discord.com/api/users/@me/settings", headers={"Authorization": __token__}).status_code == 200:
        status = requests.get("https://discord.com/api/users/@me/settings", headers={"Authorization": __token__}).json()["status"]
    else:
        status = "online"
    Ghost = commands.Bot(command_prefix=__prefix__, self_bot=True, status=discord.Status.try_value(status))
    Ghost.remove_command('help')
    Ghost.launch_time = datetime.utcnow()
    botStartTime = time.time()

    giveawayBots = []
    for index in GIVEAWAYBOTS:
        giveawayBots.append(int(index))

    version = "2.3.7"
    cycleStatusText = ""
    cycleStatus = False
    discordServer = "discord.gg/reKgzfRrpt"
    uwuifyEnabled = False
    channelBlankChar = "᲼"
    spammingMessages = False
    rickRollEnabled = False
    nukingToken = False
    consoleMode = __consolemode__
    consoleModes = ["new", "new2", "new3", "new4", "bear", "old", "react", "rise", "nighty", "rainbow"]
    scriptsList = []
    afkMode = CONFIG["afkmode"]["enabled"]

    def include(filename):
        global scriptsList
        if os.path.exists(filename):
            scriptsList.append(filename)
            exec(codecs.open(filename, encoding="utf-8").read(), globals(), locals())

    # hideText = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
    
    if not __custommotd__:
        motd = "Developed by Benny | Discontinued October 2021"
    else:
        motd = __custommotdtext__

    @Ghost.event
    async def on_connect():
        if str(sounddevice.query_devices()) != "":
            pygame.mixer.init()
        width = os.get_terminal_size().columns

        if is_windows():
            os.system("cls")
            os.system(f"title Ghost [{version}] [{Ghost.user}]")

        # if is_windows():
        #     def startupPath():
        #         return str(shell.SHGetFolderPath(0, (shellcon.CSIDL_STARTUP, shellcon.CSIDL_COMMON_STARTUP)[0], None, 0))

        #     os.system("cls")
        #     os.system(f"title Ghost [{version}] [{Ghost.user}]")
            
        #     if (CONFIG["load_on_startup"] == True):
        #         print("Adding to startup.......")
        #         USER_NAME = getpass.getuser()

        #         def add_to_startup(file_path=""):
        #             if file_path == "":
        #                 file_path = os.path.dirname(os.path.realpath(__file__))
                    
        #             bat_file = open(startupPath() + r"\\Ghost.bat", "w")
        #             bat_file.write(f"cd {file_path}\nstart Ghost")   
        #             bat_file.close()

        #         add_to_startup()   

        #     else:
        #         print("Removing from startup......")
        #         if os.path.exists(startupPath() + r"\\Ghost.bat"): os.remove(startupPath() + r"\\Ghost.bat");

        #     os.system("cls")
        if is_linux():
            os.system("clear")
        if consoleMode.lower() == "new":
            print("")
            print(fg.consoleColour + "")                    
            print(" ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗".center(width))
            print("██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝".center(width))
            print("██║  ███╗███████║██║   ██║███████╗   ██║   ".center(width))
            print("██║   ██║██╔══██║██║   ██║╚════██║   ██║   ".center(width))
            print("╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ".center(width))
            print(" ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ".center(width))
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")  
        if consoleMode.lower() == "rainbow":
            print("")
            print(fg.consoleColour + "")                    
            print(fg.cRed + " ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗".center(width))
            print(fg.cOrange + "██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝".center(width))
            print(fg.cYellow + "██║  ███╗███████║██║   ██║███████╗   ██║   ".center(width))
            print(fg.cGreen + "██║   ██║██╔══██║██║   ██║╚════██║   ██║   ".center(width))
            print(fg.cBlue + "╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ".center(width))
            print(fg.cPurple + " ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ".center(width))
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")                                       
        if consoleMode.lower() == "new2":
            print("")
            print(fg.consoleColour + "")                    
            print(" ______     __  __     ______     ______     ______  ".center(width))
            print("/\  ___\   /\ \_\ \   /\  __ \   /\  ___\   /\__  _\ ".center(width))
            print("\ \ \__ \  \ \  __ \  \ \ \/\ \  \ \___  \  \/_/\ \/ ".center(width))
            print(" \ \_____\  \ \_\ \_\  \ \_____\  \/\_____\    \ \_\ ".center(width))
            print("  \/_____/   \/_/\/_/   \/_____/   \/_____/     \/_/ ".center(width))
            print("                                                     ".center(width)) 
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")                      
        if consoleMode.lower() == "new3":
            print("")
            print(fg.consoleColour + "")                    
            print("            88                                         ".center(width))
            print("            88                                  ,d     ".center(width))
            print("            88                                  88     ".center(width))
            print(" ,adPPYb,d8 88,dPPYba,   ,adPPYba,  ,adPPYba, MM88MMM  ".center(width))
            print('a8"    `Y88 88P\'    "8a a8"     "8a I8[    ""   88     '.center(width))
            print('8b       88 88       88 8b       d8  `"Y8ba,    88     '.center(width))                       
            print('"8a,   ,d88 88       88 "8a,   ,a8" aa    ]8I   88,    '.center(width))                       
            print(' `"YbbdP"Y8 88       88  `"YbbdP"\'  `"YbbdP"\'   "Y888  '.center(width))                       
            print(' aa,    ,88                                            '.center(width))                       
            print('  "Y8bbdP"                                             '.center(width))  
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")                    
        if consoleMode.lower() == "new4":
            print("")
            print(fg.consoleColour + "")                    
            print("   ▄██████▄     ▄█    █▄     ▄██████▄     ▄████████     ███     ".center(width))
            print("  ███    ███   ███    ███   ███    ███   ███    ███ ▀█████████▄ ".center(width))
            print("  ███    █▀    ███    ███   ███    ███   ███    █▀     ▀███▀▀██ ".center(width))
            print(" ▄███         ▄███▄▄▄▄███▄▄ ███    ███   ███            ███   ▀ ".center(width))
            print('▀▀███ ████▄  ▀▀███▀▀▀▀███▀  ███    ███ ▀███████████     ███     '.center(width))
            print('  ███    ███   ███    ███   ███    ███          ███     ███     '.center(width))                       
            print('  ███    ███   ███    ███   ███    ███    ▄█    ███     ███     '.center(width))                       
            print('  ████████▀    ███    █▀     ▀██████▀   ▄████████▀     ▄████▀   '.center(width))         
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")                                                                              
        if consoleMode.lower() == "bear":
            if is_windows():
                os.system("mode con: cols=90 lines=24")                    
            print("")
            print(fg.consoleColour + "")                    
            print("     ▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄      ".center(os.get_terminal_size().columns))
            print("     █▒▒░░░░░░░░░▒▒█      ".center(os.get_terminal_size().columns))
            print("      █░░█░░░░░█░░█       ".center(os.get_terminal_size().columns))
            print("   ▄▄  █░░░▀█▀░░░█   ▄▄   ".center(os.get_terminal_size().columns))
            print("  █░░█ ▀▄░░░░░░░▄▀  █░░█  ".center(os.get_terminal_size().columns))
            print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█".center(os.get_terminal_size().columns))                                      
            print("█░█▀▀░░█ █░░█▀█░░█▀░░▀█▀░█".center(os.get_terminal_size().columns))                                      
            print("█░█▄█░░█▀█░░█▄█░░▄█░░ █ ░█".center(os.get_terminal_size().columns))                                      
            print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█".center(os.get_terminal_size().columns))    
            print("")
            print(fg.cWhite + f"{motd}".center(os.get_terminal_size().columns))
            print(fg.consoleColour + '─'*os.get_terminal_size().columns)
            print("")                                                      
        elif consoleMode.lower() == "old":
            print("")
            print(fg.consoleColour + "")                    
            print("  ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓".center(width))
            print(" ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒".center(width))
            print("▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░".center(width))
            print("░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░ ".center(width))
            print("░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ ".center(width))
            print(" ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ".center(width))                    
            print("  ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░    ".center(width))                    
            print("░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░      ".center(width))                    
            print("      ░  ░  ░  ░    ░ ░        ░           ".center(width))  
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")                    
        elif consoleMode not in consoleModes:
            print("")
            print(fg.consoleColour + "")                    
            print(" ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗".center(width))
            print("██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝".center(width))
            print("██║  ███╗███████║██║   ██║███████╗   ██║   ".center(width))
            print("██║   ██║██╔══██║██║   ██║╚════██║   ██║   ".center(width))
            print("╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ".center(width))
            print(" ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ".center(width))                                      
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")
        if consoleMode.lower() == "react":
            print("")
            print(fg.consoleColour + "")                    
            print("██████╗ ███████╗ █████╗  ██████╗████████╗".center(width))
            print("██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝".center(width))
            print("██████╔╝█████╗  ███████║██║        ██║   ".center(width))
            print("██╔══██╗██╔══╝  ██╔══██║██║        ██║   ".center(width))
            print("██║  ██║███████╗██║  ██║╚██████╗   ██║   ".center(width))
            print("╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ".center(width))
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")  
        if consoleMode.lower() == "rise":
            print(fg.cBlue + "")                    
            print("██████╗ ██╗███████╗███████╗    ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗".center(width))
            print("██╔══██╗██║██╔════╝██╔════╝    ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝".center(width))
            print("██████╔╝██║███████╗█████╗      ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   ".center(width))
            print("██╔══██╗██║╚════██║██╔══╝      ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   ".center(width))
            print("██║  ██║██║███████║███████╗    ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   ".center(width))
            print("╚═╝  ╚═╝╚═╝╚══════╝╚══════╝    ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   ".center(width))
            print("╭─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╮")
            print(fg.cGrey + f"Connected: {Ghost.user} | Prefix: {Ghost.command_prefix} | Servers: {len(Ghost.guilds)}".center(width))
            print(fg.cBlue + "╰─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╯")
            print("")
            print(fg.cBlue + '━'*width)
            print("")         

        if consoleMode.lower() == "nighty":
            if is_windows():
                os.system("mode con: cols=90 lines=24")
            print("")                    
            print(f"                     {fg.cWhite}███{fg.consoleColour}╗   {fg.cWhite}██{fg.consoleColour}╗{fg.cWhite}██{fg.consoleColour}╗ {fg.cWhite}██████{fg.consoleColour}╗ {fg.cWhite}██{fg.consoleColour}╗  {fg.cWhite}██{fg.consoleColour}╗{fg.cWhite}████████{fg.consoleColour}╗{fg.cWhite}██{fg.consoleColour}╗   {fg.cWhite}██{fg.consoleColour}╗")
            print(f"                     {fg.cWhite}████{fg.consoleColour}╗  {fg.cWhite}██{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}╔════╝ {fg.cWhite}██{fg.consoleColour}║  {fg.cWhite}██{fg.consoleColour}║╚══{fg.cWhite}██{fg.consoleColour}╔══╝╚{fg.cWhite}██{fg.consoleColour}╗ {fg.cWhite}██{fg.consoleColour}╔╝")
            print(f"                     {fg.cWhite}██{fg.consoleColour}╔{fg.cWhite}██{fg.consoleColour}╗ {fg.cWhite}██{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}║  {fg.cWhite}███{fg.consoleColour}╗{fg.cWhite}███████{fg.consoleColour}║   {fg.cWhite}██{fg.consoleColour}║    ╚{fg.cWhite}████{fg.consoleColour}╔╝ ")
            print(f"                     {fg.cWhite}██{fg.consoleColour}║╚{fg.cWhite}██{fg.consoleColour}╗{fg.cWhite}██{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}║   {fg.cWhite}██{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}╔══{fg.cWhite}██{fg.consoleColour}║   {fg.cWhite}██{fg.consoleColour}║     ╚{fg.cWhite}██{fg.consoleColour}╔╝  ")
            print(f"                     {fg.cWhite}██{fg.consoleColour}║ ╚{fg.cWhite}████{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}║╚{fg.cWhite}██████{fg.consoleColour}╔╝{fg.cWhite}██{fg.consoleColour}║  {fg.cWhite}██{fg.consoleColour}║   {fg.cWhite}██{fg.consoleColour}║      {fg.cWhite}██{fg.consoleColour}║   ")
            print(fg.consoleColour + f"                     ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ")
            print("")
            print(f"{fg.cWhite}Status:    {fg.cGreen}Connected")
            print(f"{fg.cWhite}Account:   {Ghost.user} [{len(Ghost.guilds)} servers] [{len(get_friends(__token__))} friends]")
            print(f"{fg.cWhite}Prefix:    {Ghost.command_prefix}")
            print(fg.cWhite + '─'*os.get_terminal_size().columns)                                                          

            # def getCurrentTime():
            #     return datetime.now().strftime("%H:%M")
            # def print_important(message):
            #     print(f"{fg.cGrey}{getCurrentTime()} | {fg.cPurple}[Important] {fg.cGrey} | {message}")    
            # def print_info(message):
            #     print(f"{fg.cGrey}{getCurrentTime()} | {fg.cYellow}[Information] {fg.cGrey} | {message}")
            # def print_cmd(command):
            #     print(f"{fg.cGrey}{getCurrentTime()} | {fg.consoleColour}[Command] {fg.cGrey} | {Ghost.command_prefix}{command}")
            # def print_sharecmd(author, command):
            #     print(f"{fg.cGrey}[{getCurrentTime()}] {fg.consoleColour}[SHARE COMMAND] {fg.cWhite}({author}) {command}")
            # def print_error(error):
            #     print(f"{fg.cGrey}{getCurrentTime()} | {fg.cRed}[Error] {fg.cGrey} | {error}")
            # def print_detect(message):
            #     print(f"{fg.cGrey}{getCurrentTime()} | {fg.cPink}[Detect] {fg.cGrey} | {message}")
            # def print_sniper(message):
            #     print(f"{fg.cGrey}{getCurrentTime()} | {fg.cOrange}[Sniper] {fg.cGrey} | {message}")
            # def print_sniper_info(firstmessage, secondmessage):
            #     print(f"{fg.cGrey}{getCurrentTime()} | {fg.cOrange}[Sniper] {fg.cGrey} | {firstmessage} | {secondmessage}")


        if "beta" in version.lower():
            print_important("You're currently using a beta build of Ghost.")
            print_important("If you notice any bugs please report them to the developer.")
            print(" ")
        elif "dev" in version.lower():
            print_important("You're currently using a developer build of Ghost.")
            print_important("If you notice any bugs please report them to the developer.")
            print(" ")                

        if not os.path.isfile('data/logins.txt'):
            message = "1"
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            f = open('data/logins.txt', "w")
            f.write(base64_message)
            f.close()
        else:
            f = open('data/logins.txt', "r")
            loginsdata = f.read()
            base64_message = loginsdata
            base64_bytes = base64_message.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('ascii')
            logindata = int(message)+1
            logindata_str = str(logindata)
            logindata_bytes = logindata_str.encode('ascii')
            base64_bytes = base64.b64encode(logindata_bytes)
            base64_logindata = base64_bytes.decode('ascii')
            f = open('data/logins.txt', "w")
            f.write(f"{base64_logindata}")
            f.close()                  
            
        print_info(f"Ghost can now be used with {Ghost.command_prefix} prefix.")
        send_notification("Ghost", "Successfully connected!", 10)  
        global __ghostloaded__
        __ghostloaded__ = True
        if __sounds__:
            if str(sounddevice.query_devices()) != "":
                pygame.mixer.music.load(resource_path("sounds/connected.mp3"))
                pygame.mixer.music.play(1)                    

        if json.load(open("richpresence.json"))["enabled"] == True:
            def readyCallback(current_user): 
                print(f"{printSpaces}{fg.cGrey}[{getCurrentTime()}] {fg.cBlue}[RPC] {fg.cWhite}Discord rich presence has been enabled.")
            def disconnectedCallback(codeno, codemsg): 
                print(f"{printSpaces}{fg.cGrey}[{getCurrentTime()}] {fg.cBlue}[RPC] {fg.cWhite}Discord rich presence has been disabled.")
            def errorCallback(errno, errmsg): 
                print(f"{printSpaces}{fg.cGrey}[{getCurrentTime()}] {fg.cBlue}[RPC] {fg.cWhite}An error happend.")

            callbacks = {'ready': readyCallback,'disconnected': disconnectedCallback,'error': errorCallback}
            discord_rpc.initialize(str(json.load(open("richpresence.json"))["client_id"]), callbacks=callbacks, log=False)

            for i in range(10):
                discord_rpc.update_presence(**{
                    'details': json.load(open("richpresence.json"))["details"].replace("{version}", version),
                    'state': json.load(open("richpresence.json"))["state"].replace("{version}", version),
                    'start_timestamp': time.time(),
                    'large_image_key': json.load(open("richpresence.json"))["large_image_key"],
                    'large_image_text': json.load(open("richpresence.json"))["large_image_text"],
                    'small_image_key': json.load(open("richpresence.json"))["small_image_key"],
                    'small_image_text': json.load(open("richpresence.json"))["small_image_text"]
                })
                discord_rpc.update_connection()     
                await asyncio.sleep(2)
                discord_rpc.run_callbacks() 

    async def get_message(ctx, id):
        channelMsgHistory = await ctx.channel.history(limit=999999999).flatten()
        for message in channelMsgHistory:
            if message.id == id:
                msg = message
                return msg

    @Ghost.event
    async def on_error(event):
        logging.error(str(event))

    @Ghost.event
    async def on_command(ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        print_cmd(f"{ctx.command.name}")

    @Ghost.event
    async def on_command_error(ctx, error):
        logging.error(str(error))
        if isinstance(error, commands.CommandNotFound):
            try:
                await ctx.message.delete()
            except:
                pass
        
        else:
            print_error(f"{error}")
            try:
                await ctx.message.delete()
            except:
                pass            

    @Ghost.event
    async def on_message_delete(message):
        if __ghostloaded__:
            if __deletedmessagesdetect__:
                if message.guild.id not in __ignoredservers__["deletedmessages"]:
                    print_detect("Deleted Message")
                    print_sniper_info("Content", message.content)
                    print_sniper_info("Author", str(message.author))
                    try:
                        print_sniper_info("Channel", str(message.channel))
                    except:
                        pass
                    try:
                        print_sniper_info("Guild", str(message.guild.name))
                    except:
                        pass  

            if __ghostpingdetect__:
                if Ghost.user.mentioned_in(message):
                    if message.guild.id not in __ignoredservers__["ghostpings"]:
                        print_detect("Ghost Ping")
                        print_sniper_info("Content", str(message.content))
                        print_sniper_info("Author", str(message.author))
                        try:
                            print_sniper_info("Channel", str(message.channel))
                        except:
                            pass
                        try:
                            print_sniper_info("Guild", str(message.guild.name))
                        except:
                            pass   
                        if __sounds__:   
                            if str(sounddevice.query_devices()) != "":          
                                pygame.mixer.music.load(resource_path("sounds/notification.mp3"))
                                pygame.mixer.music.play(1)                        
                        send_notification("Ghost Ping", f"You were ghost pinged in {message.guild} by {message.author}.", 10)
                        if __ghostpingwebhook__ != "":
                            webhook = DiscordWebhook(url=__ghostpingwebhook__)
                            embed = DiscordEmbed(title='Ghost Ping', color=__embedcolourraw__[1:], description=f"`{message.author}` ghost pinged you in `{message.channel}` (`{message.guild}`)")
                            embed.set_thumbnail(url=__embedimage__)
                            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                            embed.set_timestamp()
                            webhook.add_embed(embed)
                            response = webhook.execute()                        

    @Ghost.event
    async def on_member_ban(guild, user):
        if __ghostloaded__:
            if __bandetect__:
                if guild.id not in __ignoredservers__["bans"]:
                    print_detect("Banned")
                    print_sniper_info("Member", f"{user}")
                    print_sniper_info("Member ID", f"{user.id}")
                    print_sniper_info("Guild", f"{guild.name}")    
                if str(Ghost.user) == str(user):
                    if __sounds__:   
                        if str(sounddevice.query_devices()) != "":          
                            pygame.mixer.music.load(resource_path("sounds/notification.mp3"))
                            pygame.mixer.music.play(1)  
                    send_notification("Ban Detect", f"You were banned in {guild.name}.", 10)                                          

    @Ghost.event
    async def on_guild_remove(guild):
        if __ghostloaded__:
            if __guildleavedetect__:
                if guild.id not in __guildleaveignoredservers__:
                    print_detect("Guild Left")
                    print_sniper_info("Name", guild.name)
                    print_sniper_info("ID", guild.id)
                    print_sniper_info("Owner", guild.owner)

                    if __guildleavewebhook__ != "":
                        webhook = DiscordWebhook(url=__guildleavewebhook__)
                        embed = DiscordEmbed(title='Guild Leave Detection', color=__embedcolourraw__[1:])
                        embed.set_thumbnail(url=__embedimage__)
                        embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                        embed.set_timestamp()
                        embed.add_embed_field(name='Name', value=str(guild.name), inline=False)
                        embed.add_embed_field(name='ID', value=str(guild.id), inline=False)
                        embed.add_embed_field(name='Owner', value=str(guild.owner), inline=False)
                        webhook.add_embed(embed)
                        response = webhook.execute()                        

    @Ghost.event
    async def on_webhooks_update(channel):
        if __ghostloaded__:
            if __webhookmodificationdetect__:
                if channel.guild.id not in __ignoredservers__["webhookmodifications"]:
                    print_detect("Webhook Modification")
                    try:
                        print_sniper_info("Server", channel.guild.name)
                    except:
                        pass
                    try:
                        print_sniper_info("Channel", channel.name)
                    except:
                        pass

    @Ghost.event
    async def on_relationship_add(relationship):
        if __ghostloaded__:
            if __friendsupdatedetect__:
                if isinstance(relationship.type, discord.RelationshipType.incoming_request):
                    print_detect("Incoming Friend Request")
                    print_sniper_info("User", relationship.user.name + "#" + relationship.user.discriminator)
                    print_sniper_info("ID", relationship.user.id)
                    if __friendsupdatewebhook__ != "":
                        webhook = DiscordWebhook(url=__friendsupdatewebhook__)
                        embed = DiscordEmbed(title='Incoming Friend Request', color=__embedcolourraw__[1:])
                        embed.set_thumbnail(url=__embedimage__)
                        embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                        embed.set_timestamp()
                        embed.add_embed_field(name='User', value=relationship.user.name + "#" + relationship.user.discriminator, inline=False)
                        embed.add_embed_field(name='ID', value=str(relationship.user.id), inline=False)
                        webhook.add_embed(embed)
                        response = webhook.execute()                              
                if isinstance(relationship.type, discord.RelationshipType.friend):
                    print_detect("New Friend")
                    print_sniper_info("User", relationship.user.name + "#" + relationship.user.discriminator)
                    print_sniper_info("ID", relationship.user.id)    
                    if __friendsupdatewebhook__ != "":
                        webhook = DiscordWebhook(url=__friendsupdatewebhook__)
                        embed = DiscordEmbed(title='Incoming Friend Request', color=__embedcolourraw__[1:])
                        embed.set_thumbnail(url=__embedimage__)
                        embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                        embed.set_timestamp()
                        embed.add_embed_field(name='User', value=relationship.user.name + "#" + relationship.user.discriminator, inline=False)
                        embed.add_embed_field(name='ID', value=str(relationship.user.id), inline=False)
                        webhook.add_embed(embed)
                        response = webhook.execute()                                                 

    @Ghost.event
    async def on_relationship_remove(relationship):
        if __ghostloaded__:
            if __friendsupdatedetect__:
                if isinstance(relationship.type, discord.RelationshipType.outgoing_request):
                    print_detect("Outgoing Friend Request")
                    print_sniper_info("User", relationship.user.name + "#" + relationship.user.discriminator)
                    print_sniper_info("ID", relationship.user.id)
                    if __friendsupdatewebhook__ != "":
                        webhook = DiscordWebhook(url=__friendsupdatewebhook__)
                        embed = DiscordEmbed(title='Outgoing Friend Request', color=__embedcolourraw__[1:])
                        embed.set_thumbnail(url=__embedimage__)
                        embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                        embed.set_timestamp()
                        embed.add_embed_field(name='User', value=relationship.user.name + "#" + relationship.user.discriminator, inline=False)
                        embed.add_embed_field(name='ID', value=str(relationship.user.id), inline=False)
                        webhook.add_embed(embed)
                        response = webhook.execute()                             
                if isinstance(relationship.type, discord.RelationshipType.blocked):
                    print_detect("Blocked User")
                    print_sniper_info("User", relationship.user.name + "#" + relationship.user.discriminator)
                    print_sniper_info("ID", relationship.user.id)        
                    if __friendsupdatewebhook__ != "":
                        webhook = DiscordWebhook(url=__friendsupdatewebhook__)
                        embed = DiscordEmbed(title='Blocked User', color=__embedcolourraw__[1:])
                        embed.set_thumbnail(url=__embedimage__)
                        embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                        embed.set_timestamp()
                        embed.add_embed_field(name='User', value=relationship.user.name + "#" + relationship.user.discriminator, inline=False)
                        embed.add_embed_field(name='ID', value=str(relationship.user.id), inline=False)
                        webhook.add_embed(embed)
                        response = webhook.execute()                                             
                if isinstance(relationship.type, discord.RelationshipType.friend):
                    print_detect("Removed Friend")
                    print_sniper_info("User", relationship.user.name + "#" + relationship.user.discriminator)
                    print_sniper_info("ID", relationship.user.id) 
                    if __friendsupdatewebhook__ != "":
                        webhook = DiscordWebhook(url=__friendsupdatewebhook__)
                        embed = DiscordEmbed(title='Removed Friend', color=__embedcolourraw__[1:])
                        embed.set_thumbnail(url=__embedimage__)
                        embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                        embed.set_timestamp()
                        embed.add_embed_field(name='User', value=relationship.user.name + "#" + relationship.user.discriminator, inline=False)
                        embed.add_embed_field(name='ID', value=str(relationship.user.id), inline=False)
                        webhook.add_embed(embed)
                        response = webhook.execute()                             

    @Ghost.event
    async def on_typing(channel, user, when):
        if __ghostloaded__:
            if isinstance(channel, discord.DMChannel):
                if __dmtypingdetect__:
                    print_detect(f"DM Typing")
                    print_sniper_info("User", user)
                    if __sounds__:   
                        if str(sounddevice.query_devices()) != "":          
                            pygame.mixer.music.load(resource_path("sounds/notification.mp3"))
                            pygame.mixer.music.play(1)  
                    send_notification("DM Typing", f"{user} is typing in their DMs.", 10)     
                    if __dmtypingwebhook__ != "":
                        webhook = DiscordWebhook(url=__dmtypingwebhook__)
                        embed = DiscordEmbed(title='DM Typing', color=__embedcolourraw__[1:])
                        embed.set_thumbnail(url=__embedimage__)
                        embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                        embed.set_timestamp()
                        embed.add_embed_field(name='User', value=str(user), inline=False)
                        embed.add_embed_field(name='ID', value=str(user.id), inline=False)
                        embed.add_embed_field(name='When', value=str(when), inline=False)
                        webhook.add_embed(embed)
                        response = webhook.execute()                                                         

    @Ghost.event
    async def on_guild_channel_create(channel):
        if __ghostloaded__:
            if __ticketsniper__:
                if "ticket" in channel.name:
                    if channel.guild.id not in __ignoredservers__["tickets"]:
                        if str(channel.type).lower() != "category":
                            request = requests.get(f"https://discord.com/api/channels/{channel.id}", headers={"Authorization": __token__, "User-Agent": get_random_user_agent()})
                            if request.status_code == 200:                        
                                print_sniper("Ticket")
                                try:
                                    print_sniper_info("Server", channel.guild.name)
                                except:
                                    pass
                                try:
                                    print_sniper_info("Channel", channel.name)
                                except:
                                    pass

                                if __sounds__:   
                                    if str(sounddevice.query_devices()) != "":          
                                        pygame.mixer.music.load(resource_path("sounds/notification.mp3"))
                                        pygame.mixer.music.play(1)  
                                send_notification("Ticket Sniper", f"{channel.name} was created in {channel.guild.name}.", 10)       
                                if __ticketswebhook__ != "":
                                    webhook = DiscordWebhook(url=__ticketswebhook__)
                                    embed = DiscordEmbed(title='Ticket', color=__embedcolourraw__[1:])
                                    embed.set_thumbnail(url=__embedimage__)
                                    embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                                    embed.set_timestamp()
                                    try:
                                        embed.add_embed_field(name='Server', value=str(channel.guild.name), inline=False)
                                    except:
                                        pass
                                    try:
                                        embed.add_embed_field(name='Channel', value=str(channel.name), inline=False)
                                    except:
                                        pass
                                    webhook.add_embed(embed)
                                    response = webhook.execute()                                                                 

    @Ghost.event
    async def on_message(message):
        if __ghostloaded__:
            messageSendTime = datetime.now()

            if message.author.id != Ghost.user.id:

                if afkMode:
                    if isinstance(message.channel, discord.DMChannel):
                        await message.channel.send(CONFIG["afkmode"]["replymessage"])

                if __nitrosniper__:
                    if "discord.gift/" in message.content:
                        if message.guild.id not in __ignoredservers__["nitro"]:
                            giftLink = ""
                            code = ""
                            for item in message.content.split(" "):
                                if "discord.gift/" in item:
                                    giftLink = item
                                    code = giftLink.replace("discord.gift/", "")
                            print_sniper("Nitro")
                            print_sniper_info("Link", giftLink)
                            print_sniper_info("Author", message.author)
                            try:
                                print_sniper_info("Server", message.guild.name)
                            except:
                                pass
                            try:
                                print_sniper_info("Channel", message.channel.name)
                            except:
                                pass
                            nitroStatus = claim_nitro(code, __token__)
                            print_sniper_info("Status", nitroStatus)                
                            print_sniper_info("Snipe Speed", str((datetime.now()-messageSendTime).total_seconds()) + "s")

                            if __nitrowebhook__ != "":
                                webhook = DiscordWebhook(url=__nitrowebhook__)
                                embed = DiscordEmbed(title='Nitro Sniper', color=__embedcolourraw__[1:])
                                embed.set_thumbnail(url=__embedimage__)
                                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                                embed.set_timestamp()
                                embed.add_embed_field(name='Author', value=str(message.author), inline=False)
                                embed.add_embed_field(name='Gift Link', value=giftLink, inline=False)
                                embed.add_embed_field(name='Nitro Status', value=nitroStatus, inline=False)
                                embed.add_embed_field(name='Jump to message', value=f"[Click Here!]({message.jump_url})", inline=False)
                                webhook.add_embed(embed)
                                response = webhook.execute()

                            if nitroStatus == "Valid Code":
                                if __sounds__:
                                    if str(sounddevice.query_devices()) != "":
                                        pygame.mixer.music.load(resource_path("sounds/notification.mp3"))
                                        pygame.mixer.music.play(1)

                                send_notification("Nitro Sniper", "Sniped a nitro gift code!", 10)                                

                if __privnotesniper__:
                    if "privnote.com/" in message.content:
                        if message.guild.id not in __ignoredservers__["privnote"]:
                            privnoteLink = ""
                            fid = datetime.now().strftime("%m_%d_%Y-%H_%M_%S")
                            for item in message.content.split(" "):
                                if "privnote.com/" in item:
                                    privnoteLink = item
                            print_sniper("Privnote")
                            print_sniper_info("Link", privnoteLink)
                            print_sniper_info("Author", message.author)
                            try:
                                print_sniper_info("Server", message.guild.name)
                            except:
                                pass
                            try:
                                print_sniper_info("Channel", message.channel.name)
                            except:
                                pass
                            try:
                                content = read_privnote(privnoteLink)
                                file = open(f"privnote-saves/{fid}.txt", "w")
                                file.write(f"Privnote sent by {message.author} in #{message.channel.name}, {message.guild.name}.\nSniped at {fid}.\n \n{content}")
                                file.close()
                                print_sniper_info("Content", content)        

                                if __sounds__:
                                    if str(sounddevice.query_devices()) != "":
                                        pygame.mixer.music.load(resource_path("sounds/notification.mp3"))
                                        pygame.mixer.music.play(1)

                                send_notification("Privnote Sniper", "Sniped a privnote note!", 10)                                       
                            except:
                                print_sniper_info("Failed", "Note already been read.")               
                            print_sniper_info("Snipe Speed", str((datetime.now()-messageSendTime).total_seconds()) + "s")

                            if __privnotewebhook__ != "":
                                webhook = DiscordWebhook(url=__privnotewebhook__)
                                embed = DiscordEmbed(title='Privnote Sniper', color=__embedcolourraw__[1:])
                                embed.set_thumbnail(url=__embedimage__)
                                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                                embed.set_timestamp()
                                embed.add_embed_field(name='Author', value=str(message.author), inline=False)
                                embed.add_embed_field(name='Privnote Link', value=privnoteLink, inline=False)
                                try:
                                    embed.add_embed_field(name='Content', value=content, inline=False)
                                except:
                                    embed.add_embed_field(name='Failed', value="Note already been read.", inline=False)
                                embed.add_embed_field(name='Jump to message', value=f"[Click Here!]({message.jump_url})", inline=False)
                                webhook.add_embed(embed)
                                response = webhook.execute()   

                if __giveawaysniper__:
                    if message.embeds:
                        messageEmbed = discord.Embed.to_dict(message.embeds[0])

                    if message.author.id in giveawayBots and message.author.bot:
                        isGiveaway = False

                        if message.embeds:
                            if "giveaway" in str(messageEmbed).lower():
                                isGiveaway = True
                        else:
                            if "giveaway" in message.content.lower():
                                isGiveaway = True

                        if isGiveaway:
                            if message.guild.id not in __ignoredservers__["giveaways"]:
                                embed = message.embeds[0].to_dict()
                                prize = embed["author"]["name"]
                                if "ban" in prize.lower() or "kick" in prize.lower() or "mute" in prize.lower() or "punish" in prize.lower():
                                    print_sniper("Giveaway")
                                    print_sniper_info("Prize", prize)
                                    print_sniper_info("Skipped", "Sus prize.")
                                    try:
                                        print_sniper_info("Server", message.guild.name)
                                    except:
                                        pass
                                    try:
                                        print_sniper_info("Channel", message.channel.name)
                                    except:
                                        pass   
                                    if __sounds__:
                                        if str(sounddevice.query_devices()) != "":
                                            pygame.mixer.music.load(resource_path("sounds/notification.mp3"))
                                            pygame.mixer.music.play(1)                                                               
                                    send_notification("Giveaway Sniper", f"Giveaway skipped because of sus prize.", 10)                                      
                                else:
                                    print_sniper("Giveaway")
                                    print_sniper_info("Prize", prize)
                                    try:
                                        print_sniper_info("Server", message.guild.name)
                                    except:
                                        pass
                                    try:
                                        print_sniper_info("Channel", message.channel.name)
                                    except:
                                        pass

                                    if __giveawaywebhook__ != "":
                                        webhook = DiscordWebhook(url=__giveawaywebhook__)
                                        embed = DiscordEmbed(title='Giveaway Sniper', description=f"Sniped a giveaway for `{prize}` in `{message.guild.name}`.", color=__embedcolourraw__[1:])
                                        embed.set_thumbnail(url=__embedimage__)
                                        embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                                        embed.set_timestamp()
                                        webhook.add_embed(embed)
                                        response = webhook.execute()
    
                                    # if __giveawaysniperui__ == True:
                                    #     def giveawayGUI():
                                    #         giveawayUi = tkinter.Tk()
                                    #         giveawayUi.attributes('-topmost', True)

                                    #         def addReactionForGiveaway():
                                    #             requests.put(f"https://discord.com/api/channels/{message.channel.id}/messages/{message.id}/reactions/%F0%9F%8E%89/@me", headers={"Authorization": __token__, "User-Agent": get_random_user_agent()})

                                    #         def closeGui():
                                    #             giveawayUi.destroy()

                                    #         def joinGiveaway():
                                    #             print(f"{printSpaces} {fg.cYellow}Joined giveaway!")
                                    #             addReactionForGiveaway()
                                    #             closeGui()

                                    #         giveawayUi.wm_title("Giveaway UI")
                                    #         windowWidth = giveawayUi.winfo_reqwidth()
                                    #         windowHeight = giveawayUi.winfo_reqheight()
                                    #         positionRight = int(giveawayUi.winfo_screenwidth()/2 - windowWidth/2)
                                    #         positionDown = int(giveawayUi.winfo_screenheight()/2 - windowHeight/2)
                                    #         giveawayUi.geometry("+{}+{}".format(positionRight, positionDown))
                                    #         tkinter.Label(giveawayUi, text=" ").pack()
                                    #         mainLabel = tkinter.Label(giveawayUi, text="Would you like to join a giveaway for").pack()
                                    #         prizeLabel = tkinter.Label(giveawayUi, text=prize).pack()
                                    #         tkinter.Label(giveawayUi, text=" ").pack()
                                    #         joinBtn = tkinter.Button(giveawayUi, text="Join", command=joinGiveaway, width=15, height=2, bg="green", fg="white").pack(side=tkinter.constants.LEFT)
                                    #         cancelBtn = tkinter.Button(giveawayUi, text="Cancel", command=closeGui, width=15, height=2, bg="red", fg="white").pack(side=tkinter.constants.LEFT)
                                    #         giveawayUi.mainloop()

                                    #     giveawayGUI()

                                    #     if __sounds__:
                                    #         if str(sounddevice.query_devices()) != "":
                                    #             pygame.mixer.music.load(resource_path("sounds/notification.mp3"))
                                    #             pygame.mixer.music.play(1)

                                    #     send_notification("Giveaway Sniper", f"Sniped a giveaway for {prize}.", 10)

                                    #     if __giveawaywebhook__ != "":
                                    #         webhook = DiscordWebhook(url=__giveawaywebhook__)
                                    #         embed = DiscordEmbed(title='Giveaway Sniper', description=f"Joined a giveaway for `{prize}` after pressing join in Giveaway UI.", color=__embedcolourraw__[1:])
                                    #         embed.set_thumbnail(url=__embedimage__)
                                    #         embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                                    #         embed.set_timestamp()
                                    #         embed.add_embed_field(name='Prize', value=prize, inline=False)
                                    #         embed.add_embed_field(name='Joined After', value=f"Pressing join in Giveaway UI.", inline=False)
                                    #         embed.add_embed_field(name='Jump to message', value=f"[Click Here!]({message.jump_url})", inline=False)
                                    #         webhook.add_embed(embed)
                                    #         response = webhook.execute()                                 

                                    # else:   

                                    pygame.mixer.music.load(resource_path("sounds/notification.mp3"))
                                    pygame.mixer.music.play(1)                                          
                                    send_notification("Giveaway Sniper", f"Sniped a giveaway for {prize}.", 10)
                                    await asyncio.sleep(__giveawayjoindelay__)
                                    emoji = GIVEAWAYBOTS[str(message.author.id)]
                                    await message.add_reaction(emoji)

                                    if __giveawaywebhook__ != "":
                                        webhook = DiscordWebhook(url=__giveawaywebhook__)
                                        embed = DiscordEmbed(title='Giveaway Sniper', description=f"Joined a giveaway for `{prize}` after `{__giveawayjoindelay__}` seconds.", color=__embedcolourraw__[1:])
                                        embed.set_thumbnail(url=__embedimage__)
                                        embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                                        embed.set_timestamp()
                                        webhook.add_embed(embed)
                                        response = webhook.execute()

                                    print_sniper("Giveaway")
                                    print_sniper_info("Prize", prize)
                                    try:
                                        print_sniper_info("Server", message.guild.name)
                                    except:
                                        pass
                                    try:
                                        print_sniper_info("Channel", message.channel.name)
                                    except:
                                        pass
                                    print_sniper_info("Joined after", f"{__giveawayjoindelay__} seconds.")
                                    send_notification("Giveaway Sniper", f"Joined a giveaway for {prize}.", 10)       
                                    pygame.mixer.music.load(resource_path("sounds/notification.mp3"))
                                    pygame.mixer.music.play(1)

                            # if "congratulations" in message.content.lower():
                            #     if f"<@{Ghost.user.id}>" in message.content.lower():
                            #         prize = message.content.split("!")[1].split("**")[1]
                            #         print_sniper("Giveaway")
                            #         print(f" {fg.cYellow}You won!!!")
                            #         print_sniper_info("Prize", prize)
                            #         try:
                            #             print_sniper_info("Server", message.guild.name)
                            #         except:
                            #             pass
                            #         try:
                            #             print_sniper_info("Channel", message.channel.name)
                            #         except:
                            #             pass

                            #         if __giveawaywebhook__  != "":
                            #             webhook = DiscordWebhook(url=__giveawaywebhook__)
                            #             embed = DiscordEmbed(title='Giveaway Sniper', description=f"You won a giveaway for `{prize}`!", color=__embedcolourraw__[1:])
                            #             embed.set_thumbnail(url=__embedimage__)
                            #             embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                            #             embed.set_timestamp()
                            #             webhook.add_embed(embed)
                            #             response = webhook.execute() 

                            #         send_notification("Giveaway Sniper", f"You won a giveaway for {prize} 🎉!", 10)                                                                       
                            #         if __sounds__:
                            #             if str(sounddevice.query_devices()) != "":
                            #                 pygame.mixer.music.load(resource_path("sounds/giveaway-win.mp3"))
                            #                 pygame.mixer.music.play(1)

                if __selfbotdetect__:
                    if not message.author.bot:
                        if message.embeds:
                            if "http" not in message.content:
                                if message.guild.id not in __ignoredservers__["selfbots"]:
                                    print_detect("Selfbot")
                                    print_sniper_info("Author", message.author)
                                    try:
                                        print_sniper_info("Server", message.guild.name)
                                    except:
                                        pass
                                    try:
                                        print_sniper_info("Channel", message.channel.name)
                                    except:
                                        pass
                                    print_sniper_info("Reason", "Sent an embedded message.")                        
                                    if __selfbotwebhook__ != "":
                                        webhook = DiscordWebhook(url=__selfbotwebhook__)
                                        embed = DiscordEmbed(title='Selfbot', color=__embedcolourraw__[1:])
                                        embed.set_thumbnail(url=__embedimage__)
                                        embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                                        embed.set_timestamp()
                                        embed.add_embed_field(name='Author', value=str(message.author), inline=False)
                                        try:
                                            embed.add_embed_field(name='Server', value=str(message.guild.name), inline=False)
                                        except:
                                            pass
                                        try:
                                            embed.add_embed_field(name='Channel', value=str(message.channel.name), inline=False)
                                        except:
                                            pass  
                                        embed.add_embed_field(name='Reason', value="Sent an embedded message.", inline=False)                                              
                                        webhook.add_embed(embed)
                                        response = webhook.execute()   

            if message.author.id == Ghost.user.id:
                ccmd = json.load(open("customcommands.json"))
                for key in ccmd:
                    cmd = key
                    response = ccmd[key]
                    if message.content == f"{__prefix__}{cmd}":
                        print_cmd(f"{cmd}")
                        try:
                            await message.delete()
                        except:
                            pass
                        
                        response = response.replace("{currenttime}", str(datetime.now().strftime("%H:%M:%S")))
                        response = response.replace("{currentdate}", str(datetime.now().strftime("%d/%m/%Y")))
                        response = response.replace("{version}", str(version))
                        response = response.replace("{uid}", str(__uid__))
                        response = response.replace("{prefix}", str(__prefix__))
                        response = response.replace("{theme}", str(__theme__))  
                        response = response.replace("{randomint}", str(random.randint(1000, 9999)))
                        response = response.replace("{randomstring}", str(''.join(random.choice(string.ascii_letters) for i in range(8))))
                        
                        await message.channel.send(response)

                if (uwuifyEnabled):
                    if (not message.content.startswith(__prefix__) or message.content == "" or message.content == None):
                        uwuedMessage = uwuify.uwu(message.content)
                        await message.edit(content=uwuedMessage)
                        
            #print(str(message.author) + " : " + str(message.content))

        await Ghost.process_commands(message)  

    for filename in os.listdir('scripts/'):
        if filename.endswith('.py'):
            include(f'scripts/{filename}')

    @Ghost.command(name="scripts", description="Display all custom scripts.", usage="scripts", aliases=["customscripts"])
    async def scripts(ctx):
        totalscripts = len(os.listdir('scripts/'))
        text = ""
        for script in os.listdir('scripts/'):
            if script.endswith('.py'):
                script = script.replace(".py", "")
                text += f"{script}\n"

        if __embedmode__:
            embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", description=f"Found {totalscripts} custom scripts", color=__embedcolour__)
            embed.add_field(name="Scripts", value=text)
            embed.set_author(name="Custom Scripts")
            embed.set_thumbnail(url=__embedimage__)
            embed.set_image(url=__embedlargeimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send(f"""```ini
[ Custom Scripts ]

Found {totalscripts} custom scripts

{text}

# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="customcommands", description="Display all custom commands.", usage="customcommands", aliases=["ccmds"])
    async def customcommands(ctx):
        totalcmds = len(ccmd)
        ccmd2 = ""
        for key in ccmd:
            cmd = key
            ccmd2 = ccmd2 + f"{__prefix__}{cmd}\n"

        if __embedmode__:
            embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__, description=f"Found {totalcmds} custom commands.")
            embed.add_field(name="Commands", value=ccmd2)
            embed.set_author(name="Custom Commands")
            embed.set_thumbnail(url=__embedimage__)
            embed.set_image(url=__embedlargeimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send(f"""```ini
[ Custom Commands ]

Found {totalcmds} custom commands.

{ccmd2}

{__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="allcmds", description="Print a list of all the commands.", usage="allcmds", aliases=["features"])
    async def allcmds(ctx):
        await ctx.message.delete()
        content = ""
        totalCommands = len(Ghost.commands)
        for command in Ghost.commands:
            content += f"{command.usage} : {command.description}\n"    

        file = open("data/features.txt", "w")
        file.write(f"[All Commands]\nTotal Commands: {totalCommands}\n \n" + content)
        file.close()

        os.system("notepad data/features.txt")

    @Ghost.command(name="search", description="Search for commands.", usage="search [term]")
    async def search(ctx, *, command = None):
        if command is None:
            if __embedmode__:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__, description="Please enter a command to search for.")
                embed.set_author(name="Search")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send(f"""```ini
[ Search ]

Please enter a command to search for.


# {__embedfooter__}
```""", delete_after=__deletetimeout__)
        else:
            text = ""
            text2 = ""
            searchedItems = 0
            for cmd in Ghost.commands:
                if command in cmd.name or command in cmd.description or command in cmd.aliases:
                    searchedItems += 1
                    text += f"`{Ghost.command_prefix}`**{cmd.usage}** » {cmd.description}\n"
                    text2 += f"{Ghost.command_prefix}{cmd.usage} » {cmd.description}\n"

            try:
                if __embedmode__:
                    embed = discord.Embed(title=f"Search results...", description=f"Found `{searchedItems}` items for `{command}`.\n\n{text}", color=__embedcolour__)
                    embed.set_thumbnail(url=__embedimage__)
                    embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                    embed.set_image(url=__embedlargeimage__)
                    embed.timestamp = datetime.now()
                    await ctx.send(embed=embed, delete_after=__deletetimeout__)
                else:
                    await ctx.send(f"""```ini
[ Searched for {command} ]

{text2}


# {__embedfooter__}```""", delete_after=__deletetimeout__)
            except:
                if __embedmode__:
                    embed = discord.Embed(title=f"Check console for search results", color=__embedcolour__)
                    embed.set_thumbnail(url=__embedimage__)
                    embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                    embed.set_image(url=__embedlargeimage__)
                    embed.timestamp = datetime.now()
                    await ctx.send(embed=embed, delete_after=__deletetimeout__)
                else:
                    await ctx.send(f"""```ini
[ Check console for search results ]


# {__embedfooter__}```""", delete_after=__deletetimeout__)
                print(f"[ Search results for {command} ]\n{text2}")

    @Ghost.command(name="help", description="The help command.", usage="help (command)", aliases=["cmds", "commands"])
    async def help(ctx, *, command = None):
        totalcmds = len(Ghost.commands)-len(scriptsList)
        if command is None:
            if __embedmode__:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__, description=f"""
Arguments in `[]` are required, arguments in `()` are optional.

`{Ghost.command_prefix}`**text (page 1/2)** » Text commands.
`{Ghost.command_prefix}`**fun (page 1)** » Fun commands.
`{Ghost.command_prefix}`**image (page 1)** » Image commands.
`{Ghost.command_prefix}`**moderation (page 1)** » Moderation commands.
`{Ghost.command_prefix}`**info (page 1)** » Info commands.
`{Ghost.command_prefix}`**user (page 1)** » User commands.
`{Ghost.command_prefix}`**selfbot (page 1)** » Selfbot commands.
`{Ghost.command_prefix}`**webhook (page 1)** » Webhook commands.
`{Ghost.command_prefix}`**abuse (page 1)** » Abuse commands.
`{Ghost.command_prefix}`**themes (page 1)** » Theme commands.
`{Ghost.command_prefix}`**giveaway (page 1)** » Giveaway commands.
`{Ghost.command_prefix}`**nsfw (page 1)** » NSFW commands.
`{Ghost.command_prefix}`**proxy (page 1)** » Proxy commands.
`{Ghost.command_prefix}`**tools (page 1)** » Discord and other tools.
`{Ghost.command_prefix}`**customcommands** » Your custom commands.
`{Ghost.command_prefix}`**customscripts** » Your scripts.

`{Ghost.command_prefix}`**search [term]** » Search for a command.
`{Ghost.command_prefix}`**help (command)** » Help for a specific command.

There is a total of `{totalcmds}` commands.
            """)
                embed.set_author(name="All Commands")
                embed.set_image(url=__embedlargeimage__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send(f"""```ini
[ {__embedtitle__} ]

Arguments in [] are required, arguments in () are optional.

{Ghost.command_prefix}text (page 1/2) » Text commands.
{Ghost.command_prefix}fun (page 1) » Fun commands.
{Ghost.command_prefix}image (page 1) » Image commands.
{Ghost.command_prefix}moderation (page 1) » Moderation commands.
{Ghost.command_prefix}info (page 1) » Info commands.
{Ghost.command_prefix}user (page 1) » User commands.
{Ghost.command_prefix}selfbot (page 1) » Selfbot commands.
{Ghost.command_prefix}webhook (page 1) » Webhook commands.
{Ghost.command_prefix}abuse (page 1) » Abuse commands.
{Ghost.command_prefix}themes (page 1) » Theme commands.
{Ghost.command_prefix}giveaway (page 1) » Giveaway commands.
{Ghost.command_prefix}nsfw (page 1) » NSFW commands.
{Ghost.command_prefix}proxy (page 1) » Proxy commands.
{Ghost.command_prefix}tools (page 1) » Discord and other tools.
{Ghost.command_prefix}customcommands » Your custom commands.
{Ghost.command_prefix}customscripts » Your scripts.

{Ghost.command_prefix}search [term] » Search for a command.
{Ghost.command_prefix}help (command) » Help for a specific command.

There is a total of {totalcmds} commands.

# {__embedfooter__}```""", delete_after=__deletetimeout__)

        else:
            for cmd in Ghost.commands:
                if command == cmd.name or command in cmd.aliases:
                    if not cmd.aliases:
                        cmd.aliases.append("No aliases")
                    if __embedmode__:
                        embed = discord.Embed(title=f"{cmd.name}", color=__embedcolour__)
                        embed.add_field(name="Usage", value=f"{cmd.usage}", inline=False)
                        embed.add_field(name="Description", value=f"{cmd.description}", inline=False)
                        embed.add_field(name="Aliases", value=', '.join(cmd.aliases))
                        embed.set_thumbnail(url=__embedimage__)
                        embed.set_image(url=__embedlargeimage__)
                        embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                        embed.timestamp = datetime.now()
                        await ctx.send(embed=embed, delete_after=__deletetimeout__)
                    else:
                        await ctx.send(f"""```ini
[ {cmd.name} ]

Usage: {cmd.usage}
Description: {cmd.description}


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="themes", description="Theme related commands.", usage="themes")
    async def themes(ctx):
        themes = ""
        for theme in os.listdir("themes"):
            if theme.endswith(".json"):
                theme = theme.replace(".json", "")
                themes += f"{theme}\n"

        if __embedmode__:
            embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__)
            embed.add_field(name="Current Theme", value=f"{__theme__}", inline=False)
            embed.add_field(name="Other Themes", value=f"{themes}", inline=False)
            embed.add_field(name="Commands", value=f"`{Ghost.command_prefix}`**newtheme [name]** » Create a new theme with the given name.\n`{Ghost.command_prefix}`**deltheme [name]** » Delete the named theme.\n`{Ghost.command_prefix}`**theme [theme]** » Change your current theme.\n`{Ghost.command_prefix}`**ctheme** » Community themes.", inline=False)
            embed.set_author(name="Theme Commands")
            embed.set_thumbnail(url=__embedimage__)
            embed.set_image(url=__embedlargeimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send(f"""```ini
[ Theme Commands ]

Current Theme: {__theme__}

[ Other Themes ]
{themes}

[ Commands ]
{Ghost.command_prefix}newtheme [name] » Create a new theme with the given name.
{Ghost.command_prefix}deltheme [name] » Delete the named theme.
{Ghost.command_prefix}theme [theme] » Change your current theme.
{Ghost.command_prefix}cthemes » Community themes.


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="ctheme", description="Community themes.", usage="ctheme", aliases=["communitythemes", "cloudthemes", "cthemes"])
    async def ctheme(ctx, *, dl = None):
        if dl is None:
            url = "https://ghost.cool/assets/cthemes.txt"
            themes = requests.get(url).text.split("\n")

            if __embedmode__:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", description=f"Community Themes, run `{Ghost.command_prefix}ctheme (theme name)` to download the theme.\n ", color=__embedcolour__)
                embed.add_field(name="Theme List", value='\n'.join(themes))
                embed.set_author(name="Community Themes")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send(f"""```ini
[ Community Themes ]

Community Themes, run {Ghost.command_prefix}ctheme (theme name) to download the theme.


[ Theme List ]
{themes}


# {__embedfooter__}```""", delete_after=__deletetimeout__)

        else:
            request = requests.get("https://ghost.cool/assets/cthemes.txt")
            themes = []
            for line in request.text.split("\n"):
                themes.append(line.replace("\r", ""))

            print(themes)
            print(dl)

            if dl in themes:
                url = f'https://ghost.cool/assets/cthemes/{dl}.json'
                data = requests.get(url, allow_redirects=True)
                open(f'themes/{dl}.json', 'wb').write(data.content)

                if __embedmode__:
                    embed = discord.Embed(title="Theme downloaded successfully", color=__embedcolour__)
                    embed.set_thumbnail(url=__embedimage__)
                    embed.set_image(url=__embedlargeimage__)
                    embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                    embed.timestamp = datetime.now()
                    await ctx.send(embed=embed, delete_after=__deletetimeout__)
                else:
                    await ctx.send(f"""```ini
[ Theme downloaded successfully ]


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="text", description="Text related commands.", usage="text (page)")
    async def text(ctx, page:int = 1):
        if __embedmode__:
            if page == 1:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__, description=f"""
`{Ghost.command_prefix}`**js [message]** » Send all your messages in a JavaScript code block.
`{Ghost.command_prefix}`**lua [message]** » Send all your messages in a Lua code block.
`{Ghost.command_prefix}`**php [message]** » Send all your messages in a PHP code block.
`{Ghost.command_prefix}`**html [message]** » Send all your messages in a HTML code block.
`{Ghost.command_prefix}`**css [message]** » Send all your messages in a CSS code block.
`{Ghost.command_prefix}`**yaml [message]** » Send all your messages in a YAML code block.
`{Ghost.command_prefix}`**json [message]** » Send all your messages in a JSON code block.
`{Ghost.command_prefix}`**cpp [message]** » Send all your messages in a C++ code block.
`{Ghost.command_prefix}`**cs [message]** » Send all your messages in a C# code block.
`{Ghost.command_prefix}`**java [message]** » Send all your messages in a Java code block.
`{Ghost.command_prefix}`**python [message]** » Send all your messages in a Python code block.
`{Ghost.command_prefix}`**secret [message]** » Send all your messages in a secret block.
`{Ghost.command_prefix}`**secretletters [message]** » Put all lettes from your message into separate secret blocks
`{Ghost.command_prefix}`**regional [message]** » Replace all letters with emoji.
`{Ghost.command_prefix}`**bold [message]** » Send all your messages in bold.
`{Ghost.command_prefix}`**italic [message]** » Send all your messages in italics.
            """)
                embed.set_author(name="Text Commands (1/2)")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            elif page == 2:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__, description=f"""
`{Ghost.command_prefix}`**rembed (delay) [title]** » Kill Discord's API with a sexy rainbow embedded message.
`{Ghost.command_prefix}`**cembed [title] [description] [colour]** » Create a custom embedded message.
`{Ghost.command_prefix}`**embed [title]** » Create an embedded message.
`{Ghost.command_prefix}`**suggest [suggestion]** » Suggest something.
`{Ghost.command_prefix}`**privatemsg [message]** » Send an encrypted message.
`{Ghost.command_prefix}`**privatemsgdecode [message]** » Decode an encrypted message.
`{Ghost.command_prefix}`**blank** » Send a blank message
`{Ghost.command_prefix}`**length [string]** » Get the length of a string.
`{Ghost.command_prefix}`**chatbypass [text]** » Bypass chat language restrictions.
`{Ghost.command_prefix}`**shrug** » Shrug your arms.
`{Ghost.command_prefix}`**tableflip** » Flip the table.
`{Ghost.command_prefix}`**unflip** » Put the table back.
`{Ghost.command_prefix}`**lmgtfy [search]** » Let me Google that for you.
`{Ghost.command_prefix}`**typing [start/stop]** » Start or stop typing.
`{Ghost.command_prefix}`**aesthetic [text]** » Send your text s p a c e d out.
`{Ghost.command_prefix}`**lowercase [msg]** » Send your message in lowercase.
`{Ghost.command_prefix}`**uppercase [msg]** » Send your message in uppercase.
`{Ghost.command_prefix}`**sentencecase [msg]** » Send your messages in sentence case.
`{Ghost.command_prefix}`**ascii [text]** » Send your message in ascii.
`{Ghost.command_prefix}`**zalgo [text]** » Unleash the zalgo into your message.  
`{Ghost.command_prefix}`**leet [text]** » Turn your text into 1337 text.
`{Ghost.command_prefix}`**fakeedited [message]** » "Edit" a message.
            """)
                embed.set_author(name="Text Commands (2/2)")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                pass
        else:
            if page == 1:
                await ctx.send(f"""```ini
[ Text Commands (1/2) ]

{Ghost.command_prefix}js [message] » Send all your messages in a JavaScript code block.
{Ghost.command_prefix}lua [message] » Send all your messages in a Lua code block.
{Ghost.command_prefix}php [message] » Send all your messages in a PHP code block.
{Ghost.command_prefix}html [message] » Send all your messages in a HTML code block.
{Ghost.command_prefix}css [message] » Send all your messages in a CSS code block.
{Ghost.command_prefix}yaml [message] » Send all your messages in a YAML code block.
{Ghost.command_prefix}json [message] » Send all your messages in a JSON code block.
{Ghost.command_prefix}cpp [message] » Send all your messages in a C++ code block.
{Ghost.command_prefix}cs [message] » Send all your messages in a C# code block.
{Ghost.command_prefix}java [message] » Send all your messages in a Java code block.
{Ghost.command_prefix}python [message] » Send all your messages in a Python code block.
{Ghost.command_prefix}secret [message] » Send all your messages in a secret block.
{Ghost.command_prefix}secretletters [message] » Put all lettes from your message into separate secret blocks
{Ghost.command_prefix}regional [message] » Replace all letters with emoji.
{Ghost.command_prefix}bold [message] » Send all your messages in bold.
{Ghost.command_prefix}italic [message] » Send all your messages in italics.


# {__embedfooter__}```""", delete_after=__deletetimeout__)

            elif page == 2:
                await ctx.send(f"""```ini
[ Text Commands (2/2) ]

{Ghost.command_prefix}rembed (delay) [title] » Kill Discord's API with a sexy rainbow embedded message.
{Ghost.command_prefix}cembed [title] [description] [colour] » Create a custom embedded message.
{Ghost.command_prefix}embed [title] » Create an embedded message.
{Ghost.command_prefix}suggest [suggestion] » Suggest something.
{Ghost.command_prefix}privatemsg [message] » Send an encrypted message.
{Ghost.command_prefix}privatemsgdecode [message] » Decode an encrypted message.
{Ghost.command_prefix}blank » Send a blank message
{Ghost.command_prefix}length [string] » Get the length of a string.
{Ghost.command_prefix}chatbypass [text] » Bypass chat language restrictions.
{Ghost.command_prefix}shrug » Shrug your arms.
{Ghost.command_prefix}tableflip » Flip the table.
{Ghost.command_prefix}unflip » Put the table back.
{Ghost.command_prefix}lmgtfy [search] » Let me Google that for you.
{Ghost.command_prefix}typing [start/stop] » Start or stop typing.
{Ghost.command_prefix}aesthetic [text] » Send your text s p a c e d out.
{Ghost.command_prefix}lowercase [msg] » Send your message in lowercase.
{Ghost.command_prefix}uppercase [msg] » Send your message in uppercase.
{Ghost.command_prefix}sentencecase [msg] » Send your messages in sentence case.
{Ghost.command_prefix}ascii [text] » Send your message in ascii.
{Ghost.command_prefix}zalgo [text] » Unleash the zalgo into your message. 
{Ghost.command_prefix}leet [text] » Turn your text into 1337 text.
{Ghost.command_prefix}fakeedited [message] » "Edit" a message.


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="fun", description="Fun related commands.", usage="fun")
    async def fun(ctx, page:int = 1):
        if __embedmode__:
            if page == 1:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__, description=f"""
`{Ghost.command_prefix}`**slots** » Play the slot machine.
`{Ghost.command_prefix}`**yomomma** » Random yo momma joke.
`{Ghost.command_prefix}`**socialcredit [@user]** » A users social credit score. 
`{Ghost.command_prefix}`**roast [@user]** » Roast a user.
`{Ghost.command_prefix}`**howgay [@user]** » How gay a user is.
`{Ghost.command_prefix}`**howskid [@user]** » Check the percentage of a skid.
`{Ghost.command_prefix}`**iq [@user]** » Check how smart a user is.
`{Ghost.command_prefix}`**pp [@user]** » The length of a user's penis.
`{Ghost.command_prefix}`**rainbowrole [@role]** » Kill Discord's API with a sexy rainbow role.
`{Ghost.command_prefix}`**coinflip** » Flip a coin.
`{Ghost.command_prefix}`**dice** » Roll a dice.
`{Ghost.command_prefix}`**8ball [question]** » Ask the magic eight ball a question.
`{Ghost.command_prefix}`**choice [choice1] [choice2]** » Pick a random choice.
`{Ghost.command_prefix}`**dox [@user]** » Dox the mentioned user.
`{Ghost.command_prefix}`**fakenitro [url]** » Hide a link in a nitro URL.
`{Ghost.command_prefix}`**purgehack** » Purge without permissions.
`{Ghost.command_prefix}`**dadjoke** » A random dad joke.
`{Ghost.command_prefix}`**randommessage** » A random message.
`{Ghost.command_prefix}`**randomquestion** » A random question.
`{Ghost.command_prefix}`**rickroll** » Send never gonna give you up lyrics one by one.
`{Ghost.command_prefix}`**stoprickroll** » Stop sending rick astley lyrics.
`{Ghost.command_prefix}`**countdown [number]** » Count down from a number.
`{Ghost.command_prefix}`**countup [number]** » Count up from a number.
`{Ghost.command_prefix}`**pytoexe [path]** » Convert a PY file to an executable.
            """)
                embed.set_author(name="Fun Commands (1/1)")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                pass
        else:
            await ctx.send(f"""```ini
[ Fun Commands ]

{Ghost.command_prefix}slots » Play the slot machine.
{Ghost.command_prefix}yomomma » Random yo momma joke.
{Ghost.command_prefix}socialcredit [@user] » A users social credit score. 
{Ghost.command_prefix}roast [@user] » Roast a user.
{Ghost.command_prefix}howgay [@user] » How gay a user is.
{Ghost.command_prefix}howskid [@user] » Check the percentage of a skid.
{Ghost.command_prefix}iq [@user] » Check how smart a user is.
{Ghost.command_prefix}pp [@user] » The length of a user's penis.
{Ghost.command_prefix}rainbowrole [@role] » Kill Discord's API with a sexy rainbow role.
{Ghost.command_prefix}coinflip » Flip a coin.
{Ghost.command_prefix}dice » Roll a dice.
{Ghost.command_prefix}8ball [question] » Ask the magic eight ball a question.
{Ghost.command_prefix}choice [choice1] [choice2] » Pick a random choice.
{Ghost.command_prefix}dox [@user] » Dox the mentioned user.
{Ghost.command_prefix}fakenitro [url] » Hide a link in a nitro URL.
{Ghost.command_prefix}purgehack » Purge without permissions.
{Ghost.command_prefix}dadjoke » A random dad joke.
{Ghost.command_prefix}randommessage » A random message.
{Ghost.command_prefix}randomquestion » A random question.
{Ghost.command_prefix}rickroll » Send never gonna give you up lyrics one by one.
{Ghost.command_prefix}stoprickroll » Stop sending rick astley lyrics.
{Ghost.command_prefix}countdown [number] » Count down from a number.
{Ghost.command_prefix}countup [number] » Count up from a number.
{Ghost.command_prefix}pytoexe [path] » Convert a PY file to an executable.


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="image", description="Image related commands.", usage="image")
    async def image(ctx, page:int = 1):
        if __embedmode__:
            if page == 1:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__, description=f"""
`{Ghost.command_prefix}`**meme** » A random meme.
`{Ghost.command_prefix}`**cat** » A random cat image.
`{Ghost.command_prefix}`**dog** » A random dog image.
`{Ghost.command_prefix}`**shiba** » A random shiba image.
`{Ghost.command_prefix}`**fox** » A random fox image. (Thanks Imf44 <3)
`{Ghost.command_prefix}`**avatar [@user]** » Get the mentioned user's avatar.
`{Ghost.command_prefix}`**servericon** » Get the server's icon. 
`{Ghost.command_prefix}`**achievement ["text"] (icon)** » Create a fake minecraft achievement image.
`{Ghost.command_prefix}`**challenge ["text"] (icon)** » Create a fake minecraft challenge image.
`{Ghost.command_prefix}`**captcha [text]** » Create a fake reCaptcha.
`{Ghost.command_prefix}`**amiajoke [@user]** » Make a user a joke.
`{Ghost.command_prefix}`**didyoumean ["text 1"] ["text 2"]** » Create a google did you mean image.
`{Ghost.command_prefix}`**drake ["text 1"] ["text 2"]** » Create a drake meme image.
`{Ghost.command_prefix}`**facts [text]** » Create a facts meme image.
`{Ghost.command_prefix}`**jokeoverhead [image url]** » Create a joke over head image.
`{Ghost.command_prefix}`**pornhub ["text 1"] ["text 2"]** » Create a pornhub logo image.
`{Ghost.command_prefix}`**salty [@user]** » Make someone salty.
`{Ghost.command_prefix}`**ship [@user 1] [@user 2]** » Ship two people.
`{Ghost.command_prefix}`**supreme [text]** » Create a supreme logo image.
`{Ghost.command_prefix}`**trash [@user]** » Put someone in the trash.
`{Ghost.command_prefix}`**what [image url]** » Make a what meme.

            """)
                embed.set_author(name="Image Commands (1/1)")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                pass         
        else:
            await ctx.send(f"""```ini
[ Image Commands ]

{Ghost.command_prefix}meme » A random meme.
{Ghost.command_prefix}cat » A random cat image.
{Ghost.command_prefix}dog » A random dog image.
{Ghost.command_prefix}shiba » A random shiba image.
{Ghost.command_prefix}fox » A random fox image. (Thanks Imf44 <3)
{Ghost.command_prefix}avatar [@user] » Get the mentioned user's avatar.
{Ghost.command_prefix}servericon » Get the server's icon. 
{Ghost.command_prefix}achievement ["text"] (icon) » Create a fake minecraft achievement image.
{Ghost.command_prefix}challenge ["text"] (icon) » Create a fake minecraft challenge image.
{Ghost.command_prefix}captcha [text] » Create a fake reCaptcha.
{Ghost.command_prefix}amiajoke [@user] » Make a user a joke.
{Ghost.command_prefix}didyoumean ["text 1"] ["text 2"] » Create a google did you mean image.
{Ghost.command_prefix}drake ["text 1"] ["text 2"] » Create a drake meme image.
{Ghost.command_prefix}facts [text] » Create a facts meme image.
{Ghost.command_prefix}jokeoverhead [image url] » Create a joke over head image.
{Ghost.command_prefix}pornhub ["text 1"] ["text 2"] » Create a pornhub logo image.
{Ghost.command_prefix}salty [@user] » Make someone salty.
{Ghost.command_prefix}ship [@user 1] [@user 2] » Ship two people.
{Ghost.command_prefix}supreme [text] » Create a supreme logo image.
{Ghost.command_prefix}trash [@user] » Put someone in the trash.
{Ghost.command_prefix}what [image url] » Make a what meme.


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="nsfw", description="NSFW related commands.", usage="nsfw")
    async def nsfw(ctx, page:int = 1):
        if __embedmode__:
            if page == 1:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__, description=f"""
`{Ghost.command_prefix}`**boobs** » Pictures or videos of boobs.
`{Ghost.command_prefix}`**ass** » Pictures or videos of ass.
`{Ghost.command_prefix}`**pussy** » Pictures or videos of pussy.
`{Ghost.command_prefix}`**porngif** » Porn gifs.
`{Ghost.command_prefix}`**hentai** » Pictures or videos of hentai.
            """)
                embed.set_author(name="NSFW Commands (1/1)")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                pass         
        else:
            await ctx.send(f"""```ini
[ NSFW Commands ]

{Ghost.command_prefix}boobs » Pictures or videos of boobs.
{Ghost.command_prefix}ass » Pictures or videos of ass.
{Ghost.command_prefix}pussy » Pictures or videos of pussy.
{Ghost.command_prefix}porngif » Porn gifs.
{Ghost.command_prefix}hentai » Pictures or videos of hentai.


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="moderation", description="Moderation related commands.", usage="moderation")
    async def moderation(ctx, page:int = 1):
        if __embedmode__:
            if page == 1:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__, description=f"""
`{Ghost.command_prefix}`**ban [@user]** » Ban the mentioned user.
`{Ghost.command_prefix}`**unban [id]** » Unban the mentioned id.
`{Ghost.command_prefix}`**banlist** » See the server's ban list.
`{Ghost.command_prefix}`**kick [@user]** » Kick the mentioned user.
`{Ghost.command_prefix}`**mute [@user]** » Mute the menitioned user.
`{Ghost.command_prefix}`**unmute [@user]** » Unmute the mentioned user.
`{Ghost.command_prefix}`**newrole [name]** » Create a new role.
`{Ghost.command_prefix}`**delrole [@role]** » Delete the mentioned role.
`{Ghost.command_prefix}`**purge [amount]** » Purge X amount of messages.
`{Ghost.command_prefix}`**lock** » Lock the command channel.
`{Ghost.command_prefix}`**unlock** » Unlock the command channel.
`{Ghost.command_prefix}`**lockdown** » Lock the entire server.
`{Ghost.command_prefix}`**unlockdown** » Unlock the entire server.
`{Ghost.command_prefix}`**spacechannel [channel name]** » Create a channel with spaces.
            """)
                embed.set_author(name="Moderation Commands (1/1)")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                pass
        else:
            await ctx.send(f"""```ini
[ Moderation Commands ]

{Ghost.command_prefix}ban [@user] » Ban the mentioned user.
{Ghost.command_prefix}unban [id] » Unban the mentioned id.
{Ghost.command_prefix}banlist » See the server's ban list.
{Ghost.command_prefix}kick [@user] » Kick the mentioned user.
{Ghost.command_prefix}mute [@user] » Mute the menitioned user.
{Ghost.command_prefix}unmute [@user] » Unmute the mentioned user.
{Ghost.command_prefix}newrole [name] » Create a new role.
{Ghost.command_prefix}delrole [@role] » Delete the mentioned role.
{Ghost.command_prefix}purge [amount] » Purge X amount of messages.
{Ghost.command_prefix}lock » Lock the command channel.
{Ghost.command_prefix}unlock » Unlock the command channel.
{Ghost.command_prefix}lockdown » Lock the entire server.
{Ghost.command_prefix}unlockdown » Unlock the entire server.
{Ghost.command_prefix}spacechannel [channel name] » Create a channel with spaces.


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="info", description="Info related commands.", usage="info")
    async def info(ctx, page:int = 1):
        if __embedmode__:
            if page == 1:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__, description=f"""
`{Ghost.command_prefix}`**userinfo [@user]** » Information about the mentioned user.
`{Ghost.command_prefix}`**serverinfo** » Information about the command server.
`{Ghost.command_prefix}`**watchdogstats** » Get stats about Hypixel's Anticheat, Watchdog.
`{Ghost.command_prefix}`**getmessage [message id]** » Get a message by ID.
`{Ghost.command_prefix}`**geoip [ip]** » Get information from an IP address.
`{Ghost.command_prefix}`**ping [ip/domain]** » Ping a domain or ip address. 
`{Ghost.command_prefix}`**crypto [currency]** » Get the current data on a cryptocurrency.
            """)
                embed.set_author(name="Info Commands (1/1)")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)     
            else:
                pass           
        else:
            await ctx.send(f"""```ini
[ Info Commands ]

{Ghost.command_prefix}userinfo [@user] » Information about the mentioned user.
{Ghost.command_prefix}serverinfo » Information about the command server.
{Ghost.command_prefix}watchdogstats » Get stats about Hypixel's Anticheat, Watchdog.
{Ghost.command_prefix}getmessage [message id] » Get a message by ID.
{Ghost.command_prefix}geoip [ip] » Get information from an IP address.
{Ghost.command_prefix}ping [ip/domain] » Ping a domain or ip address.
{Ghost.command_prefix}crypto [currency] » Get the current data on a cryptocurrency.


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="user", description="User related commands.", usage="user")
    async def user(ctx, page:int = 1):
        if __embedmode__:
            if page == 1:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__, description=f"""
`{Ghost.command_prefix}`**purgeself [amount]** » Purge your messages.
`{Ghost.command_prefix}`**statuscycle** » Start a custom status cycle.
`{Ghost.command_prefix}`**statuscycletext [text]** » Set the text used in status cycle.
`{Ghost.command_prefix}`**clearstatus** » Clear your status.
`{Ghost.command_prefix}`**nickname [text]** » Set your nickname to anything.
`{Ghost.command_prefix}`**clearnickname** » Clear your nickname.
`{Ghost.command_prefix}`**ppin [message id]** » Add a message to your personal pins.
`{Ghost.command_prefix}`**ppins** » List all your pinned messages.
`{Ghost.command_prefix}`**ppindel [pin id]** » Delete a pin from your personal pins.
`{Ghost.command_prefix}`**backupfriends** » Backup all your friend's user IDs to a file.
`{Ghost.command_prefix}`**backupservers** » Backup all your servers and try to create invites for each one.
`{Ghost.command_prefix}`**changehypesquad [bravery/brilliance/balance]** » Change your hypesquad house.
`{Ghost.command_prefix}`**stealpfp [@user]** » Set someones avatar as your avatar.
            """)
                embed.set_author(name="User Commands (1/1)")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)       
            else:
                pass         
        else:
            await ctx.send(f"""```ini
[ User Commands ]

{Ghost.command_prefix}purgeself [amount] » Purge your messages.
{Ghost.command_prefix}statuscycle » Start a custom status cycle.
{Ghost.command_prefix}statuscycletext [text] » Set the text used in status cycle.
{Ghost.command_prefix}clearstatus » Clear your status.
{Ghost.command_prefix}nickname [text] » Set your nickname to anything.
{Ghost.command_prefix}clearnickname » Clear your nickname.
{Ghost.command_prefix}ppin [message id] » Add a message to your personal pins.
{Ghost.command_prefix}ppins » List all your pinned messages.
{Ghost.command_prefix}ppindel [pin id] » Delete a pin from your personal pins. 
{Ghost.command_prefix}backupfriends » Backup all your friend's user IDs to a file.
{Ghost.command_prefix}backupservers » Backup all your servers and try to create invites for each one.
{Ghost.command_prefix}changehypesquad [bravery/brilliance/balance] » Change your hypesquad house.
{Ghost.command_prefix}stealpfp [@user] » Set someones avatar as your avatar.


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="selfbot", description="Selfbot related commands.", usage="selfbot")
    async def selfbot(ctx, page:int = 1):
        if __embedmode__:
            if page == 1:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__, description=f"""
`{Ghost.command_prefix}`**afkmode** » Toggle afk mode.
`{Ghost.command_prefix}`**settings** » The bot's settings.
`{Ghost.command_prefix}`**restart** » Restart Ghost selfbot.
`{Ghost.command_prefix}`**prefix [prefix]** » Set the command prefix.
`{Ghost.command_prefix}`**dumpchat [amount] (channel id) (oldest first, true/false)** » Get the chat's history.
`{Ghost.command_prefix}`**invite** » Get Ghost's Discord server invite link.
`{Ghost.command_prefix}`**addccmd [name] [response]** » Add a custom command.
`{Ghost.command_prefix}`**enablesniper [type, nitro/privnote/giveaway]** » Enable a sniper.
`{Ghost.command_prefix}`**disablesniper [type, nitro/privnote/giveaway]** » Disable a sniper.
`{Ghost.command_prefix}`**enabledetect [type, selfbot/..]** » Enable a detection.
`{Ghost.command_prefix}`**disabledetect [type, selfbot/..]** » Disable a detection.
`{Ghost.command_prefix}`**riskmode** » Disable and enable risk mode
            """)
                embed.set_author(name="Selfbot Commands (1/1)")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)     
            else:
                pass           
        else:
            await ctx.send(f"""```ini
[ Selfbot Commands ]

{Ghost.command_prefix}settings » The bot's settings.
{Ghost.command_prefix}restart » Restart Ghost selfbot.
{Ghost.command_prefix}prefix [prefix] » Set the command prefix.
{Ghost.command_prefix}dumpchat [amount] (channel id) (oldest first, true/false) » Get the chat's history.
{Ghost.command_prefix}invite » Get Ghost's Discord server invite link.
{Ghost.command_prefix}addccmd [name] [response] » Add a custom command.
{Ghost.command_prefix}enablesniper [type, nitro/privnote/giveaway] » Enable a sniper.
{Ghost.command_prefix}disablesniper [type, nitro/privnote/giveaway] » Disable a sniper.
{Ghost.command_prefix}enabledetect [type, selfbot/..] » Enable a detection.
{Ghost.command_prefix}disabledetect [type, selfbot/..] » Disable a detection.    
{Ghost.command_prefix}riskmode » Disable and enable risk mode


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="webhook", description="Webhook related commands.", usage="webhook")
    async def webhook(ctx, page:int = 1):
        if __embedmode__:
            if page == 1:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__, description=f"""
`{Ghost.command_prefix}`**delwebhook [id]** » Delete a webhook from the ID.
`{Ghost.command_prefix}`**newwebhook [name]** » Create a webhook in the command channel.
`{Ghost.command_prefix}`**spamwebhook [amount] [url] (message)** » Spam the shit out of a webhook.
`{Ghost.command_prefix}`**webhooksetup** » Creates a new server with webhooks.
`{Ghost.command_prefix}`**webhookinfo [id]** » Information about the webhook.
            """)
                embed.set_author(name="Webhook Commands (1/1)")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                pass
        else:
            await ctx.send(f"""```ini
[ Webhook Commands ]

{Ghost.command_prefix}delwebhook [id] » Delete a webhook from the ID.
{Ghost.command_prefix}newwebhook [name] » Create a webhook in the command channel.
{Ghost.command_prefix}spamwebhook [amount] [url] (message) » Spam the shit out of a webhook.
{Ghost.command_prefix}webhooksetup » Creates a new server with webhooks.
{Ghost.command_prefix}webhookinfo [id] » Information about the webhook.


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="abuse", description="Abuse related commands.", usage="abuse")
    async def abuse(ctx, page:int = 1):
        if __riskmode__:
            if __embedmode__:
                if page == 1:
                    embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__, description=f"""
`{Ghost.command_prefix}`**spam [amount] [delay] [message]** » Spam X amount of times.
`{Ghost.command_prefix}`**stopspam** » Stop spamming messages.
`{Ghost.command_prefix}`**dmspam [amount] [delay] [@user] [message]** » Spam DM messages X amount of times.
`{Ghost.command_prefix}`**channelspam [amount] [delay] [message]** » Spam a message X amount of times in every channel.
`{Ghost.command_prefix}`**threadspam [delay] [amount] [addusers | true/false] [name] [startmessage]** » Spam create threads with a starting message.
`{Ghost.command_prefix}`**ttsspam [amount] [delay] [message]** » Spam TTS messages X amount of times.
`{Ghost.command_prefix}`**reactspam [emoji] [messages]** » Spam reactions on X amount of messages.
`{Ghost.command_prefix}`**massghostping [delay] [@user]** » Ghost Ping the user in every channel.
`{Ghost.command_prefix}`**ghostping [@user]** » Ping a user then delete the message.
`{Ghost.command_prefix}`**massping (amount of messages) (send delay)** » Ping a mass amount of people in the command server.
`{Ghost.command_prefix}`**massnick [nickname]** » Change the nickname of all members in the command server.
`{Ghost.command_prefix}`**massdm [delay] [amount] [message]** » Send a DM message to everyone in the server.
`{Ghost.command_prefix}`**nukeserver** » Delete all roles and channels in the command server.
`{Ghost.command_prefix}`**destroyserver** » Completely destroy the command server.
`{Ghost.command_prefix}`**deletechannels** » Delete all of the command server's channels.
`{Ghost.command_prefix}`**deleteroles** » Delete all of the command server's roles.
`{Ghost.command_prefix}`**spamchannels [amount] (name)** » Spam create channels with a desired name. (Thanks Port <3)
`{Ghost.command_prefix}`**spamroles [amount] (name)** » Spam create roles with a desired name.
`{Ghost.command_prefix}`**raidjoin [delay] [invite]** » Make all your account tokens join a server.
`{Ghost.command_prefix}`**tokenraid [amount] [channel id] (message)** » Raid a server with all your account tokens.
`{Ghost.command_prefix}`**massban** » Ban all the members in the command server.
`{Ghost.command_prefix}`**masskick** » Kick all the members in the command server.
                """)
                    embed.set_author(name="Abuse Commands (1/1)")
                    embed.set_thumbnail(url=__embedimage__)
                    embed.set_image(url=__embedlargeimage__)
                    embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                    embed.timestamp = datetime.now()
                    await ctx.send(embed=embed, delete_after=__deletetimeout__)
                else:
                    pass         
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

{Ghost.command_prefix}spam [amount] [delay] [message] » Spam X amount of times.
{Ghost.command_prefix}stopspam » Stop spamming messages.
{Ghost.command_prefix}dmspam [amount] [delay] [@user] [message] » Spam DM messages X amount of times.
{Ghost.command_prefix}channelspam [amount] [delay] [message] » Spam X amount of times in all channels.
{Ghost.command_prefix}threadspam [delay] [amount] [name] [startmessage] » Spam create threads with a starting message.
{Ghost.command_prefix}ttsspam [amount] [delay] [message] » Spam TTS messages X amount of times.
{Ghost.command_prefix}reactspam [emoji] [messages] » Spam reactions on X amount of messages.
{Ghost.command_prefix}massghostping [delay] [@user] » Ghost Ping the user in every channel.
{Ghost.command_prefix}ghostping [@user] » Ping a user then delete the message.
{Ghost.command_prefix}massping » Ping a mass amount of people in the command server.
{Ghost.command_prefix}massnick [nickname] » Change the nickname of all members in the command server.
{Ghost.command_prefix}massdm [delay] [amount] [message] » Send a DM message to everyone in the server.
{Ghost.command_prefix}nukeserver » Delete all roles and channels in the command server.
{Ghost.command_prefix}destroyserver » Completely destroy the command server.
{Ghost.command_prefix}deletechannels » Delete all of the command server's channels.
{Ghost.command_prefix}deleteroles » Delete all of the command server's roles.
{Ghost.command_prefix}spamchannels [amount] (name) » Spam create channels with a desired name. (Thanks Port <3)
{Ghost.command_prefix}spamroles [amount] (name) » Spam create roles with a desired name.
{Ghost.command_prefix}raidjoin [delay] [invite] » Make all your account tokens join a server.
{Ghost.command_prefix}tokenraid [amount] [channel id] (message) » Raid a server with all your account tokens.
{Ghost.command_prefix}massban » Ban all the members in the command server.
{Ghost.command_prefix}masskick » Kick all the members in the command server.


# {__embedfooter__}```""", delete_after=__deletetimeout__)

        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                                          

    @Ghost.command(name="tools", description="Discord and other tools.", usage="tools")
    async def tools(ctx, page:int = 1):
        if __embedmode__:
            if page == 1:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}", color=__embedcolour__, description=f"""
`{Ghost.command_prefix}`**tokeninfo [token]** » Information about a token. 
`{Ghost.command_prefix}`**nuketoken [token]** » Nuke a token.
`{Ghost.command_prefix}`**checktoken [token]** » Checks if a token is working.
`{Ghost.command_prefix}`**checktokens** » Check your tokens. 
`{Ghost.command_prefix}`**nitrogen** » Generate a nitro code.
`{Ghost.command_prefix}`**tokengen** » Generate a discord user token.
`{Ghost.command_prefix}`**identitygen** » Generate a fake identity.
`{Ghost.command_prefix}`**passwordgen [length]** » Generate a secure password.
`{Ghost.command_prefix}`**ccgen** » Generate a fake Credit card.
            """)
                embed.set_author(name="Tools (1/1)")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                pass         
        else:
            await ctx.send(f"""```ini
[ Tools ]

{Ghost.command_prefix}tokeninfo [token] » Information about a token.
{Ghost.command_prefix}nuketoken [token] » Nuke a token.
{Ghost.command_prefix}checktoken [token] » Checks if a token is working.
{Ghost.command_prefix}checktokens » Check your tokens.
{Ghost.command_prefix}nitrogen » Generate a nitro code.
{Ghost.command_prefix}tokengen » Generate a discord user token.
{Ghost.command_prefix}identitygen » Generate a fake identity.
{Ghost.command_prefix}passwordgen [length] » Generate a secure password.
{Ghost.command_prefix}ccgen » Generate a fake Credit card.


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="giveaway", description="Giveaway related commands.", usage="giveaway")
    async def giveaway(ctx, page:int = 1):
        if __embedmode__:
            if page == 1:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}",
                                    color=__embedcolour__, description=f"""
`{Ghost.command_prefix}`**gstart [duration] [winners] [prize]** » Start a giveaway in the same channel
`{Ghost.command_prefix}`**gend [message id]** » End a giveaway
`{Ghost.command_prefix}`**greroll [message id]** » Re-roll a giveaway
            """)
                embed.set_author(name="Giveaway Commands (1/1)")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)  
            else:
                pass              
        else:
            await ctx.send(f"""```ini
[ Giveaway Commands ]

{Ghost.command_prefix}gstart [duration] [winners] [prize] » Start a giveaway in the same channel
{Ghost.command_prefix}gend [message id] » End a giveaway
{Ghost.command_prefix}greroll [message id] » Re-roll a giveaway


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="proxy", description="Proxy related commands.", usage="proxy")
    async def proxy(ctx, page:int=1):
        if __embedmode__:
            if page == 1:
                embed = discord.Embed(title=f"{__embedemoji__} **{__embedtitle__}** {__embedemoji__}",
                                    color=__embedcolour__, description=f"""
`{Ghost.command_prefix}`**proxies http** » Scrape HTTP proxies.
`{Ghost.command_prefix}`**proxies https** » Scrape HTTPS proxies.
`{Ghost.command_prefix}`**proxies socks4** » Scrape SOCKS4 proxies.
`{Ghost.command_prefix}`**proxies socks5** » Scrape SOCKS5 proxies.
`{Ghost.command_prefix}`**proxies all** » Scrape HTTP, HTTPS, SOCKS4 AND SOCKS5 proxies.
            """)
                embed.set_author(name="Proxy Commands (1/1)")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_image(url=__embedlargeimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)  
            else:
                pass              
        else:
            await ctx.send(f"""```ini
[ Giveaway Commands ]

{Ghost.command_prefix}proxies http » Scrape HTTP proxies.
{Ghost.command_prefix}proxies https » Scrape HTTPS proxies.
{Ghost.command_prefix}proxies socks4 » Scrape SOCKS4 proxies.
{Ghost.command_prefix}proxies socks5 » Scrape SOCKS5 proxies.
{Ghost.command_prefix}proxies all » Scrape HTTP, HTTPS, SOCKS4 AND SOCKS5 proxies.


# {__embedfooter__}```""", delete_after=__deletetimeout__)


    @Ghost.command(name="hiddenchannels", description="Sends a list of all the channels you cant see.", usage="hiddenchannels (guild id)")
    async def hiddenchannels(ctx, guild=None):
        if guild == None:
            guild = ctx.guild
        else:
            guild = await Ghost.fetch_guild(int(guild))
        hiddenChannels = []

        message = await ctx.send("Looking for hidden channels, this could take a while...")

        for channel in guild.channels:
            if str(channel.type).lower() != "category":
                request = requests.get(f"https://discord.com/api/channels/{channel.id}", headers={"Authorization": __token__, "User-Agent": get_random_user_agent()})
                if request.status_code != 200:
                    if __embedmode__:
                        hiddenChannels.append("#"+channel.name)
                    else:
                        hiddenChannels.append(channel.name)
                    print_info(f"{channel.name} is hidden.")
                else:
                    print_info(f"{channel.name} is not hidden.")
                # await asyncio.sleep(1)

        if __embedmode__:
            embed = discord.Embed(title=f"Hidden Channels", description=f"There is a total of `{len(hiddenChannels)}` hidden channels.\n \n```{', '.join(hiddenChannels)}```", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await message.edit(content="", embed=embed, delete_after=__deletetimeout__) 
        else:
            await message.edit(content=f"""```ini
[ Hidden Channels ]

There is a total of {len(hiddenChannels)} hidden channels.

{', '.join(hiddenChannels)}


# {__embedfooter__}
```""", delete_after=__deletetimeout__) 

    @Ghost.command(name="clearconsole", description="Clear your console.", usage="clearconsole", aliases=["resetconsole", "consoleclear", "consolereset"])
    async def clearconsole(ctx):
        width = os.get_terminal_size().columns

        if is_windows():
            os.system("cls")
            os.system(f"title Ghost [{version}] [{Ghost.user}]")

        # if is_windows():
        #     def startupPath():
        #         return str(shell.SHGetFolderPath(0, (shellcon.CSIDL_STARTUP, shellcon.CSIDL_COMMON_STARTUP)[0], None, 0))

        #     os.system("cls")
        #     os.system(f"title Ghost [{version}] [{Ghost.user}]")
            
        #     if (CONFIG["load_on_startup"] == True):
        #         print("Adding to startup.......")
        #         USER_NAME = getpass.getuser()

        #         def add_to_startup(file_path=""):
        #             if file_path == "":
        #                 file_path = os.path.dirname(os.path.realpath(__file__))
                    
        #             bat_file = open(startupPath() + r"\\Ghost.bat", "w")
        #             bat_file.write(f"cd {file_path}\nstart Ghost")   
        #             bat_file.close()

        #         add_to_startup()   

        #     else:
        #         print("Removing from startup......")
        #         if os.path.exists(startupPath() + r"\\Ghost.bat"): os.remove(startupPath() + r"\\Ghost.bat");

        #     os.system("cls")
        if is_linux():
            os.system("clear")
        if consoleMode.lower() == "new":
            print("")
            print(fg.consoleColour + "")                    
            print(" ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗".center(width))
            print("██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝".center(width))
            print("██║  ███╗███████║██║   ██║███████╗   ██║   ".center(width))
            print("██║   ██║██╔══██║██║   ██║╚════██║   ██║   ".center(width))
            print("╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ".center(width))
            print(" ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ".center(width))
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")  
        if consoleMode.lower() == "rainbow":
            print("")
            print(fg.consoleColour + "")                    
            print(fg.cRed + " ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗".center(width))
            print(fg.cOrange + "██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝".center(width))
            print(fg.cYellow + "██║  ███╗███████║██║   ██║███████╗   ██║   ".center(width))
            print(fg.cGreen + "██║   ██║██╔══██║██║   ██║╚════██║   ██║   ".center(width))
            print(fg.cBlue + "╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ".center(width))
            print(fg.cPurple + " ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ".center(width))
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")                                       
        if consoleMode.lower() == "new2":
            print("")
            print(fg.consoleColour + "")                    
            print(" ______     __  __     ______     ______     ______  ".center(width))
            print("/\  ___\   /\ \_\ \   /\  __ \   /\  ___\   /\__  _\ ".center(width))
            print("\ \ \__ \  \ \  __ \  \ \ \/\ \  \ \___  \  \/_/\ \/ ".center(width))
            print(" \ \_____\  \ \_\ \_\  \ \_____\  \/\_____\    \ \_\ ".center(width))
            print("  \/_____/   \/_/\/_/   \/_____/   \/_____/     \/_/ ".center(width))
            print("                                                     ".center(width)) 
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")                      
        if consoleMode.lower() == "new3":
            print("")
            print(fg.consoleColour + "")                    
            print("            88                                         ".center(width))
            print("            88                                  ,d     ".center(width))
            print("            88                                  88     ".center(width))
            print(" ,adPPYb,d8 88,dPPYba,   ,adPPYba,  ,adPPYba, MM88MMM  ".center(width))
            print('a8"    `Y88 88P\'    "8a a8"     "8a I8[    ""   88     '.center(width))
            print('8b       88 88       88 8b       d8  `"Y8ba,    88     '.center(width))                       
            print('"8a,   ,d88 88       88 "8a,   ,a8" aa    ]8I   88,    '.center(width))                       
            print(' `"YbbdP"Y8 88       88  `"YbbdP"\'  `"YbbdP"\'   "Y888  '.center(width))                       
            print(' aa,    ,88                                            '.center(width))                       
            print('  "Y8bbdP"                                             '.center(width))  
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")                    
        if consoleMode.lower() == "new4":
            print("")
            print(fg.consoleColour + "")                    
            print("   ▄██████▄     ▄█    █▄     ▄██████▄     ▄████████     ███     ".center(width))
            print("  ███    ███   ███    ███   ███    ███   ███    ███ ▀█████████▄ ".center(width))
            print("  ███    █▀    ███    ███   ███    ███   ███    █▀     ▀███▀▀██ ".center(width))
            print(" ▄███         ▄███▄▄▄▄███▄▄ ███    ███   ███            ███   ▀ ".center(width))
            print('▀▀███ ████▄  ▀▀███▀▀▀▀███▀  ███    ███ ▀███████████     ███     '.center(width))
            print('  ███    ███   ███    ███   ███    ███          ███     ███     '.center(width))                       
            print('  ███    ███   ███    ███   ███    ███    ▄█    ███     ███     '.center(width))                       
            print('  ████████▀    ███    █▀     ▀██████▀   ▄████████▀     ▄████▀   '.center(width))         
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")                                                                              
        if consoleMode.lower() == "bear":
            if is_windows():
                os.system("mode con: cols=90 lines=24")                    
            print("")
            print(fg.consoleColour + "")                    
            print("     ▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄      ".center(os.get_terminal_size().columns))
            print("     █▒▒░░░░░░░░░▒▒█      ".center(os.get_terminal_size().columns))
            print("      █░░█░░░░░█░░█       ".center(os.get_terminal_size().columns))
            print("   ▄▄  █░░░▀█▀░░░█   ▄▄   ".center(os.get_terminal_size().columns))
            print("  █░░█ ▀▄░░░░░░░▄▀  █░░█  ".center(os.get_terminal_size().columns))
            print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█".center(os.get_terminal_size().columns))                                      
            print("█░█▀▀░░█ █░░█▀█░░█▀░░▀█▀░█".center(os.get_terminal_size().columns))                                      
            print("█░█▄█░░█▀█░░█▄█░░▄█░░ █ ░█".center(os.get_terminal_size().columns))                                      
            print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█".center(os.get_terminal_size().columns))    
            print("")
            print(fg.cWhite + f"{motd}".center(os.get_terminal_size().columns))
            print(fg.consoleColour + '─'*os.get_terminal_size().columns)
            print("")                                                      
        elif consoleMode.lower() == "old":
            print("")
            print(fg.consoleColour + "")                    
            print("  ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓".center(width))
            print(" ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒".center(width))
            print("▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░".center(width))
            print("░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░ ".center(width))
            print("░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ ".center(width))
            print(" ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ".center(width))                    
            print("  ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░    ".center(width))                    
            print("░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░      ".center(width))                    
            print("      ░  ░  ░  ░    ░ ░        ░           ".center(width))  
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")                    
        elif consoleMode not in consoleModes:
            print("")
            print(fg.consoleColour + "")                    
            print(" ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗".center(width))
            print("██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝".center(width))
            print("██║  ███╗███████║██║   ██║███████╗   ██║   ".center(width))
            print("██║   ██║██╔══██║██║   ██║╚════██║   ██║   ".center(width))
            print("╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ".center(width))
            print(" ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ".center(width))                                      
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")
        if consoleMode.lower() == "react":
            print("")
            print(fg.consoleColour + "")                    
            print("██████╗ ███████╗ █████╗  ██████╗████████╗".center(width))
            print("██╔══██╗██╔════╝██╔══██╗██╔════╝╚══██╔══╝".center(width))
            print("██████╔╝█████╗  ███████║██║        ██║   ".center(width))
            print("██╔══██╗██╔══╝  ██╔══██║██║        ██║   ".center(width))
            print("██║  ██║███████╗██║  ██║╚██████╗   ██║   ".center(width))
            print("╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ".center(width))
            print("")
            print(fg.cWhite + f"{motd}".center(width))
            print(fg.consoleColour + '─'*width)
            print("")  
        if consoleMode.lower() == "rise":
            print(fg.cBlue + "")                    
            print("██████╗ ██╗███████╗███████╗    ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗".center(width))
            print("██╔══██╗██║██╔════╝██╔════╝    ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝".center(width))
            print("██████╔╝██║███████╗█████╗      ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   ".center(width))
            print("██╔══██╗██║╚════██║██╔══╝      ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   ".center(width))
            print("██║  ██║██║███████║███████╗    ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   ".center(width))
            print("╚═╝  ╚═╝╚═╝╚══════╝╚══════╝    ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   ".center(width))
            print("╭─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╮")
            print(fg.cGrey + f"Connected: {Ghost.user} | Prefix: {Ghost.command_prefix} | Servers: {len(Ghost.guilds)}".center(width))
            print(fg.cBlue + "╰─━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━─╯")
            print("")
            print(fg.cBlue + '━'*width)
            print("")         

        if consoleMode.lower() == "nighty":
            if is_windows():
                os.system("mode con: cols=90 lines=24")
            print("")                    
            print(f"                     {fg.cWhite}███{fg.consoleColour}╗   {fg.cWhite}██{fg.consoleColour}╗{fg.cWhite}██{fg.consoleColour}╗ {fg.cWhite}██████{fg.consoleColour}╗ {fg.cWhite}██{fg.consoleColour}╗  {fg.cWhite}██{fg.consoleColour}╗{fg.cWhite}████████{fg.consoleColour}╗{fg.cWhite}██{fg.consoleColour}╗   {fg.cWhite}██{fg.consoleColour}╗")
            print(f"                     {fg.cWhite}████{fg.consoleColour}╗  {fg.cWhite}██{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}╔════╝ {fg.cWhite}██{fg.consoleColour}║  {fg.cWhite}██{fg.consoleColour}║╚══{fg.cWhite}██{fg.consoleColour}╔══╝╚{fg.cWhite}██{fg.consoleColour}╗ {fg.cWhite}██{fg.consoleColour}╔╝")
            print(f"                     {fg.cWhite}██{fg.consoleColour}╔{fg.cWhite}██{fg.consoleColour}╗ {fg.cWhite}██{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}║  {fg.cWhite}███{fg.consoleColour}╗{fg.cWhite}███████{fg.consoleColour}║   {fg.cWhite}██{fg.consoleColour}║    ╚{fg.cWhite}████{fg.consoleColour}╔╝ ")
            print(f"                     {fg.cWhite}██{fg.consoleColour}║╚{fg.cWhite}██{fg.consoleColour}╗{fg.cWhite}██{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}║   {fg.cWhite}██{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}╔══{fg.cWhite}██{fg.consoleColour}║   {fg.cWhite}██{fg.consoleColour}║     ╚{fg.cWhite}██{fg.consoleColour}╔╝  ")
            print(f"                     {fg.cWhite}██{fg.consoleColour}║ ╚{fg.cWhite}████{fg.consoleColour}║{fg.cWhite}██{fg.consoleColour}║╚{fg.cWhite}██████{fg.consoleColour}╔╝{fg.cWhite}██{fg.consoleColour}║  {fg.cWhite}██{fg.consoleColour}║   {fg.cWhite}██{fg.consoleColour}║      {fg.cWhite}██{fg.consoleColour}║   ")
            print(fg.consoleColour + f"                     ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ")
            print("")
            print(f"{fg.cWhite}Status:    {fg.cGreen}Connected")
            print(f"{fg.cWhite}Account:   {Ghost.user} [{len(Ghost.guilds)} servers] [{len(get_friends(__token__))} friends]")
            print(f"{fg.cWhite}Prefix:    {Ghost.command_prefix}")
            print(fg.cWhite + '─'*os.get_terminal_size().columns)                                                          

            # def getCurrentTime():
            #     return datetime.now().strftime("%H:%M")
            # def print_important(message):
            #     print(f"{fg.cGrey}{getCurrentTime()} | {fg.cPurple}[Important] {fg.cGrey} | {message}")    
            # def print_info(message):
            #     print(f"{fg.cGrey}{getCurrentTime()} | {fg.cYellow}[Information] {fg.cGrey} | {message}")
            # def print_cmd(command):
            #     print(f"{fg.cGrey}{getCurrentTime()} | {fg.consoleColour}[Command] {fg.cGrey} | {Ghost.command_prefix}{command}")
            # def print_sharecmd(author, command):
            #     print(f"{fg.cGrey}[{getCurrentTime()}] {fg.consoleColour}[SHARE COMMAND] {fg.cWhite}({author}) {command}")
            # def print_error(error):
            #     print(f"{fg.cGrey}{getCurrentTime()} | {fg.cRed}[Error] {fg.cGrey} | {error}")
            # def print_detect(message):
            #     print(f"{fg.cGrey}{getCurrentTime()} | {fg.cPink}[Detect] {fg.cGrey} | {message}")
            # def print_sniper(message):
            #     print(f"{fg.cGrey}{getCurrentTime()} | {fg.cOrange}[Sniper] {fg.cGrey} | {message}")
            # def print_sniper_info(firstmessage, secondmessage):
            #     print(f"{fg.cGrey}{getCurrentTime()} | {fg.cOrange}[Sniper] {fg.cGrey} | {firstmessage} | {secondmessage}")


        if "beta" in version.lower():
            print_important("You're currently using a beta build of Ghost.")
            print_important("If you notice any bugs please report them to the developer.")
            print(" ")
        elif "dev" in version.lower():
            print_important("You're currently using a developer build of Ghost.")
            print_important("If you notice any bugs please report them to the developer.")
            print(" ")                      

    @Ghost.command(name="blocksend", description="Send a message to a blocked user.", usage="blocksend [user id] [messages]", aliases=["sendblocked", "sendtoblocked"])
    async def blocksend(ctx, userid:int, *, message):
        user = await Ghost.fetch_user(userid)
        await user.unblock()
        await user.send(message)
        await user.block()

        if __embedmode__:
            embed = discord.Embed(title=f"Block Send", description=f"Sent `{message}` to {user}.", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__) 
        else:
            await ctx.send(f"Sent `{message}` to {user}.", delete_after=__deletetimeout__) 

    @Ghost.command(name="riskmode", description="Disable and enable risk mode", usage="riskmode")
    async def riskmode(ctx):
        global __riskmode__
        riskModeText = ""

        if __riskmode__:
            __riskmode__ = False
            cfg = Config.getConfig()
            cfg["riskmode"] = False
            Config.saveConfig(cfg)
            riskModeText = "disabled"
        else:
            __riskmode__ = True
            cfg = Config.getConfig()
            cfg["riskmode"] = True
            Config.saveConfig(cfg)
            riskModeText = "enabled"         

        if __embedmode__:
            embed = discord.Embed(description=f"Risk mode has been {riskModeText}.", color=__embedcolour__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__) 
        else:
            await ctx.send(f"Risk mode has been {riskModeText}.", delete_after=__deletetimeout__)  

    @Ghost.command(name="embedmode", description="Toggle embed mode.", usage="embedmode")
    async def embedmode(ctx):
        global __embedmode__
        if not __embedmode__:
            __embedmode__ = True
            cfg = Config.getConfig()
            cfg["embed_mode"] = True
            Config.saveConfig(cfg)
            if __embedmode__:
                embed = discord.Embed(title=f"Embed mode has been enabled.", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__) 
            else:
                await ctx.send("Embed mode has been enabled.", delete_after=__deletetimeout__) 
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Embed mode is already enabled.", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)    
            else:
                await ctx.send("Embed mode is already enabled.", delete_after=__deletetimeout__)

    @Ghost.command(name="textmode", description="Toggle text mode.", usage="textmode")
    async def textmode(ctx):
        global __embedmode__
        if __embedmode__:
            __embedmode__ = False
            cfg = Config.getConfig()
            cfg["embed_mode"] = False
            Config.saveConfig(cfg)
            if __embedmode__:
                embed = discord.Embed(title=f"Text mode has been enabled.", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)    
            else:
                await ctx.send("Text mode has been enabled.", delete_after=__deletetimeout__)
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Text mode is already enabled.", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)    
            else:
                await ctx.send("Text mode is already enabled.", delete_after=__deletetimeout__)                    

    @Ghost.command(name="readall", description="Mark every message as read.", usage="readall")
    async def readall(ctx):
        index = 0
        index2 = 0
        DiscumClient = discum.Client(token=__token__, log=False)
        for guild in Ghost.guilds:
            messages2 = []
            for channel in guild.text_channels:
                index+=1
                try:
                    messages = await channel.history(limit=1, oldest_first=False).flatten()
                    for message in messages:
                        index2+=1
                        messages2.append({"channel_id": str(channel.id), "message_id": str(message.id)})
                    print_info(f"({channel.name}) Fetched new messages to read.")
                except:
                    pass
            DiscumClient.bulkAck(messages2)
            print_info(f"Read all messages in {guild.name}.")
        print_info("All messages have been read.")
        await ctx.send(f"Read a total of `{index}` channels and `{index2}` messages.")

    @Ghost.command(name="specs", description="Your computers specifications.", usage="specs", aliases=["computerspecs", "pcspecs", "specifications"])
    async def specs(ctx):
        def get_size(bytes, suffix="B"):
            factor = 1024
            for unit in ["", "K", "M", "G", "T", "P"]:
                if bytes < factor:
                    return f"{bytes:.2f}{unit}{suffix}"
                bytes /= factor

        uname = platform.uname()
        svmem = psutil.virtual_memory()

        system = uname.system
        machine = uname.machine
        cpu = platform.processor()
        ram = str(get_size(svmem.used)) + "/" + str(get_size(svmem.total))
        gpus = []
        for gpu in GPUtil.getGPUs():
            gpus.append(gpu.name)

        if __embedmode__:
            embed = discord.Embed(title="Specifications", color=__embedcolour__)
            embed.add_field(name="System", value=f"```{system}```")
            embed.add_field(name="Machine", value=f"```{machine}```")
            embed.add_field(name="RAM", value=f"```{ram}```")
            embed.add_field(name="CPU", value=f"```{cpu}```")
            embed.add_field(name="GPUs", value=f"```{', '.join(gpus)}```")
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.set_thumbnail(url=__embedimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send(f"""```ini
[ Specifications ]

System: {system}
Machine: {machine}
CPU: {cpu}
GPUs: {', '.join(gpus)}
RAM: {ram}


# {__embedfooter__}
```""", delete_after=__deletetimeout__)

    @Ghost.command(name="crypto", description="Get the current data on a cryptocurrency.", usage="crypto [currency]", aliases=["cryptodata"])
    async def crypto(ctx, *, currency="bitcoin"):
        request = requests.get(f"https://api.coingecko.com/api/v3/coins/{currency}")
        if request.status_code == 200:
            request = request.json()
            if __embedmode__:
                embed = discord.Embed(title=f"{request['name']} Data", color=__embedcolour__)
                embed.add_field(name="Scores", value=f"""```
Coingecko score: {request['coingecko_score']}
Liquidity score: {request['liquidity_score']}
Developer score: {request['developer_score']}
Commuinity score: {request['community_score']}
```""", inline=False)
                embed.add_field(name="Current Prices", value=f"""```
USD: {'{:,}'.format(request['market_data']['current_price']['usd'])}
CAD: {'{:,}'.format(request['market_data']['current_price']['cad'])}
AUD: {'{:,}'.format(request['market_data']['current_price']['aud'])}
GBP: {'{:,}'.format(request['market_data']['current_price']['gbp'])}
EUR: {'{:,}'.format(request['market_data']['current_price']['eur'])}
```""", inline=False)
                embed.add_field(name="Last 24h Price Change", value=f"""```
USD: {'{:,}'.format(request['market_data']['price_change_24h_in_currency']['usd'])}
CAD: {'{:,}'.format(request['market_data']['price_change_24h_in_currency']['cad'])}
AUD: {'{:,}'.format(request['market_data']['price_change_24h_in_currency']['aud'])}
GBP: {'{:,}'.format(request['market_data']['price_change_24h_in_currency']['gbp'])}
EUR: {'{:,}'.format(request['market_data']['price_change_24h_in_currency']['eur'])}
```""", inline=False)
                embed.set_thumbnail(url=request["image"]["large"])
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()    
                await ctx.send(embed=embed)  
            else:
                await ctx.send(f"""```ini
[ {request['name']} Data ]

[Scores]
Coingecko score: {request['coingecko_score']}
Liquidity score: {request['liquidity_score']}
Developer score: {request['developer_score']}
Commuinity score: {request['community_score']}

[Current Prices]
USD: {'{:,}'.format(request['market_data']['current_price']['usd'])}
CAD: {'{:,}'.format(request['market_data']['current_price']['cad'])}
AUD: {'{:,}'.format(request['market_data']['current_price']['aud'])}
GBP: {'{:,}'.format(request['market_data']['current_price']['gbp'])}
EUR: {'{:,}'.format(request['market_data']['current_price']['eur'])}

[Last 24h Price Change]
USD: {'{:,}'.format(request['market_data']['price_change_24h_in_currency']['usd'])}
CAD: {'{:,}'.format(request['market_data']['price_change_24h_in_currency']['cad'])}
AUD: {'{:,}'.format(request['market_data']['price_change_24h_in_currency']['aud'])}
GBP: {'{:,}'.format(request['market_data']['price_change_24h_in_currency']['gbp'])}
EUR: {'{:,}'.format(request['market_data']['price_change_24h_in_currency']['eur'])}


# {__embedfooter__}
```""")              
        else:
            if __embedmode__:
                embed = discord.Embed(title="Invalid Crypto", description="That crypto currency doesnt exist or there was an error.", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()    
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"""```ini
[ Invalid Crypto ]

That crypto currency doesnt exist or there was an error.


# {__embedfooter__}
```""")

    @Ghost.command(name="proxies", description="Scrape an type of proxy.", usage="proxies [http, https, socks4, socks5, all]", aliases=["proxygen", "genproxies"])
    async def proxies(ctx, type):
        if type == "http":
            if not os.path.isdir("data/proxies/"): os.makedirs("data/proxies/");
            file = open("data/proxies/http.txt", "a+")
            request = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000")
            proxies = []
            for proxy in request.text.split("\n"):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)
                    file.write(str(proxy)+"\n")
            file.close()
            await ctx.send(content=f"Scraped `{len(proxies)}` HTTP proxies.", file=discord.File("data/proxies/http.txt"))

        if type == "https":
            if not os.path.isdir("data/proxies/"): os.makedirs("data/proxies/");
            file = open("data/proxies/https.txt", "a+")
            request = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=5000")
            proxies = []
            for proxy in request.text.split("\n"):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)
                    file.write(str(proxy)+"\n")
            file.close()
            await ctx.send(content=f"Scraped `{len(proxies)}` HTTPS proxies.", file=discord.File("data/proxies/https.txt"))  

        if type == "socks4":
            if not os.path.isdir("data/proxies/"): os.makedirs("data/proxies/");
            file = open("data/proxies/socks4.txt", "a+")
            request = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=5000")
            proxies = []
            for proxy in request.text.split("\n"):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)
                    file.write(str(proxy)+"\n")
            file.close()
            await ctx.send(content=f"Scraped `{len(proxies)}` SOCKS4 proxies.", file=discord.File("data/proxies/socks4.txt"))   

        if type == "socks5":
            if not os.path.isdir("data/proxies/"): os.makedirs("data/proxies/");
            file = open("data/proxies/socks5.txt", "a+")
            request = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000")
            proxies = []
            for proxy in request.text.split("\n"):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)
                    file.write(str(proxy)+"\n")
            file.close()
            await ctx.send(content=f"Scraped `{len(proxies)}` SOCKS5 proxies.", file=discord.File("data/proxies/socks5.txt"))

        if type == "all":
            if not os.path.isdir("data/proxies/"): os.makedirs("data/proxies/");
            file = open("data/proxies/all.txt", "a+")
            request = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=5000")
            proxies = []
            for proxy in request.text.split("\n"):
                proxy = proxy.strip()
                if proxy:
                    proxies.append(proxy)
                    file.write(str(proxy)+"\n")
            file.close()
            await ctx.send(content=f"Scraped `{len(proxies)}` HTTP, HTTPS, SOCKS4 AND SOCKS5 proxies.", file=discord.File("data/proxies/all.txt"))                                                                               

    @Ghost.command(name="stealpfp", description="Set someones avatar as your avatar.", usage="stealpfp [@user]", aliases=["stealavatar"])
    async def stealpfp(ctx, user:discord.User):
        DiscumClient = discum.Client(token=__token__, log=False, user_agent=get_random_user_agent())
        avatar1 = user.avatar
        extension = str(avatar1)[:-10][-3:]
        open(f"data/pfpstealavatar.{extension}", "wb").write(requests.get(str(avatar1), allow_redirects=True).content)
        DiscumClient.setAvatar(f"data/pfpstealavatar.{extension}")
        await ctx.send(f"Stolen `{user}`'s avatar.", delete_after=__deletetimeout__)

    # @Ghost.command(name="stealusername", description="Steal someones username.", usage="stealusername [@user]", aliases=["stealname"])
    # async def stealusername(ctx, user:discord.User):
    #     DiscumClient = discum.Client(token=__token__, log=False, user_agent=get_random_user_agent())
    #     username = user.name
    #     DiscumClient.setUsername(username)
    #     await ctx.send(f"Stolen `{user}`'s username.", delete_after=__deletetimeout__) 

    # @Ghost.command(name="stealprofile", description="Steal someones avatar and username.", usage="stealprofile [@user]")
    # async def stealprofile(ctx, user:discord.User):
    #     DiscumClient = discum.Client(token=__token__, log=False, user_agent=get_random_user_agent())
    #     avatar = user.avatar
    #     username = user.name
    #     extension = str(avatar)[:-10][-3:]
    #     open(f"data/pfpstealavatar.{extension}", "wb").write(requests.get(str(avatar), allow_redirects=True).content)
    #     DiscumClient.setAvatar(f"data/pfpstealavatar.{extension}") 
    #     DiscumClient.setUsername(username)           

    @Ghost.command(name="cloneemoji", description="Clone an emoji to the command server.", usage="cloneemoji [emoji]", aliases=["stealemoji"])
    async def cloneemoji(ctx, *, msg):
        msg = re.sub("<:(.+):([0-9]+)>", "\\2", msg)

        match = None
        exact_match = False
        for guild in Ghost.guilds:
            for emoji in guild.emojis:
                if msg.strip().lower() in str(emoji):
                    match = emoji
                if msg.strip() in (str(emoji.id), emoji.name):
                    match = emoji
                    exact_match = True
                    break
            if exact_match:
                break

        if not match:
            return await ctx.send("Couldnt find that emoji.")

        response = requests.get(match.url)
        emoji = await ctx.guild.create_custom_emoji(name=match.name, image=response.content)
        await ctx.send(f"Successfully cloned `{emoji.name}`.")                

    @Ghost.command(name="enabledetect", description="Enable a detection.", usage="enabledetect [type, selfbot/ghostping/bans/deletedmessages/webhookmodification]")
    async def enabledetect(ctx, *, type):
        if type.lower() == "selfbot":
            global __selfbotdetect__
            __selfbotdetect__ = True
            CONFIG["detections"]["selfbot"] = True
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False)
            await ctx.send("Selfbot detection has been enabled.", delete_after=__deletetimeout__)
        if type.lower() == "ghostping":
            global __ghostpingdetect__
            __ghostpingdetect__ = True
            CONFIG["detections"]["ghostping"] = True
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False)
            await ctx.send("Ghostping detection has been enabled.", delete_after=__deletetimeout__)    
        if type.lower() == "bans":
            global __bandetect__
            __bandetect__ = True
            CONFIG["detections"]["bans"] = True
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False)
            await ctx.send("Ban detection has been enabled.", delete_after=__deletetimeout__)    
        if type.lower() == "deletedmessages":
            global __deletedmessagesdetect__
            __deletedmessagesdetect__ = True
            CONFIG["detections"]["deletedmessages"] = True
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False)
            await ctx.send("Deleted messages detection has been enabled.", delete_after=__deletetimeout__)    
        if type.lower() == "webhookmodification":
            global __webhookmodificationdetect__
            __webhookmodificationdetect__ = True
            CONFIG["detections"]["webhookmodification"] = True
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False)
            await ctx.send("Webhook modification detection has been enabled.", delete_after=__deletetimeout__)                                                       
        else:
            await ctx.send("Invalid type.", delete_after=__deletetimeout__)

    @Ghost.command(name="disabledetect", description="Disable a detection.", usage="disabledetect [type, selfbot/ghostping/bans/deletedmessages/webhookmodification]")
    async def disabledetect(ctx, *, type):
        if type.lower() == "selfbot":
            global __selfbotdetect__
            __selfbotdetect__ = False
            CONFIG["detections"]["selfbot"]  = False
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False)
            await ctx.send("Selfbot detection has been disabled.", delete_after=__deletetimeout__)
        if type.lower() == "ghostping":
            global __ghostpingdetect__
            __selfbotdetect__ = False
            CONFIG["detections"]["ghostping"]  = False
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False)
            await ctx.send("Ghostping detection has been disabled.", delete_after=__deletetimeout__)           
        if type.lower() == "bans":
            global __bandetect__
            __bandetect__ = False
            CONFIG["detections"]["bans"]  = False
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False)
            await ctx.send("Ban detection has been disabled.", delete_after=__deletetimeout__)  
        if type.lower() == "deletedmessages":
            global __deletedmessagesdetect__
            __deletedmessagesdetect__ = False
            CONFIG["detections"]["deletedmessages"]  = False
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False)
            await ctx.send("Deleted messages detection has been disabled.", delete_after=__deletetimeout__)     
        if type.lower() == "webhookmodification":
            global __webhookmodificationdetect__
            __webhookmodificationdetect__ = False
            CONFIG["detections"]["webhookmodification"]  = False
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False)
            await ctx.send("Webhook modifcation detection has been disabled.", delete_after=__deletetimeout__)                                                                 
        else:
            await ctx.send("Invalid type.", delete_after=__deletetimeout__)

    @Ghost.command(name="enablesniper", description="Enable a sniper.", usage="enablesniper [type, nitro/privnote/giveaway/tickets]")
    async def enablesniper(ctx, *, type):
        if type.lower() == "nitro":
            global __nitrosniper__
            __nitrosniper__ = True
            CONFIG["snipers"]["nitro"] = True
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False)
            await ctx.send("Nitro sniper has been enabled.", delete_after=__deletetimeout__)
        elif type.lower() == "privnote":
            global __privnotesniper__
            __privnotesniper__ = True
            CONFIG["snipers"]["privnote"] = True
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False) 
            await ctx.send("Privnote sniper has been enabled.", delete_after=__deletetimeout__)  
        elif type.lower() == "giveaway":
            global __giveawaysniper__
            __giveawaysniper__ = True
            CONFIG["snipers"]["giveaway"] = True
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False)    
            await ctx.send("Giveaway sniper has been enabled.", delete_after=__deletetimeout__)        
        elif type.lower() == "tickets":
            global __ticketsniper__
            __ticketsniper__ = True
            CONFIG["snipers"]["tickets"] = True
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False)    
            await ctx.send("Ticket sniper has been enabled.", delete_after=__deletetimeout__)                                                
        else:
            await ctx.send("Invalid type.", delete_after=__deletetimeout__)

    @Ghost.command(name="disablesniper", description="Disable a sniper.", usage="disablesniper [type, nitro/privnote/giveaway/tickets]")
    async def disablesniper(ctx, *, type):
        if type.lower() == "nitro":
            global __nitrosniper__
            __nitrosniper__ = False
            CONFIG["snipers"]["nitro"] = False
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False)
            await ctx.send("Nitro sniper has been disabled.", delete_after=__deletetimeout__)
        elif type.lower() == "privnote":
            global __privnotesniper__
            __privnotesniper__ = False
            CONFIG["snipers"]["privnote"] = False
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False)  
            await ctx.send("Privnote sniper has been disabled.", delete_after=__deletetimeout__) 
        elif type.lower() == "giveaway":
            global __giveawaysniper__
            __giveawaysniper__ = False
            CONFIG["snipers"]["giveaway"] = False
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False) 
            await ctx.send("Giveaway sniper has been disabled.", delete_after=__deletetimeout__)
        elif type.lower() == "tickets":
            global __ticketsniper__
            __ticketsniper__ = False
            CONFIG["snipers"]["tickets"] = False
            json.dump(CONFIG, open("config.json", "w"), indent=4, sort_keys=False) 
            await ctx.send("Ticket sniper has been disabled.", delete_after=__deletetimeout__)                    
        else:
            await ctx.send("Invalid type.", delete_after=__deletetimeout__)                    

#             @Ghost.command(name="ghostusers", description="Finds all the people using Ghost in a server.", usage="ghostusers")
#             @commands.guild_only()
#             async def ghostusers(ctx):
#                 message = await ctx.send("Looking for people that have Ghost, this may take a while...")

#                 ghostUsers = []
#                 userAgent = get_random_user_agent()
#                 try:
#                     await ctx.message.delete()
#                 except:
#                     pass
#                 DiscumClient = discum.Client(token=__token__, user_agent=f"{userAgent}")
#                 @DiscumClient.gateway.command
#                 def getmembers(resp):
#                     guild_id = f'{ctx.guild.id}'
#                     channel_id = f'{ctx.channel.id}'
#                     if resp.event.ready_supplemental:
#                         DiscumClient.gateway.fetchMembers(guild_id, channel_id, wait=1)
#                     if DiscumClient.gateway.finishedMemberFetching(guild_id):
#                         DiscumClient.gateway.removeCommand(getmembers)
#                         DiscumClient.gateway.close()

#                 DiscumClient.gateway.run()

#                 for memberID in DiscumClient.gateway.session.guild(f'{ctx.guild.id}').members:
#                     member = await ctx.guild.fetch_member(int(memberID))
#                     ghostguild = await Ghost.fetch_guild(838869729829191681)
#                     mutualGuilds = member.mutual_guilds
#                     for guild in mutualGuilds:
#                         print(guild.name)

#                 DiscumClient.gateway.close()

#                 if __embedmode__:
#                     embed=discord.Embed(
#                         title="Ghost Users",
#                         description=f"There are a total of `{len(ghostUsers)}` Ghost users in `{ctx.guild.name}`\n \n```\n" + ", ".join(ghostUsers) + f"\n```",
#                         color=__embedcolour__
#                     )
#                     embed.set_thumbnail(url=__embedimage__)
#                     embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
#                     embed.timestamp = datetime.now()

#                     await message.edit(content="", embed=embed)
#                 else:
#                     await message.edit(content=f"""```ini
# [ Ghost Users ]

# There is a total of {len(ghostUsers)} in {ctx.guild.name}.

# {', '.join(ghostUsers)}


# # {__embedfooter__}
# ```""")

    @Ghost.command(name="addccmd", description="Add a custom command.", usage="addccmd [name] [response]", aliases=["addcustomcommand"])
    async def addccmd(ctx, name, *, response):
        global ccmd
        customCommands = json.load(open("customcommands.json"))
        customCommands[name] = response
        json.dump(customCommands, open("customcommands.json", "w"), indent=4, sort_keys=False)
        ccmd = json.load(open("customcommands.json"))
        await ctx.send(f"Added `{Ghost.command_prefix}{name}` to your custom commands.", delete_after=__deletetimeout__)

    @Ghost.command(name="delccmd", description="Remove a custom command.", usage="delccmd [name]", aliases=["deletecustomcommand", "delcustomcommand", "removecustomcommand", "removeccmd", "deleteccmd"])
    async def delccmd(ctx, name):
        global ccmd
        customCommands = json.load(open("customcommands.json"))
        customCommands.pop(name)
        json.dump(customCommands, open("customcommands.json", "w"), indent=4, sort_keys=False)
        ccmd = json.load(open("customcommands.json"))
        await ctx.send(f"Removed `{Ghost.command_prefix}{name}` from your custom commands", delete_after=__deletetimeout__)            

    @Ghost.command(name="boobs", description="Pictures or videos of boobs.", usage=f"boobs", aliases=["tits", "tit", "milkers", "titties", "boob"])
    async def boobs(ctx):
        type = "boobs"
        image = get_nsfw(type)
        if image.endswith("png") or image.endswith("jpeg") or image.endswith("jpg") or image.endswith("gif"):
            embed = discord.Embed(title=f"{type}", color=__embedcolour__)
            embed.set_image(url=image)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()    
            await ctx.send(embed=embed)                  
        else:  
            await ctx.send(image)

    @Ghost.command(name="ass", description="Pictures or videos of ass.", usage=f"ass")
    async def ass(ctx):
        type = "ass"
        image = get_nsfw(type)
        if image.endswith("png") or image.endswith("jpeg") or image.endswith("jpg") or image.endswith("gif"):
            if __embedmode__:
                embed = discord.Embed(title=f"{type}", color=__embedcolour__)
                embed.set_image(url=image)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()    
                await ctx.send(embed=embed)          
            else:
                await ctx.send(image)       
        else:  
            await ctx.send(image)                


    @Ghost.command(name="pussy", description="Pictures or videos of pussy.", usage=f"pussy")
    async def pussy(ctx):
        type = "pussy"
        image = get_nsfw(type)
        if image.endswith("png") or image.endswith("jpeg") or image.endswith("jpg") or image.endswith("gif"):
            if __embedmode__:
                embed = discord.Embed(title=f"{type}", color=__embedcolour__)
                embed.set_image(url=image)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()    
                await ctx.send(embed=embed)              
            else:
                await ctx.send(image)    
        else:  
            await ctx.send(image)  

    @Ghost.command(name="porngif", description="Porn gifs.", usage=f"porngif")
    async def porngif(ctx):
        type = "porngif"
        image = get_nsfw(type)
        if image.endswith("png") or image.endswith("jpeg") or image.endswith("jpg") or image.endswith("gif"):
            if __embedmode__:
                embed = discord.Embed(title=f"{type}", color=__embedcolour__)
                embed.set_image(url=image)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()    
                await ctx.send(embed=embed)   
            else:
                await ctx.send(image)               
        else:  
            await ctx.send(image)  

    @Ghost.command(name="hentai", description="Pictures or videos of hentai.", usage=f"hentai")
    async def hentai(ctx):
        type = random.randint(1, 2)
        if type == 1:
            image = requests.get("https://nekos.life/api/lewd/neko").json()["neko"]
        elif type == 2:
            image = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif").json()["url"]
        if __embedmode__:
            embed = discord.Embed(title=f"hentai", color=__embedcolour__)
            embed.set_image(url=image)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()    
            await ctx.send(embed=embed)      
        else:
            await ctx.send(image)                     

    @Ghost.command(name="discordtheme", description="Change default Discord theme.", usage="discordtheme [light/dark]")
    async def discordtheme(ctx, theme = "dark"):
        theme = theme.lower()
        validThemes = ["dark", "light"]
        if theme in validThemes:
            DiscumClient = discum.Client(token=__token__, user_agent=get_random_user_agent(), log=False)
            DiscumClient.setTheme(theme)
            await ctx.send(f"Set Discord theme to `{theme}`.", delete_after=__deletetimeout__)
        else:
            await ctx.send("That isn't a valid Discord theme.", delete_after=__deletetimeout__)

    @Ghost.command(name="changehypesquad", description="Change your hypesquad house.", usage="changehypesquad [bravery/brilliance/balance]")
    async def changehypesquad(ctx, house):
        house = house.lower()
        houses = ["bravery", "brilliance", "balance"]
        if house in houses:
            DiscumClient = discum.Client(token=__token__, user_agent=get_random_user_agent(), log=False)
            DiscumClient.setHypesquad(house)
            await ctx.send(f"Changed your hypesquad house to `{house[:1].upper() + house[1:].lower()}`.", delete_after=__deletetimeout__)
        else:
            await ctx.send("That isn't a valid hypesquad house.", delete_after=__deletetimeout__)

    @Ghost.command(name="backupfriends", description="Backup all your friend's user IDs to a file.", usage="backupfriends", aliases=["friendbackup"])
    async def backupfriends(ctx):
        print_info("Grabbing all friends...")
        request = requests.get("https://discord.com/api/v6/users/@me/relationships", headers={"authorization": __token__})
        json = request.json()
        ids = []
        blockedIds = []
        incoming = []
        outgoing = []
        for item in json:
            if item["type"] == 1:
                print_info(f'Backed up {str(item["user"]["username"]) + "#" + str(item["user"]["discriminator"])}!')             
                ids.append(
                    str(item["id"]) + 
                    " : " + 
                    str(item["user"]["username"]) + 
                    "#" + str(item["user"]["discriminator"])
                    )
            if item["type"] == 2:
                print_info(f'Backed up a blocked user : {str(item["user"]["username"]) + "#" + str(item["user"]["discriminator"])}')
                blockedIds.append(
                    str(item["id"]) + 
                    " : " + 
                    str(item["user"]["username"]) + 
                    "#" + str(item["user"]["discriminator"])
                    )
            if item["type"] == 3:
                print_info(f'Backed up an incoming friend request : {str(item["user"]["username"]) + "#" + str(item["user"]["discriminator"])}')
                incoming.append(
                    str(item["id"]) + 
                    " : " + 
                    str(item["user"]["username"]) + 
                    "#" + str(item["user"]["discriminator"])
                    )   
            if item["type"] == 4:
                print_info(f'Backed up an outgoing friend request : {str(item["user"]["username"]) + "#" + str(item["user"]["discriminator"])}')
                outgoing.append(
                    str(item["id"]) + 
                    " : " + 
                    str(item["user"]["username"]) + 
                    "#" + str(item["user"]["discriminator"])
                    ) 

        print_info("Backed up all friends!")
        await ctx.send(f"Backed up a total of `{len(ids)}` friends, `{len(blockedIds)}` blocked, `{len(outgoing)}` outgoing friend requests and `{len(incoming)}` incoming friend requests to __data/friends.txt__.", delete_after=__deletetimeout__)

        if not ids:
            ids.append("Couldnt find any friends.")
        if not blockedIds:
            blockedIds.append("Couldnt find any blocked users.")
        if not outgoing:
            outgoing.append("Couldnt find any outgoing friend requests.")
        if not incoming:
            incoming.append("Couldnt find any incoming friend requests.")
                                                
        file = codecs.open("data/friends.txt", "w", encoding="utf-8")
        file.write(
            "Current Friends\n===============\n" + "\n".join(ids) + 
            "\n \nOutgoing Requests\n=================\n" + "\n".join(outgoing) + 
            "\n \nIncoming Requests\n=================\n" + "\n".join(incoming) + 
            "\n \nBlocked Users\n=============\n" + "\n".join(blockedIds)
            )
        file.close()

    @Ghost.command(name="backupservers", description="Backup all your servers and try to create invites for each one.", usage="backupservers", aliases=["backupguilds", "serverbackup", "guildbackup"])
    async def backupservers(ctx):
        DiscumClient = discum.Client(token=__token__, log=False, user_agent=get_random_user_agent())
        try:
            await ctx.message.delete()
        except:
            pass
        print_info("Saving and creating invites for your guilds with a 4 second interval...")
        guilds = requests.get("https://discordapp.com/api/v6/users/@me/guilds", headers={"authorization": __token__}).json()
        print_info("Grabbing all the guilds...")
        guildsIdsAndInvites = []
        for item in guilds:
            guildid = item["id"]
            guildname = item["name"]
            invite = ""

            print_info(f"Trying to create invite for {guildname}")
            server = discord.utils.get(Ghost.guilds, id=int(guildid))
            for channel in server.text_channels:
                if invite == "":
                    invite = DiscumClient.createInvite(str(channel.id))
                    if invite.status_code == 200:
                        invite = invite.json()["code"]
                    else:
                        invite = ""
                    break

            if invite == "":
                invite = "Failed to create an invite."
            guildsIdsAndInvites.append(item["name"] + " : " + str(item["id"]) + " : discord.gg/" + str(invite))
            await asyncio.sleep(4)
        print_info(f"Saved guilds data.")
        file = codecs.open("data/servers.txt", "w", encoding="utf-8")
        file.write("\n".join(guildsIdsAndInvites))
        file.close()        
        await ctx.send("Saved a list of all your guilds and their IDs in __data/servers.txt__.", delete_after=__deletetimeout__)

    @Ghost.command(name="richpresence", description="Enable or disable rich presence.", usage="richpresence [on/off]", aliases=["rpc"])
    async def richpresence(ctx, status):
        if status == "on" or status == "On":
            richpresence = json.load(open("richpresence.json"))

            richpresence["enabled"] = True
            json.dump(richpresence, open('richpresence.json', 'w'), sort_keys=False, indent=4)

            await ctx.send("Rich presence has been enabled, restarting to change effect...", delete_after=__deletetimeout__)
            restart_bot()
        elif status == "off" or status == "Off":
            richpresence = json.load(open("richpresence.json"))

            richpresence["enabled"] = False
            json.dump(richpresence, open('richpresence.json', 'w'), sort_keys=False, indent=4)

            await ctx.send("Rich presence has been disabled, restarting to change effect...", delete_after=__deletetimeout__)
            restart_bot()
    
    @Ghost.command(name="spacechannel", description="Create a channel with spaces.", usage="spacechannel [channel name]")
    async def spacechannel(ctx, *, channelName = "example channel name"):
        channelName = channelName.replace(" ", channelBlankChar)
        await ctx.guild.create_text_channel(name=channelName)
        
        if __embedmode__:
            embed = discord.Embed(title=f"Space Channel", description=f"Created a channel with the name `{channelName}`.", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()

            await ctx.send(embed=embed, delete_after=__deletetimeout__)  
        else:
            await ctx.send(f"""```ini
[ Space Channel ]

Created a channel with the name {channelName}.


# {__embedfooter__}
```""")
    
    @Ghost.command(name="uwu", description="Translate your messages to uwu!", usage="uwu [message]")
    async def uwu__(ctx, *, message):
        uwued = uwuify.uwu(message)
        await ctx.send(uwued)
        
    @Ghost.command(name="uwuify", description="Automatically translate all your sent messages to uwu!", usage="uwuify")
    async def uwuify__(ctx):
        global uwuifyEnabled
        
        if (uwuifyEnabled):
            uwuifyEnabled = False
            await ctx.send("All your messages will no longer be translated to uwu.", delete_after=__deletetimeout__)              
        else:
            uwuifyEnabled = True
            await ctx.send("All your messages will now be translated to uwu.", delete_after=__deletetimeout__)            

    @Ghost.command(name="geoip", description="Get information from an IP address.", usage="geoip [ip]", aliases=["iplookup", "lookupip", "ipinfo"])
    async def geoip(ctx, ip):
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        data2 = requests.get(f"https://ipqualityscore.com/api/json/ip/oOswzMILsf8QA7JGtaQDdXARfDtbKW1K/{ip}").json()

        country = data["country"]
        city = data["city"]
        zipCode = data["zip"]
        lat = data["lat"]
        lon = data["lon"]
        isp = data["isp"]
        as1 = data["as"]
        region = data["regionName"]
        vpn = data2["vpn"]
        hostname = data2["host"]

        if __embedmode__:
            embed = discord.Embed(title=f"{ip} information...", color=__embedcolour__)
            embed.add_field(name="Country", value=f"```{country}```", inline=False)
            embed.add_field(name="City", value=f"```{city}```", inline=True)
            embed.add_field(name="Region", value=f"```{region}```", inline=True)
            embed.add_field(name="ZIP", value=f"```{zipCode}```", inline=True)
            embed.add_field(name="LAT", value=f"```{lat}```", inline=True)
            embed.add_field(name="LON", value=f"```{lon}```", inline=True)
            embed.add_field(name="VPN", value=f"```{vpn}```", inline=True)
            embed.add_field(name="AS", value=f"```{as1}```", inline=False)
            embed.add_field(name="ISP", value=f"```{isp}```", inline=False)
            embed.add_field(name="Hostname", value=f"```{hostname}```", inline=False)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()

            await ctx.send(embed=embed, delete_after=__deletetimeout__)  
        else:
            await ctx.send(f"""```ini
[ {ip} information.. ]

Country: {country}
City: {city}
Region: {region}
ZIP: {zipCode}
LAT: {lat}
LON: {lon}
VPN: {vpn}
AS: {as1}
ISP: {isp}
Hostname: {hostname}


# {__embedfooter__}
```""", delete_after=__deletetimeout__)      

    @Ghost.command(name="invite", description="Get Ghost's Discord server invite link.", usage="invite")
    async def invite(ctx):
        print_info(f"Discord server invite: {discordServer}")

    @Ghost.command(name="pytoexe", description="Convert a PY file to an executable.", usage="pytoexe [path]", aliases=["pythontoexe", "py2exe", "python2exe"])
    async def pytoexe(ctx, *, path):
        pyFile = False
        file = path.split("/")[-1]

        if (file.endswith(".py")):
            pyFile = True
        
        if (pyFile):
            file = file[:-3]

            if __embedmode__:
                embed = discord.Embed(title=f"PY To Executable", description="Conversion for your file has started, check the console for more information.", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()

                message = await ctx.send(embed=embed)
            else:
                message = await ctx.send(f"""```ini
[ PY To Executable ]

Conversion for your file has started, check the console for more information.


# {__embedfooter__}
```""")

            print_info("Converting your file to an exe using pyinstaller...\nThis will fill your console and possibly take a while.")
            os.system(f'pyinstaller -n "{file}" -i "icon.ico" --onefile --distpath "pytoexe/" {path}')
            print_info("Conversion complete!")
            print(f"{fg.cYellow}Path: {fg.cGrey}pytoexe/{file}.exe")

            if __embedmode__:
                embed = discord.Embed(title=f"PY To Executable", description="Conversion for your file has completed! Check the console for more information.", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()     

                await message.edit(content="", embed=embed)  
            else:
                await message.edit(content=f"""```ini
[ PY To Executable ]

Converstion for your file has completed! Check the console for more information.


# {__embedfooter__}
```""")

        else:
            if __embedmode__:
                embed = discord.Embed(title=f"PY To Executable", description="The path you submitted does not link to a PY file.", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()

                await ctx.send(embed=embed)   
            else:
                await ctx.send(f"""```ini
[ PY To Executable ]

The path you submitted does not link to a PY file.


# {__embedfooter__}
```""")          

    @Ghost.command(name="statuscycle", description="Start a custom status cycle.", usage="statuscycle", aliases=["cyclestatus"])
    async def statuscycle(ctx):
        global cycleStatus

        if (cycleStatus is False):
            cycleStatus = True
        else:
            cycleStatus = False

        def changeStatus(text2, token):
            url = "https://discordapp.com/api/v8/users/@me/settings"

            payload="{\r\n    \"custom_status\": {\r\n        \"text\": \"" + text2 + "\"\r\n    }\r\n}"
            headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'Cookie': '__cfduid=d7e8d2784592da39fb3f621664b9aede51620414171; __dcfduid=24a543339247480f9b0bb95c710ce1e6'
            }

            requests.request("PATCH", url, headers=headers, data=payload)    

        async def loopStatus(text):
            while cycleStatus is True:
                for word in text.split(" "):
                    changeStatus(word, __token__)   
                    await asyncio.sleep(1)

        Ghost.loop.create_task(loopStatus(cycleStatusText))

        if (cycleStatus is True):
            await ctx.send(f"Now looping your custom status.", delete_after=__deletetimeout__)
        else:
            await ctx.send(f"No longer looping your custom status.", delete_after=__deletetimeout__)

    @Ghost.command(name="statuscycletext", description="Set the text used in status cycle.", usage="statuscycletext [text]", aliases=["cyclestatustext"])
    async def statuscycletext(ctx, *, text: str):
        global cycleStatusText
        cycleStatusText = text

        await ctx.send(f"Status cycle text set to `{cycleStatusText}`", delete_after=__deletetimeout__)

    @Ghost.command(name="ghostping", description="Ping a user then delete the message.", usage="ghostping [@user]")
    async def ghostping(ctx, user: discord.User):
        pass

    @Ghost.command(name="getmessage", description="Get a message by ID.", usage="getmessage [message id]", aliases=["fetchmessage"])
    async def getmessage(ctx, messageid: int):
        msg = await ctx.send("Getting the message . . .")
        message = await get_message(ctx, messageid)

        if __embedmode__:
            embed = discord.Embed(title=f"Get Message", color=__embedcolour__)
            embed.add_field(name="Content", value=f"```{message.content}```", inline=True)
            embed.add_field(name="Author", value=f"```{message.author}```", inline=True)
            embed.add_field(name="Message Link", value=message.jump_url, inline=False)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await msg.edit(content="", embed=embed, delete_after=__deletetimeout__)  
        else:
            await msg.edit(content=f"""```ini
[ Get Message ]

Content: {message.content}
Author: {message.author}
Message Link: {message.jump_url}


# {__embedfooter__}
```""", delete_after=__deletetimeout__)      

    @Ghost.command(name="watchdogstats", description="Get stats about Hypixel's Anticheat, Watchdog", usage="watchdogstats")
    async def watchdogstats(ctx):
        data = requests.get("https://api.hypixel.net/punishmentstats?key=591c390d-6e97-4b39-abb3-ef3fb386aff0").json()
        if __embedmode__:
            embed = discord.Embed(title=f"Watchdog Stats", color=__embedcolour__)
            embed.add_field(name="Total Bans", value="```" + str(data["watchdog_total"]) + "```", inline=True)
            embed.add_field(name="Last Minute", value="```" + str(data["watchdog_lastMinute"]) + "```", inline=True)
            embed.add_field(name="Daily Bans", value="```" + str(data["watchdog_rollingDaily"]) + "```", inline=True)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send(f"""```ini
[ Watchdog Stats ]

Total Bans: {data['watchdog_total']}
Last Minute: {data['watchdog_lastMinute']}
Daily Bans: {data['watchdog_rollingDaily']}


# {__embedfooter__}
```""", delete_after=__deletetimeout__)

    @Ghost.command(name="ppin", description="Add a message to your personal pins.", usage="ppin [message id]", aliases=["personalpin", "addppin", "addpersonalpin"])
    async def ppin(ctx, msgId: int):
        message = await get_message(ctx, msgId)

        data = json.load(open("data/personal-pins.json"))
        data[msgId] = {}
        data[msgId]["content"] = message.content
        data[msgId]["author"] = f"{message.author.name}#{message.author.discriminator}"

        json.dump(data, open("data/personal-pins.json", 'w'), sort_keys=False, indent=4)

        if __embedmode__:
            embed = discord.Embed(title=f"Personal Pin", color=__embedcolour__, description=f"Pinned message `{message.content}` by `{message.author.name}#{message.author.discriminator}`.")
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send(f"**📌 Personal Pin**\nPinned message `{message.content}` by `{message.author.name}#{message.author.discriminator}`.")

    @Ghost.command(name="ppins", description="List all your pinned messages.", usage="ppins", aliases=["personalpins"])
    async def ppins(ctx):
        data = json.load(open("data/personal-pins.json"))

        ppinsMsg = ""
        for value in data:
            content = data[value]["content"]
            author = data[value]["author"]

            ppinsMsg += f"\n__{value}__ :\n**  **- Content : `{content}`\n**  **- Author : `{author}`"

        if __embedmode__:
            embed = discord.Embed(title=f"Personal Pin", color=__embedcolour__, description=ppinsMsg)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send(f"**Personal Pins**\n{ppinsMsg}")

    @Ghost.command(name="ppindel", description="Delete a pin from your personal pins.", usage="ppindel [pin id]", aliases=["ppindelete", "removeppin", "deleteppin", "personalpindelete", "deletepersonalpin", "removepersonalpin"])
    async def ppindel(ctx, pinId: str):
        data = json.load(open("data/personal-pins.json"))

        del data[pinId]

        json.dump(data, open("data/personal-pins.json", 'w'), sort_keys=False, indent=4)

        if __embedmode__:
            embed = discord.Embed(title=f"Personal Pin", color=__embedcolour__, description=f"Delete pin `{pinId}`.")
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send(f"**Personal Pin**\nDelete pin `{pinId}`.")

    @Ghost.command(name="countdown", description="Count down from a number.", usage="countdown [number]")
    async def countdown(ctx, number: int):
        for count in range(number, 0, -1):
            await ctx.send(count)

    @Ghost.command(name="countup", description="Count up from a number.", usage="countup [number]")
    async def countup(ctx, number: int):
        for count in range(number):
            await ctx.send(count)

    @Ghost.command(name="massban", description="Ban all the members in the command server.", usage="massban")
    async def massban(ctx):
        if __riskmode__:
            try:
                await ctx.message.delete()
            except:
                pass

            bot = discum.Client(token=__token__, log=False, user_agent=get_random_user_agent())

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    print_info("Fetching complete.")
                    members = bot.gateway.session.guild(guild_id).members
                    bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()
                    print_info(f"Fetched a total of {len(members)} members.")
                    return members

            def get_members(guild_id, channel_id):
                print_info("Fetching members...")
                bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1)
                bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(str(ctx.guild.id), str(ctx.channel.id))

            for member in members:
                try:
                    member = await ctx.guild.fetch_member(int(member))
                    await member.ban()
                    await asyncio.sleep(1)
                except:
                    pass
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                              

    @Ghost.command(name="masskick", description="Kick all the members in the command server.", usage="masskick")
    async def masskick(ctx):
        if __riskmode__:
            try:
                await ctx.message.delete()
            except:
                pass

            bot = discum.Client(token=__token__, log=False, user_agent=get_random_user_agent())

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    print_info("Fetching complete.")
                    members = bot.gateway.session.guild(guild_id).members
                    bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()
                    print_info(f"Fetched a total of {len(members)} members.")
                    return members

            def get_members(guild_id, channel_id):
                print_info("Fetching members...")
                bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1)
                bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(str(ctx.guild.id), str(ctx.channel.id))

            for member in members:
                try:
                    member = await ctx.guild.fetch_member(int(member))
                    await member.kick()
                    await asyncio.sleep(1)
                except:
                    pass
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                              
            
    @Ghost.command(name="raidjoin", description="Make all your account tokens join a server.", usage="raidjoin [delay] [invite]")
    async def raidjoin(ctx, delay:int = 3, *, invite: str):
        if __riskmode__:
            print_info(f"Trying to join server with tokens every {delay} seconds.")
            for Token in open("data/tokens.txt", "r").readlines():
                Token = Token.replace("\n", "")
                userAgent = get_random_user_agent()
                request = requests.post(f"https://discord.com/api/v9/invites/{invite}", headers={
                    "Authorization": Token,
                    "accept": "*/*",
                    "accept-language": "en-US",
                    "connection": "keep-alive",
                    "cookie": f"__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US",
                    "DNT": "1",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "referer": "https://discord.com/channels/@me",
                    "TE":"Trailers ",
                    "User-Agent": userAgent,
                    "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                })
                if request.status_code == 200:
                    print_info(f"Joined successfully.")
                else:
                    print_info("Failed to join.")
                try:
                    print_info("Accepted guild rules.")
                    requests.put(f"https://discord.com/api/guilds/{request['guild']['id']}/requests/@me", headers={"Authorization": Token, "User-Agent": userAgent, "Content-Type": "application/json"}, data=json.dumps({}))
                except:
                    print_info("Couldnt accept guild rules")
                await asyncio.sleep(delay)
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                              

    @Ghost.command(name="tokenraid", description="Raid a server with all your account tokens.", usage="tokenraid [threads] [amount] [channel id] (message)")
    async def tokenraid(ctx, threadsAmount:int, amount: int, channel_id: int = None, *, text = None):
        if __riskmode__:
            await ctx.message.delete()

            tokens = []
            for token in open("data/tokens.txt", "r").readlines():
                tokens.append(token.replace("\n", ""))

            def raid():
                def sendMessages():
                    message = text
                    print_info("Started new thread.")
                    for _ in range(amount):
                        requests.post(f"https://discord.com/api/channels/{channel_id}/messages", headers={"Authorization": random.choice(tokens), "User-Agent": get_random_user_agent(), "Content-Type": "application/json"}, data=json.dumps({
                            "content": message + f" [{random.randint(1000, 9999)}]" 
                        }))

                print_info("Raid has begun.")
                threads = []
                for _ in range(threadsAmount):
                    thread = threading.Thread(target=sendMessages())
                    threads.append(thread)
                    threads[_].start()
                for thread in threads:
                    thread.join()
                print_info("Raid finished.")

            Ghost.loop.create_task(raid())
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                          

    @Ghost.command(name="checktoken", description="Checks if a token is working.", usage="checktoken [token]")
    async def checktoken(ctx, *, token):
        tokens = [token]
        valid = "invalid"

        message = await ctx.send("Starting check, read console for more information.")
        print_info("Checking the token you gave...")                

        for token in tokens:
            request = requests.get("https://discord.com/api/users/@me/library", headers={"Authorization": token, "User-Agent": get_random_user_agent()})
            if request.status_code != 200:
                valid = "invalid"
                print(f"{printSpaces}{fg.cGrey}[{getCurrentTime()}] {fg.cRed}[INVALID] {fg.cWhite}{token}")
            else:
                valid = "valid"
                print(f"{printSpaces}{fg.cGrey}[{getCurrentTime()}] {fg.cGreen}[VALID] {fg.cWhite}{token}")

        await message.edit(content="Check complete, read console for more information.", delete_after=__deletetimeout__)
        print_info(f"Check complete, the token is {valid}.")

    @Ghost.command(name="checktokens", description="Checks if your tokens are working.", usage="checktokens")
    async def checktokens(ctx):
        tokens = []
        validTokens = []
        invalidTokens = []

        message = await ctx.send("Starting check, read console for more information.")
        print_info("Checking your tokens has started.")

        for token in open("data/tokens.txt", "r").readlines():
            tokens.append(token.replace("\n", ""))
        for token in tokens:
            request = requests.get("https://discord.com/api/users/@me/library", headers={"Authorization": token, "User-Agent": get_random_user_agent()})
            if request.status_code != 200:
                invalidTokens.append(token)
                print(f"{printSpaces}{fg.cGrey}[{getCurrentTime()}] {fg.cRed}[INVALID] {fg.cWhite}{token}")
            else:
                validTokens.append(token)   
                print(f"{printSpaces}{fg.cGrey}[{getCurrentTime()}] {fg.cGreen}[VALID] {fg.cWhite}{token}")  

        open("data/valid-tokens.txt", "w").write('\n'.join(validTokens))           
        open("data/invalid-tokens.txt", "w").write('\n'.join(invalidTokens))

        await message.edit(content="Check complete, read console for more information.", delete_after=__deletetimeout__)
        print_info("Check complete.")
        print_info(f"Valid tokens: {len(validTokens)} (Saved to data/valid-tokens.txt)")           
        print_info(f"Invalid tokens: {len(invalidTokens)} (Saved to data/invalid-tokens.txt)")           

    @Ghost.command(name="wipetoken", description="Completely wipe a token.", aliases=["cleantoken"])
    async def wipetoken(ctx, token):
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.send("Check console for more info...", delete_after=__deletetimeout__)                

        def closeDms():
            try:
                dms = requests.get("https://discord.com/api/users/@me/channels", headers={"Authorization": token, "User-Agent": get_random_user_agent()}).json()
                for dm in dms:
                    try:
                        requests.delete(f"https://discord.com/api/channels/{dm['id']}", headers={"Authorization": token, "User-Agent": get_random_user_agent()})
                    except:
                        pass
            except:
                pass
        def leaveServers():
            try:
                guilds = requests.get("https://discord.com/api/users/@me/guilds", headers={"Authorization": token, "User-Agent": get_random_user_agent()}).json()
                for guild in guilds:
                    try:
                        requests.delete(f"https://discord.com/api/guilds/{guild['id']}", headers={"Authorization": token, "User-Agent": get_random_user_agent()})
                    except:
                        pass
            except:
                pass
        def removeFriends():
            try:
                friends = requests.get("https://discord.com/api/users/@me/relationships", headers={"Authorization": token, "User-Agent": get_random_user_agent()}).json()
                for friend in friends:
                    try:
                        requests.delete(f"https://discord.com/api/users/@me/relationships/{friend['id']}", headers={"Authorization": token, "User-Agent": get_random_user_agent()})
                    except:
                        pass
            except:
                pass

        threading.Thread(target=closeDms).start()
        threading.Thread(target=leaveServers).start()
        threading.Thread(target=removeFriends).start()

    @Ghost.command(name="nuketoken", description="Nuke a token.", usage="nuketoken [token]", aliases=["tokennuke"])
    async def nuketoken(ctx, token):
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.send("Check console for more info...", delete_after=__deletetimeout__)

        def themeSpammer():
            themes = ["dark", "light"]
            for i in range(999999999):
                requests.patch("https://discord.com/api/users/@me/settings", headers={"Authorization": token, "User-Agent": get_random_user_agent(), "Content-Type": "application/json"}, data=json.dumps({
                    "theme": random.choice(themes)
                }))
        def closeDms():
            try:
                dms = requests.get("https://discord.com/api/users/@me/channels", headers={"Authorization": token, "User-Agent": get_random_user_agent()}).json()
                for dm in dms:
                    try:
                        requests.delete(f"https://discord.com/api/channels/{dm['id']}", headers={"Authorization": token, "User-Agent": get_random_user_agent()})
                    except:
                        pass
            except:
                pass
        def leaveServers():
            try:
                guilds = requests.get("https://discord.com/api/users/@me/guilds", headers={"Authorization": token, "User-Agent": get_random_user_agent()}).json()
                for guild in guilds:
                    try:
                        requests.delete(f"https://discord.com/api/guilds/{guild['id']}", headers={"Authorization": token, "User-Agent": get_random_user_agent()})
                    except:
                        pass
            except:
                pass
        def removeFriends():
            try:
                friends = requests.get("https://discord.com/api/users/@me/relationships", headers={"Authorization": token, "User-Agent": get_random_user_agent()}).json()
                for friend in friends:
                    try:
                        requests.delete(f"https://discord.com/api/users/@me/relationships/{friend['id']}", headers={"Authorization": token, "User-Agent": get_random_user_agent()})
                    except:
                        pass
            except:
                pass
        def createGuilds():
            while True:
                requests.post("https://discord.com/api/guilds", headers={"Authorization": token, "User-Agent": get_random_user_agent(), "Content-Type": "application/json"}, data=json.dumps({
                    "name": "EPIC GAMERS"
                }))

        threading.Thread(target=themeSpammer).start()
        threading.Thread(target=closeDms).start()
        threading.Thread(target=leaveServers).start()
        threading.Thread(target=removeFriends).start()
        threading.Thread(target=createGuilds).start()

    @Ghost.command(name="gstart", description="Start a giveaway in the same channel", usage="gstart [duration] [winners] [prize]", aliases=["giveawaystart", "startgiveaway"])
    async def gstart(ctx, duration=None, winners: int = None, *, prize=None):
        if duration is not None:
            if winners is not None:
                if prize is not None:

                    if duration.endswith("m"):
                        duration = duration[:-1]
                        time = int(duration) * 60
                        timemins = time // 60
                        timepretty = f"{timemins} minute(s)"

                    elif duration.endswith("s"):
                        duration = duration[:-1]
                        time = int(duration)
                        timepretty = f"{time} second(s)"

                    elif duration.endswith("h"):
                        duration = duration[:-1]
                        time = int(duration) * 3600
                        timehrs = time // 3600
                        timepretty = f"{timehrs} hour(s)"

                    else:
                        if duration.endswith("s") or duration.endswith("m") or duration.endswith("h"):
                            duration = duration[:-1]
                            time = int(duration)
                            timepretty = f"{time} second(s)"

                    e = discord.Embed(
                        description=f"React with 🎉 to enter!\nEnds in {timepretty}\nHosted by {ctx.author.mention}",
                        color=__embedcolour__)
                    if winners >= 2:
                        e.set_footer(text=f"{winners} winners | Ends at")
                    else:
                        e.set_footer(text="1 winner | Ends at")
                    e.set_author(name=prize)
                    future = datetime.now() + timedelta(seconds=time)
                    e.timestamp = future
                    msg = await ctx.send("🎉 **GIVEAWAY** 🎉", embed=e)
                    await msg.add_reaction('\U0001F389')

                    await asyncio.sleep(time)

                    channelMsgHistory = await ctx.channel.history(limit=500).flatten()
                    for message in channelMsgHistory:
                        if message.id == msg.id:
                            msg = message

                    #running = False
                    if "🎉 **GIVEAWAY** 🎉" in msg.content:
                        entries = []
                        reactions = msg.reactions
                        for reaction in reactions:
                            users = await reaction.users().flatten()
                            for user in users:
                                entries.append(f"<@{user.id}>")
                        entries.remove(f"<@{Ghost.user.id}>")

                        nowinner = False
                        if entries != []:
                            nowinner = False
                            winnerslist = []
                            if winners >= 2:
                                for _ in range(winners):
                                    winner1 = random.choice(entries)
                                    winnerslist.append(winner1)
                            else:
                                winner1 = random.choice(entries)
                                winnerslist.append(winner1)
                        else:
                            nowinner = True

                        #running = True

                        if nowinner is True:
                            await ctx.send(f"A winner was not determined.\n{msg.jump_url}")
                            newe = discord.Embed(
                                description=f"A winner was not determined.\nHosted by {ctx.author.mention}",
                                color=0x36393F)

                        else:
                            await ctx.send("🎉 " + ', '.join(winnerslist) + f" you won **{prize}**\n{msg.jump_url}")
                            newe = discord.Embed(
                                description=', '.join(winnerslist) + f" won!\nHosted by {ctx.author.mention}",
                                color=0x36393F)
                        newe.set_author(name=prize)

                        if winners >= 2:
                            newe.set_footer(text=f"{winners} winners | Ended at")
                        else:
                            newe.set_footer(text="1 winner | Ended at")
                        future = datetime.now() + timedelta(seconds=time)
                        newe.timestamp = future

                        await msg.edit(content="🎉 **GIVEAWAY ENDED** 🎉", embed=newe)

                    #elif "🎉 **GIVEAWAY ENDED** 🎉" in msg.content:
                        #running = False

                else:
                    await ctx.send(
                        f"❌ **Incorrect Syntax**\nTry: `{Ghost.command_prefix}gstart 30m 1 Awesome T-Shirt`")
            else:
                await ctx.send(f"❌ **Incorrect Syntax**\nTry: `{Ghost.command_prefix}gstart 30m 1 Awesome T-Shirt`")
        else:
            await ctx.send(f"❌ **Incorrect Syntax**\nTry: `{Ghost.command_prefix}gstart 30m 1 Awesome T-Shirt`")


    @Ghost.command(name="gend", description="End a giveaway", usage="gend [message id]", aliases=["giveawayend", "endgiveaway"])
    async def gend(ctx, id: int = None):
        #running = False

        msgId = ""
        msgAuthorId = ""
        msgContent = ""
        channelMsgHistory = await ctx.channel.history(limit=500).flatten()
        #print(channelMsgHistory)
        for message in channelMsgHistory:
            #print(message.id)
            if message.id == id:
                msgId = message.id
                msgAuthorId = message.author.id
                msgContent = message.content
                msg = message

        #print("Fetched Message ID: " + str(msgId))
        #print("Looking for Message ID: " + str(id))
        #print("Message author ID: " + str(msgAuthorId))
        #print("Bot user ID: " + str(Ghost.user.id))

        if msgId == id and msgAuthorId == Ghost.user.id:
            if "🎉 **GIVEAWAY** 🎉" in msgContent:
                #running = True
                embeds = msg.embeds
                for embed in embeds:
                    embed_dict = embed.to_dict()

                entries = []
                reactions = msg.reactions
                for reaction in reactions:
                    users = await reaction.users().flatten()
                    for user in users:
                        entries.append(f"<@{user.id}>")
                entries.remove(f"<@{Ghost.user.id}>")

                nowinner = False
                if "winners" in embed_dict['footer']['text']:
                    winners = embed_dict['footer']['text'].replace(" winners | Ends at", "")
                elif "winner" in embed_dict['footer']['text']:
                    winners = embed_dict['footer']['text'].replace(" winner | Ends at", "")

                prize = embed_dict['author']['name']

                if entries != []:
                    nowinner = False
                    winnerslist = []
                    if int(winners) >= 2:
                        for _ in range(int(winners)):
                            winner1 = random.choice(entries)
                            winnerslist.append(winner1)
                    else:
                        winner1 = random.choice(entries)
                        winnerslist.append(winner1)
                else:
                    nowinner = True

                if nowinner is True:
                    await ctx.send(f"A winner was not determined.\n{msg.jump_url}")
                    newe = discord.Embed(
                        description=f"A winner was not determined.\nHosted by {ctx.author.mention}", color=0x36393F)

                else:
                    await ctx.send("🎉 " + ', '.join(winnerslist) + f" you won **{prize}**\n{msg.jump_url}")
                    newe = discord.Embed(
                        description=', '.join(winnerslist) + f" won!\nHosted by {ctx.author.mention}",
                        color=0x36393F)

                newe.set_author(name=embed_dict['author']['name'])
                if int(winners) >= 2:
                    newe.set_footer(text=f"{winners} winners | Ended at")
                else:
                    newe.set_footer(text=f"{winners} winner | Ended at")
                newe.timestamp = datetime.now()

                await msg.edit(content="🎉 **GIVEAWAY ENDED** 🎉", embed=newe)

            elif "🎉 **GIVEAWAY ENDED** 🎉" in msgContent:
                #running = False
                await ctx.send("😔 That giveaway has already ended.")

            else:
                await ctx.send("That is not a giveaway.")
        else:
            await ctx.send("That is not a giveaway.")


    @Ghost.command(name="greroll", description="Re-roll a giveaway", usage="greroll [message id]", aliases=["giveawayreroll", "rerollgiveaway"])
    async def greroll(ctx, id: int = None):
        #running = False

        channelMsgHistory = await ctx.channel.history(limit=500).flatten()
        for message in channelMsgHistory:
            if message.id == id:
                msg = message

        if msg.author.id == Ghost.user.id:
            if "🎉 **GIVEAWAY** 🎉" in msg.content:
                #running = True
                await ctx.send("You can't re-roll a running giveaway.")

            elif "🎉 **GIVEAWAY ENDED** 🎉" in msg.content:
                #running = False
                embeds = msg.embeds
                for embed in embeds:
                    embed_dict = embed.to_dict()

                entries = []
                reactions = msg.reactions
                for reaction in reactions:
                    users = await reaction.users().flatten()
                    for user in users:
                        entries.append(f"<@{user.id}>")
                entries.remove(f"<@{Ghost.user.id}>")

                nowinner = False
                if "winners" in embed_dict['footer']['text']:
                    winners = embed_dict['footer']['text'].replace(" winners | Ended at", "")
                elif "winner" in embed_dict['footer']['text']:
                    winners = embed_dict['footer']['text'].replace(" winner | Ended at", "")

                prize = embed_dict['author']['name']

                if entries != []:
                    nowinner = False
                    winnerslist = []
                    if int(winners) >= 2:
                        for _ in range(int(winners)):
                            winner1 = random.choice(entries)
                            winnerslist.append(winner1)
                    else:
                        winner1 = random.choice(entries)
                        winnerslist.append(winner1)
                else:
                    nowinner = True

                if nowinner is True:
                    await ctx.send(f"A winner was not determined.\n{msg.jump_url}")

                else:
                    await ctx.send("🎉 " + ', '.join(winnerslist) + f" you won **{prize}**\n{msg.jump_url}")
            else:
                await ctx.send("That is not a giveaway.")
        else:
            await ctx.send("That is not a giveaway.")

    typing = False

    @Ghost.command(name="typing", description="Start or stop typing.", usage="typing [start/stop]", aliases=["inftyping", "infintetyping"])
    async def typing__(ctx, action = None):
        global typing
        if action == "start" or action == "Start":
            await ctx.send("Started typing.")

            typing = True

            while typing is True:
                async with ctx.typing():
                        await asyncio.sleep(1)
                        if typing is False:
                            break

        elif action == "stop" or action == "Stop":
            await ctx.send("Stopped typing.")

            typing = False

        elif action is None:
            pass

    @Ghost.command(name="sounds", description="Toggle Ghost notification sounds.", usage="sounds", aliases=["togglesounds", "soundstoggle"])
    async def sounds(ctx):
        global __sounds__
        if __sounds__:
            __sounds__ = False
            cfg = Config.getConfig()
            cfg["sounds"] = False
            Config.saveConfig(cfg)
            await ctx.send("Disabled Ghost notification sounds.")
        else:
            __sounds__ = True
            cfg = Config.getConfig()
            cfg["sounds"] = True
            Config.saveConfig(cfg)
            await ctx.send("Enabled Ghost notification sounds.")

    @Ghost.command(name="ping", description="Ping a domain or ip address.", usage="ping [ip/domain]")
    async def ping(ctx, *, dns):
        message = await ctx.send("Pinging...")

        output = subprocess.run(f"ping {dns}",text=True,stdout=subprocess.PIPE).stdout.splitlines()
        values = "".join(output[-1:])[4:].split(", ")

        minimum = values[0][len("Minimum = "):]
        maximum = values[1][len("Maximum = "):]
        average = values[2][len("Average = "):]
        address = output[1].replace(f"Pinging {dns} [", "").replace("] with 32 bytes of data:", "")

        if __embedmode__:
            embed = discord.Embed(title=f"{dns} ping..", color=__embedcolour__)
            embed.add_field(name="IP Address", value=f"```{address}```", inline=False)
            embed.add_field(name="Minimum", value=f"```{minimum}```", inline=False)
            embed.add_field(name="Maximum", value=f"```{maximum}```", inline=False)
            embed.add_field(name="Average", value=f"```{average}```", inline=False)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await message.edit(content="Pong!", embed=embed, delete_after=__deletetimeout__)
        else:
            await message.edit(content=f"""```ini
[ {dns} ping.. ]

IP Address: {address}
Minimum: {minimum}
Maximum: {maximum}
Average: {average}


# {__embedfooter__}
```""", delete_after=__deletetimeout__)

    @Ghost.command(name="cloneserver", description="Clone a server.", usage="cloneserver", aliases=["copyserver"])
    async def cloneserver(ctx):
        serverName = ctx.guild.name
        serverIcon = ctx.guild.icon

        newGuild = await Ghost.create_guild(serverName)
        print_info(f"Created new guild.")
        newGuildDefaultChannels = await newGuild.fetch_channels()
        for channel in newGuildDefaultChannels:
            await channel.delete()

        for channel in ctx.guild.channels:
            if str(channel.type).lower() == "category":
                try:
                    await newGuild.create_category(channel.name, overwrites=channel.overwrites, position=channel.position)
                    print_info(f"Created new category : {channel.name}")
                except:
                    pass
                
        for channel in ctx.guild.voice_channels:
            try:
                cat = ""
                for category in newGuild.categories:
                    if channel.category.name == category.name:
                        cat = category
                        
                await newGuild.create_voice_channel(channel.name, category=cat, overwrites=channel.overwrites, topic=channel.topic, slowmode_delay=channel.slowmode_delay, nsfw=channel.nsfw, position=channel.position)
                print_info(f"Created new voice channel : {channel.name}")
            except:
                pass

        for channel in ctx.guild.stage_channels:
            try:
                cat = ""
                for category in newGuild.categories:
                    if channel.category.name == category.name:
                        cat = category                    
                await newGuild.create_stage_channel(channel.name, category=cat, overwrites=channel.overwrites, topic=channel.topic, slowmode_delay=channel.slowmode_delay, nsfw=channel.nsfw, position=channel.position)
                print_info(f"Created new stage channel : {channel.name}")
            except:
                pass
            
        for channel in ctx.guild.text_channels:
            try:
                cat = ""
                for category in newGuild.categories:
                    if channel.category.name == category.name:
                        cat = category                            
                await newGuild.create_text_channel(channel.name, category=cat, overwrites=channel.overwrites, topic=channel.topic, slowmode_delay=channel.slowmode_delay, nsfw=channel.nsfw, position=channel.position)
                print_info(f"Created new text channel : {channel.name}")
            except:
                pass

        for role in ctx.guild.roles[::-1]:
            if role.name != "@everyone":
                try:
                    await newGuild.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
                    print_info(f"Created new role : {role.name}")
                except:
                    pass

        await ctx.send(f"Made a clone of `{ctx.guild.name}`.")

    @Ghost.command(name="webhooksetup", description="Create a new server with webhooks.", usage="webhooksetup", aliases=["setupwebhooks"])
    async def webhooksetup(ctx):
        global __nitrowebhook__, __privnotewebhook__, __giveawaywebhook__, __ghostpingwebhook__, __friendsupdatewebhook__, __dmtypingwebhook__, __guildleavewebhook__, __selfbotwebhook__, __ticketswebhook__
        
        configFile = json.load(open("config.json"))
        guild = await Ghost.create_guild(ctx.author.name + "'s webhooks")
        newGuildDefaultChannels = await guild.fetch_channels()
        
        for channel in newGuildDefaultChannels:
            await channel.delete()                
        for channel in guild.text_channels:
            await channel.delete()
        for channel in guild.voice_channels:
            await channel.delete()
        for channel in guild.categories:
            await channel.delete()

        category = await guild.create_category_channel("Webhooks")

        nitroWebhookChannel = await category.create_text_channel("nitro-sniper")
        privnoteWebhookChannel = await category.create_text_channel("privnote-sniper")
        giveawayWebhookChannel = await category.create_text_channel("giveaway-sniper")
        ghostPingWebhookChannel = await category.create_text_channel("ghost-pings")
        friendUpdatesWebhookChannel = await category.create_text_channel("friend-updates")
        dmTypingWebhookChannel = await category.create_text_channel("dm-typing")
        guildLeaveWebhookChannel = await category.create_text_channel("guild-leave")
        selfbotsWebhookChannel = await category.create_text_channel("selfbots")
        ticketsWebhookChannel = await category.create_text_channel("tickets")

        nitroWebhook = await nitroWebhookChannel.create_webhook(name="Ghost Nitro Sniper")
        privnoteWebhook = await privnoteWebhookChannel.create_webhook(name="Ghost Privnote Sniper")
        giveawayWebhook = await giveawayWebhookChannel.create_webhook(name="Ghost Giveaway Sniper")
        ghostPingWebhook = await ghostPingWebhookChannel.create_webhook(name="Ghost Pings")
        friendUpdatesWebhook = await friendUpdatesWebhookChannel.create_webhook(name="Friend Updates")
        dmTypingWebhook = await dmTypingWebhookChannel.create_webhook(name="DM Typing")
        guildLeaveWebhook = await guildLeaveWebhookChannel.create_webhook(name="Guild Leave")
        selfbotsWebhook = await selfbotsWebhookChannel.create_webhook(name="Selfbots")
        ticketsWebhook = await ticketsWebhookChannel.create_webhook(name="Tickets")

        __nitrowebhook__ = nitroWebhook.url
        __privnotewebhook__ = privnoteWebhook.url
        __giveawaywebhook__ = giveawayWebhook.url
        __ghostpingwebhook__ = ghostPingWebhook.url
        __friendsupdatewebhook__ = friendUpdatesWebhook.url
        __dmtypingwebhook__ = dmTypingWebhook.url
        __guildleavewebhook__ = guildLeaveWebhook.url
        __selfbotwebhook__ = selfbotsWebhook.url
        __ticketswebhook__ = ticketsWebhook.url

        configFile["webhooks"]["nitro"] = __nitrowebhook__  
        configFile["webhooks"]["privnote"] = __privnotewebhook__  
        configFile["webhooks"]["giveaway"] = __giveawaywebhook__
        configFile["webhooks"]["ghostping"] = __ghostpingwebhook__
        configFile["webhooks"]["friendsupdate"] = __friendsupdatewebhook__
        configFile["webhooks"]["dmtyping"] = __dmtypingwebhook__
        configFile["webhooks"]["guildleave"] = __guildleavewebhook__
        configFile["webhooks"]["selfbot"] = __selfbotwebhook__
        configFile["webhooks"]["tickets"] = __ticketswebhook__

        json.dump(configFile, open("config.json", "w"), sort_keys=False, indent=4)  
        
        if __embedmode__:
            embed = discord.Embed(title="Webhook Setup", description=f"Created a new guild for your webhooks called `{guild.name}`.", colour=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send(f"Created a new guild for your webhooks called `{guild.name}`.", delete_after=__deletetimeout__)

    @Ghost.command(name="spamwebhook", description="Spam the shit out of a webhook.", usage="spamwebhook [amount] [url] (message)")
    async def spamwebhook(ctx, amount: int, url, *, message = None):
        if __embedmode__:
            embed = discord.Embed(title="Spamming webhook...", colour=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send("Spamming webhook...", delete_after=__deletetimeout__)

        if message is None:
            for _ in range(amount):
                spamMsg = ''.join(random.choice(string.ascii_letters) for i in range(2000))
                webhook = DiscordWebhook(url=url, content=spamMsg)
                webhook.execute()            
        else:
            for _ in range(amount):
                webhook = DiscordWebhook(url=url, content=message)
                webhook.execute() 

        if __embedmode__:
            embed = discord.Embed(title="Finished spamming webhook", colour=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send("Finished spamming webhook!", delete_after=__deletetimeout__)

    @Ghost.command(name="newwebhook", description="Create a webhook in the command channel.", usage="newwebhook [name]", aliases=["createwebhook"])
    async def newwebhook(ctx, *, name):
        webhook = await ctx.channel.create_webhook(name=name)


        if __embedmode__:
            embed = discord.Embed(title=f"Created a webhook called {name}", description=f"URL: {webhook.url}", colour=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send(f"Created a webhook called {name}\nURL: {webhook.url}", delete_after=__deletetimeout__)

    @Ghost.command(name="delwebhook", description="Delete a webhook from the ID.", usage="delwebhook [id]", aliases=["deletewebhook", "removewebhook"])
    async def delwebhook(ctx, id: int):
        webhook = await Ghost.fetch_webhook(id)
        await webhook.delete()

        if __embedmode__:
            embed = discord.Embed(title="Deleted the webhook", colour=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send("Deleted the webhook", delete_after=__deletetimeout__)

    @Ghost.command(name="webhookinfo", description="Information about the webhook.", usage="webhookinfo [id]", aliases=["webhooklookup", "lookupwebhook"])
    async def webhookinfo(ctx, id: int):
        webhook = await Ghost.fetch_webhook(id)

        if __embedmode__:
            embed = discord.Embed(title=f"{webhook.name} Information", colour=__embedcolour__)
            embed.add_field(name="Webhook Name", value=f"```{webhook.name}```", inline=False)
            embed.add_field(name="Webhook ID", value=f"```{webhook.id}```", inline=False)
            embed.add_field(name="Webhook Guild", value=f"```{webhook.guild.name}```", inline=False)
            embed.add_field(name="Webhook Channel", value=f"```{webhook.channel.name}```", inline=False)
            embed.add_field(name="Webhook Token", value=f"```{webhook.token}```", inline=False)
            embed.set_thumbnail(url=webhook.avatar_url)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"""```ini
[ {webhook.name} Information ]

Webhook Name: {webhook.name}
Webhook ID: {webhook.id}
Webhook Guild: {webhook.guild.name}
Webhook Channel: {webhook.channel.name}
Webhook Token: {webhook.token}


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="dumpchat", description="Get the chat's history.", usage="dumpchat [amount] (channel id) (oldest first, true/false)", aliases=["savechat", "chathistory"])
    async def dumpchat(ctx, amount: int, channelId: int = None, oldestFirst: bool = False):
        if channelId is None:
            messages = await ctx.channel.history(limit=amount, oldest_first=oldestFirst).flatten()

            f = open("chat_history.txt", "a")
            try:
                f.write(f"Chat history for #{ctx.channel.name} in {ctx.guild.name}\nSaved a total of {len(messages)} messages.\n \n")
            except:
                f.write(f"Saved a total of {len(messages)} messages.\n \n")
            for msg in messages:
                try:
                    f.write(f"[{msg.created_at.strftime('%m/%d/%Y, %H:%M:%S')}] {msg.author.name}#{msg.author.discriminator}: {msg.content}\n")
                except:
                    pass

            f.close()

            await ctx.send("Generated the chat history.", file=discord.File("chat_history.txt"))
            os.remove("chat_history.txt")
        else:
            channel = Ghost.get_channel(channelId)
            messages = await channel.history(limit=amount, oldest_first=oldestFirst).flatten()

            f = open("chat_history.txt", "a")
            try:
                f.write(f"Chat history for #{channel.name} in {channel.guild.name}\nSaved a total of {len(messages)} messages.\n \n")
            except:
                f.write(f"Saved a total of {len(messages)} messages.\n \n")
            for msg in messages:
                try:
                    f.write(f"[{msg.created_at.strftime('%m/%d/%Y, %H:%M:%S')}] {msg.author.name}#{msg.author.discriminator}: {msg.content}\n")
                except:
                    pass

            f.close()

            await ctx.send("Generated the chat history.", file=discord.File("chat_history.txt"))
            os.remove("chat_history.txt")

    @Ghost.command(name="newtheme", description="Create a new theme with the given name.", usage="newtheme [name]", aliases=["createtheme"])
    async def newtheme(ctx, *, name):
        if not os.path.isfile(f'themes/{name}.json'):
            name = name.replace(" ", "-")
            f = open(f'themes/{name}.json', "w")
            f.write("""
{
"embedtitle": "Ghost Recoded",
"embedcolour": "#708ffa",
"embedfooter": "",
"embedfooterimage": "",
"globalemoji": ":ghost:",
"embedimage": ""
}
            """)
            f.close()
            if __embedmode__:
                embed = discord.Embed(title="Theme create with the name " + name, colour=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"""```ini
[ Theme create with the name {name} ]


# {__embedfooter__}```""", delete_after=__deletetimeout__)
        else:
            if __embedmode__:
                embed = discord.Embed(title="A theme with that name already exists", colour=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"""```ini
[ A theme with that name already exists ]


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="deltheme", description="Delete the named theme.", usage="deltheme [name]", aliases=["deletetheme", "removetheme"])
    async def deltheme(ctx, *, name):
        if not os.path.isfile(f'themes/{name}.json'):
            if __embedmode__:
                embed = discord.Embed(title="A theme with that name doesnt exist", colour=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"""```ini
[ A theme with that name doesnt exist ]


# {__embedfooter__}```""", delete_after=__deletetimeout__)
        else:
            os.remove(f'themes/{name}.json')
            if __embedmode__:
                embed = discord.Embed(title="Theme with the name " + name + " was deleted", colour=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"""```ini
[ Theme with the name {name} was deleted ]


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="theme", description="Change your current theme.", usage="theme [theme]", aliases=["settheme"])
    async def theme__(ctx, *, theme):
        if os.path.isfile(f'themes/{theme}.json'):
            Config.changeTheme(theme)

            if __embedmode__:
                embed = discord.Embed(title="That theme has been set", colour=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send(f"""```ini
[ That theme has been set ]


# {__embedfooter__}```""", delete_after=__deletetimeout__)
        else:
            if __embedmode__:
                embed = discord.Embed(title="A theme with that name doesnt exist", colour=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send(f"""```ini
[ A theme with that name doesnt exist ]


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="prefix", description="Set the command prefix.", usage="prefix [prefix]", aliases=["c"])
    async def prefix(ctx, *, prefix):
        Config.changePrefix(prefix)

        if __embedmode__:
            embed = discord.Embed(title=f"Prefix changed to `{prefix}`", colour=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"""```ini
[ Prefix changed to {prefix} ]


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="restart", description="Restart Ghost selfbot.", usage="restart", aliases=["reboot", "reload"])
    async def restart(ctx):
        print_info("Restarting ghost...")
        await ctx.send("Restarting ghost...")
        restart_bot()

    @Ghost.command(name="firstmessage", description="Get the first message in the command channel.", usage="firstmessage")
    async def firstmessage(ctx):
        messages = await ctx.channel.history(limit=1, oldest_first=True).flatten()
        for message in messages:
            firstMessage = message

        if __embedmode__:
            embed = discord.Embed(title="First Message", description=f"{firstMessage.jump_url}", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"First message: {firstMessage.jump_url}")

    @Ghost.command(name="haste", description="Upload text to Ghost's Haste site.", usage="haste [text]")
    async def haste(ctx, *, text):
        url = "https://haste.ghost.cool/haste"
        payload=f'password=h5MEn3ptby4XSdxJ&text={text}&username={ctx.author.name}'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '__cfduid=dffeb66149683e21f8e860ea28116dd7d1613823909'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        await ctx.send(response.text)

    @Ghost.command(name="shrug", description="Shrug your arms.", usage="shrug")
    async def shrug(ctx):
        await ctx.send(f"¯\_(ツ)_/¯")

    @Ghost.command(name="tableflip", description="Flip the table.", usage="tableflip")
    async def tableflip(ctx):
        await ctx.send("(╯°□°）╯︵ ┻━┻")

    @Ghost.command(name="unflip", description="Put the table back.", usage="unflip")
    async def unflip(ctx):
        await ctx.send("┬─┬ ノ( ゜-゜ノ)")

    # @Ghost.command(name="hide", description="Hide a message behind another message.", usage="hide [msg1] [msg2]")
    # async def hide(ctx, msg1, msg2):
    #     await ctx.send(msg1+hideText+msg2)

    @Ghost.command(name="blank", description="Send a blank message", usage="blank")
    async def blank(ctx):
        await ctx.send("** **")

    @Ghost.command(name="length", description="Get the length of a string.", usage="length [string]", aliases=["stringlength"])
    async def length(ctx, *, string):
        await ctx.send(f"Length of `{string}`: " + len(string))

    @Ghost.command(name="lmgtfy", description="Let me Google that for you.", usage="lmgtfy [search]", aliases=["letmegooglethatforyou"])
    async def lmgtfy(ctx, *, search):
        await ctx.send(f"https://lmgtfy.app/?q={search.replace(' ', '+')}")

    @Ghost.command(name="selfbotcheck", description="Checks for users using a selfbot.", usage="selfbotcheck")
    async def selfbotcheck(ctx):
        await ctx.send("Checking for users with a trash selfbot...\nPeople who react below are using a selfbot.")
        await ctx.send("GIVEAWAY")
        await ctx.send("🎉 **GIVEAWAY** 🎉")

    @Ghost.command(name="nukeserver", description="Delete all roles and channels in the command server.", usage="nukeserver", aliases=["nukeguild"])
    async def nukeserver(ctx):
        if __riskmode__:
            if ctx.author.guild_permissions.administrator:
                for channel in ctx.guild.channels:
                    try:
                        await channel.delete()
                    except:
                        pass
                for role in ctx.guild.roles:
                    try:
                        await role.delete()
                    except:
                        pass
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                                  

    @Ghost.command(name="destroyserver", description="Completely destroy the command server.", usage="destroyserver", aliases=["destroyguild"])
    async def destroyserver(ctx):
        if __riskmode__:
            if ctx.author.guild_permissions.administrator:
                for channel in ctx.guild.channels:
                    try:
                        await channel.delete()
                    except:
                        pass
                for role in ctx.guild.roles:
                    try:
                        await role.delete()
                    except:
                        pass            
                name = ''.join(random.choice(string.ascii_letters) for i in range(100))
                await ctx.guild.edit(name=name)
                for _ in range(500):
                    name = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(12, 18)))
                    await ctx.guild.create_text_channel(name=f'{name}')
                    await ctx.guild.create_role(name=f'{name}')
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                                  

    @Ghost.command(name="spamchannels", description="Spam create channels with a desired name. (Thanks Port <3)", usage="spamchannels [amount] (name)", aliases=["spamcreatechannels"])
    async def spamchannels(ctx, amount: int, *, name = None):
        if __riskmode__:
            if ctx.author.guild_permissions.manage_channels:
                if name is None:
                    for _ in range(amount):
                        name = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(12, 18)))
                        await ctx.guild.create_text_channel(name=f'{name}')
                else:
                    for _ in range(amount):
                        await ctx.guild.create_text_channel(name=f'{name}')
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                                      

    @Ghost.command(name="spamroles", description="Spam create roles with a desired name.", usage="spamroles [amount] (name)", aliases=["spamcreateroles"])
    async def spamroles(ctx, amount: int, *, name = None):
        if __riskmode__:
            if ctx.author.guild_permissions.manage_roles:
                if name is None:
                    for _ in range(amount):
                        name = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(12, 18)))
                        await ctx.guild.create_role(name=f'{name}')
                else:
                    for _ in range(amount):
                        await ctx.guild.create_role(name=f'{name}')
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                                      

    @Ghost.command(name="deletechannels", description="Delete all of the command server's channels.", usage="deletechannels", aliases=["delchannels", "removechannels"])
    async def deletechannels(ctx):
        if __riskmode__:
            if ctx.author.guild_permissions.manage_channels:
                for channel in ctx.guild.channels:
                    try:
                        await channel.delete()
                    except:
                        pass
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                                  

    @Ghost.command(name="deleteroles", description="Delete all of the command server's roles.", usage="deleteroles", aliases=["delroles", "removeroles"])
    async def deleteroles(ctx):
        if __riskmode__:
            if ctx.author.guild_permissions.manage_roles:
                for role in ctx.guild.roles:
                    try:
                        await role.delete()
                    except:
                        pass
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)      

    @Ghost.command(name="dmspam", description="Spam DM messages X amount of times.", usage="dmspam [amount] [delay] [@user] [message]", aliases=["spamdm"])
    async def dmspam(ctx, amount: int, delay: int, user: discord.User, *, message):
        if __riskmode__:
            for _ in range(amount):
                try:
                    await user.send(message)
                    await asyncio.sleep(delay)
                except:
                    pass
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                              

    @Ghost.command(name="threadspam", description="Spam create threads with a starting message.", usage="threadspam [delay] [amount] [addusers | true/false] [name] [startmessage]", aliases=["spamthreads", "spamcreatethreads"])
    async def threadspam(ctx, delay: int, amount: int, addusers: bool, name: str = "Ghost best selfbot!", *, startmessage: str):
        if __riskmode__:
            users = []
            
            try:
                await ctx.message.delete()
            except:
                pass

            def createThread(title, channel_id, start_message_id):
                return requests.request("post", f"https://discord.com/api/channels/{channel_id}/messages/{start_message_id}/threads", headers={"Authorization": __token__, "Content-Type": "application/json"}, data=json.dumps({"name": title}))
            def getUsers(guild, channel):
                DiscumClient = discum.Client(token=__token__, user_agent=f"{get_random_user_agent()}")
                @DiscumClient.gateway.command
                def pingpingbrbr(resp):
                    guild_id = f'{guild.id}'
                    channel_id = f'{channel.id}'
                    if resp.event.ready_supplemental:
                        DiscumClient.gateway.fetchMembers(guild_id, channel_id, wait=1)
                    if DiscumClient.gateway.finishedMemberFetching(guild_id):
                        DiscumClient.gateway.removeCommand(pingpingbrbr)
                        DiscumClient.gateway.close()
                DiscumClient.gateway.run()
                members = []
                for memberID in DiscumClient.gateway.session.guild(f'{guild.id}').members:
                    members.append(f"<@!{memberID}>")     

                return members         

            async def addUsers(users, channel_id):
                try:
                    requests.post(f"https://discord.com/api/channels/{channel_id}/messages", headers={"Authorization": __token__, "Content-Type": "application/json"}, data=json.dumps({"content": ' '.join(users)}))
                except:
                    pass

            if addusers:
                print_info("Fetching channel members...")
                users = getUsers(ctx.guild, ctx.channel)
                await asyncio.sleep(2)
                print(users)
                await asyncio.sleep(2)

            index = 0
            if not ctx.author.guild_permissions.administrator:
                if amount > 5:
                    print_info("Limiting amount of threads to 5 to prevent rate limits.")
                    amount = 5
            for _ in range(amount):
                index += 1
                try:
                    message = await ctx.send(startmessage + f" {index}")
                    createThredResponse = createThread(name, ctx.channel.id, message.id)
                    if addusers:
                        print_info("Adding users to the thread...")
                        await addUsers(users, createThredResponse.json()["id"])
                    print_info("Created a new thread.")
                    try:
                        await message.delete()
                    except:
                        pass
                    await asyncio.sleep(delay)
                except:
                    pass
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                              

    @Ghost.command(name="channelspam", description="Spam a message X amount of times in every channel.", usage="channelspam [amount] [delay] [message]", aliases=["sendall", "sendtoallchannels", "msgallchannels", "messageallchannels"])
    async def channelspam(ctx, amount:int, *, message:str):               
        if __riskmode__:
            for _ in range(amount):
                for channel in ctx.guild.text_channels:
                    try:
                        await channel.send(message)
                        await asyncio.sleep(1)
                    except:
                        pass
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                          

    @Ghost.command(name="spam", description="Spam X amount of times.", usage="spam [amount] [delay] [message]")
    async def spam(ctx, amount: int, delay: int, *, message):
        if __riskmode__:
            global spammingMessages
            spammingMessages = True
            async def spamMessages():
                for _ in range(amount):
                    if spammingMessages == True:
                        await ctx.send(message)
                        await asyncio.sleep(delay)
                    else:
                        return
            Ghost.loop.create_task(spamMessages())
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                      
        
    @Ghost.command(name="stopspam", description="Stop spamming messages.", usage="stopspam")
    async def stopspam(ctx):
        if __riskmode__:
            global spammingMessages
            spammingMessages = False
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                          

    @Ghost.command(name="ttsspam", description="Spam TTS messages X amount of times.", usage="ttsspam [amount] [delay] [message]", aliases=["texttospeachspam"])
    async def ttsspam(ctx, amount: int, delay: int, *, message):
        if __riskmode__:
            for _ in range(amount):
                await ctx.send(message, tts=True)
                await asyncio.sleep(delay)
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                              

    @Ghost.command(name="massghostping", description="Ping a mass amount of people in the command server and delete the messages.", usage="massghostping (amount of messages) (send delay)", aliases=["massghostmention", "theotherfunny"])
    async def massghostping(ctx, amount:int=1, delay:int=0):
        if __riskmode__:
            try:
                await ctx.message.delete()
            except:
                pass

            bot = discum.Client(token=__token__, log=False, user_agent=get_random_user_agent())

            def close_after_fetching(resp, guild_id):  
                if bot.gateway.finishedMemberFetching(guild_id):
                    print_info("Fetching complete.")
                    members = bot.gateway.session.guild(guild_id).members
                    bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()
                    print_info(f"Fetched a total of {len(members)} members.")
                    return members

            def get_members(guild_id, channel_id):
                print_info("Fetching members...")
                bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=0)
                bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            # members = []
            members = get_members(str(ctx.guild.id), str(ctx.channel.id))
            messages = []
            message = ""

            # for channel in ctx.guild.text_channels:
            #     print_info(f"Starting fetch in #{channel.name}.")
            #     members2 = get_members(str(ctx.guild.id), str(channel.id))
            #     for member in members2:
            #         members.append(member)

            # print_info(f"Fetched a total of {len(members)} members.")

            for member in members:
                if len(message) < 1950:
                    message += f"<@{member}> "
                else:
                    messages.append(message)
                    message = ""

            messages.append(message)

            for _ in range(amount):
                for message in messages:
                    try:
                        await ctx.send(message, delete_after=0)
                        await asyncio.sleep(delay)
                    except:
                        pass
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                                  

    @Ghost.command(name="massping", description="Ping a mass amount of people in the command server.", usage="massping (amount of messages) (send delay)", aliases=["massmention", "sigmainstaller", "hahafunny"])
    async def massping(ctx, amount:int=1, delay:int=0):
        if __riskmode__:
            try:
                await ctx.message.delete()
            except:
                pass

            bot = discum.Client(token=__token__, log=False, user_agent=get_random_user_agent())

            def close_after_fetching(resp, guild_id):          
                if bot.gateway.finishedMemberFetching(guild_id):
                    print_info("Fetching complete.")
                    members = bot.gateway.session.guild(guild_id).members
                    bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()
                    print_info(f"Fetched a total of {len(members)} members.")
                    return members

            def get_members(guild_id, channel_id):
                print_info("Fetching members...")
                bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=0)
                bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(str(ctx.guild.id), str(ctx.channel.id))
            messages = []
            message = ""

            for member in members:
                if len(message) < 1950:
                    message += f"<@{member}> "
                else:
                    messages.append(message)
                    message = ""

            messages.append(message)

            for _ in range(amount):
                for message in messages:
                    try:
                        await ctx.send(message)
                        await asyncio.sleep(delay)
                    except:
                        pass
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                                  
            
    @Ghost.command(name="massdm", description="Send a DM message to everyone in the server.", usage="massdm [delay] [amount] [message]")
    @commands.guild_only()
    async def massdm(ctx, delay:int=0, amount:int=10, *, message:str):
        if __riskmode__:
            try:
                await ctx.message.delete()
            except:
                pass

            bot = discum.Client(token=__token__, log=False, user_agent=get_random_user_agent())

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    print_info("Fetching complete.")
                    members = bot.gateway.session.guild(guild_id).members
                    bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()
                    print_info(f"Fetched a total of {len(members)} members.")
                    return members

            def get_members(guild_id, channel_id):
                print_info("Fetching members...")
                bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1)
                bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(str(ctx.guild.id), str(ctx.channel.id))

            for _ in range(amount):
                for member in members:
                    try:
                        member = await Ghost.fetch_user(int(member))
                        await member.send(message)
                    except:
                        pass
                    await asyncio.sleep(delay)
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                                  

    @Ghost.command(name="rickroll", description="Send never gonna give you up lyrics one by one.", usage="rickroll")
    async def rickroll(ctx):
        global rickRollEnabled
        rickRollEnabled = True
        
        async def sendLyrics():
            file1 = open('data/rickroll.txt', 'r')
            Lines = file1.readlines()
            for line in Lines:
                if rickRollEnabled == True:
                    await ctx.send(line)
                    await asyncio.sleep(1)
                else:
                    return
                
        Ghost.loop.create_task(sendLyrics())

    @Ghost.command(name="stoprickroll", description="Stop sending rick astley lyrics.", usage="stoprickroll")
    async def stoprickroll(ctx):
        global rickRollEnabled
        rickRollEnabled = False

    @Ghost.command(name="suggest", description="Suggest something.", usage="suggest [suggestion]")
    async def suggest(ctx, *, suggestion):
        if __embedmode__:
            embed = discord.Embed(title="Suggestion", description=suggestion, colour=__embedcolour__)
            embed.set_footer(text=ctx.author.name + " suggested.", icon_url=ctx.author.avatar_url)
            embed.timestamp = datetime.now()
            msg = await ctx.send(embed=embed)
        else:
            msg = await ctx.send(f"""```ini
[ Suggestion ]

{suggestion}


# {ctx.author.name} suggested.```""", delete_after=__deletetimeout__)
        await msg.add_reaction('\U0001F44D')
        await msg.add_reaction('\U0001F44E')

    @Ghost.command(name="massnick", description="Change the nickname of all members in the command server.", usage="massnick [nickname]", aliases=["massnickname", "masschangenickname"])
    async def massnick(ctx, *, nickname):
        if __riskmode__:
            try:
                await ctx.message.delete()
            except:
                pass

            bot = discum.Client(token=__token__, log=False, user_agent=get_random_user_agent())

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    print_info("Fetching complete.")
                    members = bot.gateway.session.guild(guild_id).members
                    bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()
                    print_info(f"Fetched a total of {len(members)} members.")
                    return members

            def get_members(guild_id, channel_id):
                print_info("Fetching members...")
                bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1)
                bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(str(ctx.guild.id), str(ctx.channel.id))

            for member in members:
                try:
                    member = await ctx.guild.fetch_member(int(member))
                    await member.edit(nick=nickname)
                    await asyncio.sleep(1)
                except:
                    pass
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                              

    @Ghost.command(name="massunnick", description="Reset the nickname of all members in the command server.", usage="massunnick", aliases=["massremovenickname", "massunnickname"])
    async def massunnick(ctx):
        try:
            await ctx.message.delete()
        except:
            pass

        bot = discum.Client(token=__token__, log=False, user_agent=get_random_user_agent())

        def close_after_fetching(resp, guild_id):
            if bot.gateway.finishedMemberFetching(guild_id):
                print_info("Fetching complete.")
                members = bot.gateway.session.guild(guild_id).members
                bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.close()
                print_info(f"Fetched a total of {len(members)} members.")
                return members

        def get_members(guild_id, channel_id):
            print_info("Fetching members...")
            bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1)
            bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.run()
            bot.gateway.resetSession()
            return bot.gateway.session.guild(guild_id).members

        members = get_members(str(ctx.guild.id), str(ctx.channel.id))

        for member in members:
            try:
                member = await ctx.guild.fetch_member(int(member))
                await member.edit(nick="")
                await asyncio.sleep(1)
            except:
                pass

    @Ghost.command(name="dadjoke", description="A random dad joke.", usage="dadjoke")
    async def dadjoke(ctx):
        url = "https://icanhazdadjoke.com/"

        payload={}
        headers = {
        'Accept': 'text/plain',
        'Cookie': '__cfduid=d6dccebb48b09fdeb9a97022fa2f292811612029832'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        if __embedmode__:
            embed = discord.Embed(description=response.text, colour=__embedcolour__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(response.text)

    @Ghost.command(name="randomquestion", description="A random question.", usage="randomquestion", aliases=["ranquestion"])
    async def randomquestion(ctx):
        question = requests.get("https://nekos.life/api/v2/why").json()["why"]

        if __embedmode__:
            embed = discord.Embed(description=question, colour=__embedcolour__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(question)                

    @Ghost.command(name="randommessage", description="A random message.", usage="randommessage", aliases=["ranmessage"])
    async def randommessage(ctx):
        url = "https://ajith-messages.p.rapidapi.com/getMsgs"

        querystring = {"category":"Random"}

        headers = {
            'x-rapidapi-key': "01eddf9d3cmsh5207aa226152e38p1f5a60jsn182a112b106d",
            'x-rapidapi-host': "ajith-messages.p.rapidapi.com"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        response_data = response.json()
        if __embedmode__:
            embed = discord.Embed(description=response_data["Message"], colour=__embedcolour__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(response_data["Message"])

    @Ghost.command(name="meme", description="A random meme.", usage="meme", aliases=["randommeme"])
    async def meme(ctx):
        response = requests.get("https://meme-api.herokuapp.com/gimme")
        data = response.json()
        if __embedmode__:
            embed = discord.Embed(title=data["title"], url=data["postLink"], colour=__embedcolour__)
            embed.set_image(url=data["url"])
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.set_author(name=f"u/{data['author']}", url=f"https://reddit.com/u/{data['author']}")
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(data["title"] + "\n" + data["url"])

    @Ghost.command(name="gif", description="Search for a gif.", usage="gif [search]", aliases=["searchgif"])
    async def gif(ctx, *, search):
        if CONFIG["api_keys"]["tenor"] == "":
            if __embedmode__:
                embed = discord.Embed(description="This command requires a tenor API key.", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send("This command requires a tenor API key.")                     
        else:                 
            search = search.replace(" ", "+")
            response = requests.get(f'https://g.tenor.com/v1/search?q={search}&key={CONFIG["api_keys"]["tenor"]}&limit=10000')
            data = response.json()
            #print(data['results'][0]["media"][0]["gif"]["url"])
            if __embedmode__:
                embed = discord.Embed(title=f"{search.replace('+', ' ')}", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                embed.set_image(url=data['results'][random.randint(0, 49)]["media"][0]["gif"]["url"])
                await ctx.send(embed=embed)
            else:
                await ctx.send(data['results'][random.randint(0, 49)]["media"][0]["gif"]["url"])     

    @Ghost.command(name="cat", description="A random cat image.", usage="cat", aliases=["randomcat"])
    async def cat(ctx):
        request = requests.get("https://cataas.com/cat?json=true").json()
        image = "https://cataas.com" + request["url"]
        if __embedmode__:
            embed = discord.Embed(title="meow", color=__embedcolour__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            embed.set_image(url=image)
            await ctx.send(embed=embed)
        else:
            await ctx.send(image)

    @Ghost.command(name="catgif", description="A random cat gif.", usage="catgif", aliases=["randomcatgif"])
    async def catgif(ctx):
        request = requests.get("https://cataas.com/cat/gif?json=true").json()
        image = "https://cataas.com" + request["url"]
        if __embedmode__:
            embed = discord.Embed(title="meow", color=__embedcolour__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            embed.set_image(url=image)
            await ctx.send(embed=embed)
        else:
            await ctx.send(image)

    @Ghost.command(name="dog", description="A random dog image.", usage="dog", aliases=["randomdog"])
    async def dog(ctx):
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        data = response.json()
        if __embedmode__:
            embed = discord.Embed(title="woof", color=__embedcolour__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            embed.set_image(url=data['message'])
            await ctx.send(embed=embed)
        else:
            await ctx.send(data['message'])

    @Ghost.command(name="shiba", description="A random shiba image.", usage="shiba", aliases=["randomshiba"])
    async def shiba(ctx):
        response = requests.get('https://shibe.online/api/shibes?count=1&httpsUrls=true')
        data = response.json()
        if __embedmode__:
            embed = discord.Embed(title="shiba", color=__embedcolour__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            embed.set_image(url=data[0])
            await ctx.send(embed=embed)
        else:
            await ctx.send(data[0])                    

    @Ghost.command(name="fox", description="A random fox image. (Thanks Imf44 <3)", usage="fox", aliases=["randomfox"])
    async def fox(ctx):
        response = requests.get('https://randomfox.ca/floof/')
        data = response.json()
        if __embedmode__:
            embed = discord.Embed(title="fox", color=__embedcolour__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            embed.set_image(url=data['image'])
            await ctx.send(embed=embed)
        else:
            await ctx.send(data['message'])

    @Ghost.command(name="achievement", description="Create a fake minecraft achievement image.", usage='achievement ["text"] (icon)', aliases=["minecraftachievement"])
    async def achievement(ctx, text, icon=10):
        if CONFIG["api_keys"]["alexflipnote"] == "":
            if __embedmode__:
                embed = discord.Embed(description="This command requires an alexflipnote API key.", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send("This command requires an alexflipnote API key.")                     
        else:
            icon = str(icon)
            text = text.replace(" ", "+")
            image = requests.get(f"https://api.alexflipnote.dev/achievement?text={text}&icon={icon}", headers={"Authorization": CONFIG["api_keys"]["alexflipnote"]})
            imageFile = open("image.png", "wb").write(image.content)
            file = discord.File("image.png", filename="image.png")
            if __embedmode__:
                embed = discord.Embed(color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file, embed=embed)
            else:
                await ctx.send(file=file)  
            os.remove("image.png")     

    @Ghost.command(name="challenge", description="Create a fake minecraft challenge image.", usage='challenge ["text"] (icon)', aliases=["minecraftchallenge"])
    async def challenge(ctx, text, icon=33):
        if CONFIG["api_keys"]["alexflipnote"] == "":
            if __embedmode__:
                embed = discord.Embed(description="This command requires an alexflipnote API key.", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send("This command requires an alexflipnote API key.")                     
        else:                
            text = text.replace(" ", "+")
            image = requests.get(f"https://api.alexflipnote.dev/challenge?text={text}&icon={icon}", headers={"Authorization": CONFIG["api_keys"]["alexflipnote"]})
            imageFile = open("image.png", "wb").write(image.content)
            file = discord.File("image.png", filename="image.png")
            if __embedmode__:
                embed = discord.Embed(color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file, embed=embed)
            else:
                await ctx.send(file=file)  
            os.remove("image.png")        

    @Ghost.command(name="captcha", description="Create a fake reCaptcha.", usage="captcha [text]", aliases=["fakecaptcha"])
    async def captcha(ctx, *, text):
        if CONFIG["api_keys"]["alexflipnote"] == "":
            if __embedmode__:
                embed = discord.Embed(description="This command requires an alexflipnote API key.", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send("This command requires an alexflipnote API key.")                     
        else:                
            text = text.replace(" ", "+")
            image = requests.get(f"https://api.alexflipnote.dev/captcha?text={text}", headers={"Authorization": CONFIG["api_keys"]["alexflipnote"]})
            imageFile = open("image.png", "wb").write(image.content)
            file = discord.File("image.png", filename="image.png")
            if __embedmode__:
                embed = discord.Embed(color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file, embed=embed)
            else:
                await ctx.send(file=file)  
            os.remove("image.png")                                                         

    @Ghost.command(name="amiajoke", description="Make a user a joke.", usage="amiajoke [@user]", aliases=["amiajoketoyou"])
    async def amiajoke(ctx, user:discord.User):
        if CONFIG["api_keys"]["alexflipnote"] == "":
            if __embedmode__:
                embed = discord.Embed(description="This command requires an alexflipnote API key.", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send("This command requires an alexflipnote API key.")                     
        else:                
            imageurl = avatarUrl(user.id, user.avatar)
            image = requests.get(f"https://api.alexflipnote.dev/amiajoke?image={imageurl}", headers={"Authorization": CONFIG["api_keys"]["alexflipnote"]})
            imageFile = open("image.png", "wb").write(image.content)
            file = discord.File("image.png", filename="image.png")
            if __embedmode__:
                embed = discord.Embed(color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file, embed=embed)
            else:
                await ctx.send(file=file)  
            os.remove("image.png")   

    @Ghost.command(name="didyoumean", description="Create a google did you mean image.", usage='didyoumean ["text 1"] ["text 2"]', aliases=["googledidyoumean"])
    async def didyoumean(ctx, text1="Nighty", text2="Ghost"):
        if CONFIG["api_keys"]["alexflipnote"] == "":
            if __embedmode__:
                embed = discord.Embed(description="This command requires an alexflipnote API key.", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send("This command requires an alexflipnote API key.")                     
        else:                
            text1 = text1.replace(" ", "+")
            text2 = text2.replace(" ", "+")
            image = requests.get(f"https://api.alexflipnote.dev/didyoumean?top={text1}&bottom={text2}", headers={"Authorization": CONFIG["api_keys"]["alexflipnote"]})
            imageFile = open("image.png", "wb").write(image.content)
            file = discord.File("image.png", filename="image.png")
            if __embedmode__:
                embed = discord.Embed(color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file, embed=embed)
            else:
                await ctx.send(file=file)  
            os.remove("image.png") 

    @Ghost.command(name="drake", description="Create a drake meme image.", usage='drake ["text 1"] ["text 2"]', aliases=["drakememe"])
    async def drake(ctx, text1="Nighty Selfbot", text2="Ghost Selfbot"):
        if CONFIG["api_keys"]["alexflipnote"] == "":
            if __embedmode__:
                embed = discord.Embed(description="This command requires an alexflipnote API key.", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send("This command requires an alexflipnote API key.")                     
        else:                
            text1 = text1.replace(" ", "+")
            text2 = text2.replace(" ", "+")
            image = requests.get(f"https://api.alexflipnote.dev/drake?top={text1}&bottom={text2}", headers={"Authorization": CONFIG["api_keys"]["alexflipnote"]})
            imageFile = open("image.png", "wb").write(image.content)
            file = discord.File("image.png", filename="image.png")
            if __embedmode__:
                embed = discord.Embed(color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file, embed=embed)
            else:
                await ctx.send(file=file)  
            os.remove("image.png")                     

    @Ghost.command(name="facts", description="Create a facts meme image.", usage='facts [text]', aliases=["factsmeme"])
    async def facts(ctx, *, text):
        if CONFIG["api_keys"]["alexflipnote"] == "":
            if __embedmode__:
                embed = discord.Embed(description="This command requires an alexflipnote API key.", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send("This command requires an alexflipnote API key.")                     
        else:                
            text = text.replace(" ", "+")
            image = requests.get(f"https://api.alexflipnote.dev/drake?text={text}", headers={"Authorization": CONFIG["api_keys"]["alexflipnote"]})
            imageFile = open("image.png", "wb").write(image.content)
            file = discord.File("image.png", filename="image.png")
            if __embedmode__:
                embed = discord.Embed(color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file, embed=embed)
            else:
                await ctx.send(file=file)  
            os.remove("image.png")

    @Ghost.command(name="jokeoverhead", description="Create a joke over head image.", usage="jokeoverhead [image url]")
    async def jokeoverhead(ctx, *, imageurl):
        if CONFIG["api_keys"]["alexflipnote"] == "":
            if __embedmode__:
                embed = discord.Embed(description="This command requires an alexflipnote API key.", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send("This command requires an alexflipnote API key.")                     
        else:                
            image = requests.get(f"https://api.alexflipnote.dev/jokeoverhead?image={imageurl}", headers={"Authorization": CONFIG["api_keys"]["alexflipnote"]})
            imageFile = open("image.png", "wb").write(image.content)
            file = discord.File("image.png", filename="image.png")
            if __embedmode__:
                embed = discord.Embed(color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file, embed=embed)
            else:
                await ctx.send(file=file)  
            os.remove("image.png")               

    @Ghost.command(name="pornhub", description="Create a pornhub logo image.", usage='pornhub ["text 1"] ["text 2"]')
    async def pornhub(ctx, text1="Ghost", text2="Selfbot"):
        if CONFIG["api_keys"]["alexflipnote"] == "":
            if __embedmode__:
                embed = discord.Embed(description="This command requires an alexflipnote API key.", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send("This command requires an alexflipnote API key.")                     
        else:                
            text1 = text1.replace(" ", "+")
            text2 = text2.replace(" ", "+")
            image = requests.get(f"https://api.alexflipnote.dev/pornhub?text={text1}&text2={text2}", headers={"Authorization": CONFIG["api_keys"]["alexflipnote"]})
            imageFile = open("image.png", "wb").write(image.content)
            file = discord.File("image.png", filename="image.png")
            if __embedmode__:
                embed = discord.Embed(color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file, embed=embed)
            else:
                await ctx.send(file=file)  
            os.remove("image.png")

    @Ghost.command(name="salty", description="Make someone salty.", usage="salty [@user]")
    async def jokeoverhead(ctx, user:discord.User):
        if CONFIG["api_keys"]["alexflipnote"] == "":
            if __embedmode__:
                embed = discord.Embed(description="This command requires an alexflipnote API key.", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send("This command requires an alexflipnote API key.")                     
        else:                
            imageurl = avatarUrl(user.id, user.avatar)
            image = requests.get(f"https://api.alexflipnote.dev/salty?image={imageurl}", headers={"Authorization": CONFIG["api_keys"]["alexflipnote"]})
            imageFile = open("image.png", "wb").write(image.content)
            file = discord.File("image.png", filename="image.png")
            if __embedmode__:
                embed = discord.Embed(color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file, embed=embed)
            else:
                await ctx.send(file=file)  
            os.remove("image.png")

    @Ghost.command(name="ship", description="Ship two people.", usage="ship [@user 1] [@user 2]")
    async def ship(ctx, user1:discord.User, user2:discord.User):
        if CONFIG["api_keys"]["alexflipnote"] == "":
            if __embedmode__:
                embed = discord.Embed(description="This command requires an alexflipnote API key.", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send("This command requires an alexflipnote API key.")                     
        else:                
            user1 = avatarUrl(user1.id, user1.avatar)
            user2 = avatarUrl(user2.id, user2.avatar)
            image = requests.get(f"https://api.alexflipnote.dev/ship?user={user1}&user2={user2}", headers={"Authorization": CONFIG["api_keys"]["alexflipnote"]})
            imageFile = open("image.png", "wb").write(image.content)
            file = discord.File("image.png", filename="image.png")
            if __embedmode__:
                embed = discord.Embed(color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file, embed=embed)
            else:
                await ctx.send(file=file)  
            os.remove("image.png")

    @Ghost.command(name="supreme", description="Create a supreme logo image.", usage='supreme [text]')
    async def supreme(ctx, *, text):
        if CONFIG["api_keys"]["alexflipnote"] == "":
            if __embedmode__:
                embed = discord.Embed(description="This command requires an alexflipnote API key.", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send("This command requires an alexflipnote API key.")                     
        else:                
            text = text.replace(" ", "+")
            image = requests.get(f"https://api.alexflipnote.dev/supreme?text={text}", headers={"Authorization": CONFIG["api_keys"]["alexflipnote"]})
            imageFile = open("image.png", "wb").write(image.content)
            file = discord.File("image.png", filename="image.png")
            if __embedmode__:
                embed = discord.Embed(color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file, embed=embed)
            else:
                await ctx.send(file=file)  
            os.remove("image.png")

    @Ghost.command(name="trash", description="Put someone in the trash.", usage='trash [@user]')
    async def trash(ctx, user: discord.User):
        if CONFIG["api_keys"]["alexflipnote"] == "":
            if __embedmode__:
                embed = discord.Embed(description="This command requires an alexflipnote API key.", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send("This command requires an alexflipnote API key.")                     
        else:                
            trash = avatarUrl(user.id, user.avatar)
            face = avatarUrl(Ghost.user.id, Ghost.user.avatar)
            image = requests.get(f"https://api.alexflipnote.dev/trash?trash={trash}&face={face}", headers={"Authorization": CONFIG["api_keys"]["alexflipnote"]})
            imageFile = open("image.png", "wb").write(image.content)
            file = discord.File("image.png", filename="image.png")
            if __embedmode__:
                embed = discord.Embed(color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file, embed=embed)
            else:
                await ctx.send(file=file)  
            os.remove("image.png")

    @Ghost.command(name="what", description="Make a what meme.", usage='what [image url]')
    async def what(ctx, *, imageurl):
        if CONFIG["api_keys"]["alexflipnote"] == "":
            if __embedmode__:
                embed = discord.Embed(description="This command requires an alexflipnote API key.", color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send("This command requires an alexflipnote API key.")                     
        else:                
            image = requests.get(f"https://api.alexflipnote.dev/what?image={imageurl}", headers={"Authorization": CONFIG["api_keys"]["alexflipnote"]})
            imageFile = open("image.png", "wb").write(image.content)
            file = discord.File("image.png", filename="image.png")
            if __embedmode__:
                embed = discord.Embed(color=__embedcolour__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                embed.set_image(url="attachment://image.png")
                await ctx.send(file=file, embed=embed)
            else:
                await ctx.send(file=file)  
            os.remove("image.png")

    @Ghost.command(name="purgehack", description="Purge without permissions.", usage="purgehack")
    async def purgehack(ctx):
        await ctx.send(f"** **\n"*100)

    @Ghost.command(name="iq", description="Check how smart a user is.", usage="iq [@user]")
    async def iq(ctx, user: discord.User):
        iq = random.randint(45, 135)
        smart = ""

        if user.id == 858034873415368715:
            iq = 45

        if iq > 90 and iq < 135:
            smart = "They're very smart!"
        if iq > 70 and iq < 90:
            smart = "They're just below average."
        if iq > 50 and iq < 70:
            smart = "They might have some issues."
        if iq > 40 and iq < 50:
            smart = "They're severely retarded."

        if __embedmode__:
            embed = discord.Embed(title=f"{user.name}'s iq is `{iq}`.", description=f"{smart}", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{user}'s iq is `{iq}`. {smart}")                

    @Ghost.command(name="howskid", description="Check the percentage of a skid.", usage="howskid [item]")
    async def howskidd(ctx, *, item):
        percentage = random.randint(0, 100)

        if __embedmode__:
            embed = discord.Embed(title="Skid Detection", description=f"{item} is {percentage}% skidded!", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()

            await ctx.send(embed=embed)
        else:
            await ctx.send(f"`{item}` is {percentage}% skidded!")

    @Ghost.command(name="howgay", description="How gay a user is.", usage="howgay [@user]")
    async def howgay(ctx, user: discord.User):
        percentage = str(random.randint(15, 100)) + "%"
        if __embedmode__:
            embed = discord.Embed(title=f"🏳️‍🌈 {user.name} is {percentage} gay", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"🏳️‍🌈 {user} is {percentage} gay")        

    @Ghost.command(name="slots", description="Play the slot machine.", usage="slots")
    async def slots(ctx):

        if __embedmode__:
            embed = discord.Embed(title=f"Slots", color=__embedcolour__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()

            message = await ctx.send(embed=embed)
        else:
            message = await ctx.send(f"""```ini
[ Slots ]

# {__embedfooter__}
```""")

        emojis = [("🍒", 0.01), ("🍊", 0.02), ("🍎", 0.06), ("💎", 0.08), ("🍆", 0.14), ("🍉", 0.24), ("🎰", 0.36)]
        emojis2 = []

        for emoji, probability in emojis:
            emojis2 += emoji*int(probability*100)

        async def game():
            amount = 8
            delay = 0.5
            dots = "."

            reel_1 = ""
            reel_2 = ""
            reel_3 = ""
            final_reel = ""

            for _ in range(amount):
                delay += 0.02
                dots += "."
                if dots == "....":
                    dots = "."

                reel_1 = random.choice(emojis2)
                reel_2 = random.choice(emojis2)
                reel_3 = random.choice(emojis2)

                final_reel = reel_1 + " | " + reel_2 + " | " + reel_3
                if __embedmode__:
                    embed = discord.Embed(title=f"Spinning{dots}", description=final_reel, color=__embedcolour__)
                    embed.timestamp = datetime.now()                            
                    await message.edit(content="", embed=embed)
                else:
                    await message.edit(content=f"""```ini
[ Spinning{dots} ]

{final_reel}


# {__embedfooter__}
```""")                            
                await asyncio.sleep(delay)

            if reel_1 == reel_2 and reel_1 == reel_3 and reel_2 == reel_3:
                if __embedmode__:
                    embed = discord.Embed(title=f"You won!", description=final_reel, color=__embedcolour__)
                    embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                    embed.timestamp = datetime.now()                            
                    await message.edit(content="", embed=embed)
                else:
                    await message.edit(content=f"""```ini
[ You won! ]

{final_reel}


# {__embedfooter__}
```""")                                   
            else:
                if __embedmode__:
                    embed = discord.Embed(title=f"You lost ;(", description=final_reel, color=__embedcolour__)
                    embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                    embed.timestamp = datetime.now()                            
                    await message.edit(content="", embed=embed)
                else:
                    await message.edit(content=f"""```ini
[ You lost ;( ]

{final_reel}


# {__embedfooter__}
```""")                               

        await game()


    @Ghost.command(name="socialcredit", description="A users social credit score.", usage="socialcredit [@user]")
    async def socialcredit(ctx, user: discord.User):
        credit = random.randint(-5000000, 10000000)
        if __embedmode__:
            embed = discord.Embed(description=f"{user.name}'s social credit score is {credit}", color=__embedcolour__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{user.name}'s social credit score is {credit}")                

    @Ghost.command(name="roast", description="Roast a user.", usage="roast [@user]", aliases=["insult"])
    async def roast(ctx, user: discord.User):
        insult = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json").json()["insult"]
        if __embedmode__:
            embed = discord.Embed(description=insult, colour=__embedcolour__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(user.mention, embed=embed)
        else:
            await ctx.send(f"Ayo {user.mention}, " + str(insult).lower())

    @Ghost.command(name="yomomma", description="Random yo momma joke.", usage="yomomma", aliases=["mom", "mum"])
    async def yomomma(ctx):
        joke = requests.get("https://api.yomomma.info/").json()["joke"]
        if __embedmode__:
            embed = discord.Embed(description=joke, colour=__embedcolour__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(joke)

    @Ghost.command(name="fakeedited", description='"Edit" a message.', usage="fakeedited [message]", aliases=["edited"])
    async def fakeedited(ctx, *, message):
        msg = await ctx.send(message)
        await msg.edit(content=message + " hehe")
        await msg.edit(content=message)

    @Ghost.command(name="pp", description="The length of a user's penis.", usage="pp (@user)", aliases=["dicksize", "cocksize", "penissize"])
    async def pp(ctx, user: discord.User = None):
        size = "8" + "="*random.randint(1, 12) + "D"
        if user is None:
            if __embedmode__:
                embed = discord.Embed(title=f"{Ghost.user.name}'s pp is {size}", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"{Ghost.user.name}'s pp size\n{size}")
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"{user.name}'s pp is {size}", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"{user.name}'s pp size\n{size}")

    # @Ghost.command(name="trumptweet", description="Make Donald Trump tweet anything.", usage="trumptweet [tweet]")
    # async def trumptweet(ctx, *, tweet):
    #     img = Image.open("trump-tweets/assets/bg.png")
    #     draw = ImageDraw.Draw(img)
    #     font = ImageFont.truetype('trump-tweets/assets/roboto.ttf', 30)
    #     draw.text((39, 123),f"{tweet}",(0,0,0),font=font)

    #     randomnum = random.randint(1000, 9999)
    #     img.save(f'trump-tweets/{randomnum}.png')

    #     file = discord.File(f'trump-tweets/{randomnum}.png')
    #     try:
    #         embed = discord.Embed(title='Trump Tweeted...', color=__embedcolour__)
    #         embed.set_image(url=f'attachment://{randomnum}.png')
    #         embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
    #         embed.timestamp = datetime.now()
    #         await ctx.send(file=file, embed=embed)
    #     except discord.HTTPException:
    #         await ctx.send(file=file)

    @Ghost.command(name="rainbowrole", description="Kill Discord's API with a sexy rainbow role.", usage="rainbowrole [@role]")
    async def rainbowrole(ctx, *, role: discord.Role):
        oldcolour = role.color
        red = Color("#ff3d3d")
        pink = Color("#f54287")
        rainbow = list(red.range_to(pink, 50))
        if __embedmode__:
            embed = discord.Embed(title=f"Rainbow Role", color=__embedcolour__, description=f"{role} now has a rainbow colour.")
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send(f"""```ini
[ Rainbow Role ]

{role} now has a rainbow colour.


# {__embedfooter__}```""", delete_after=__deletetimeout__)

        for _ in range(5):
            for x in rainbow:
                colour = f'{x}'
                await role.edit(color=int(colour.replace('#', '0x'), 0))
        await role.edit(color=oldcolour)

    @Ghost.command(name="rembed", description="Kill Discord's API with a sexy rainbow embedded message.", usage="rembed [text]", aliases=["rainbowembed"])
    async def rembed(ctx, *, text):
        if __embedmode__:
            red = Color("#ff3d3d")
            pink = Color("#f54287")
            rainbow = list(red.range_to(pink, 25))
            embed = discord.Embed(color=int("#ff3d3d".replace('#', '0x'), 0))
            embed.set_author(name=text)
            msg = await ctx.send(embed=embed)
            for _ in range(5):
                for x in rainbow:
                    colour = f'{x}'
                    newembed = discord.Embed(color=int(colour.replace('#', '0x'), 0))
                    newembed.set_author(name=text)
                    await msg.edit(embed=newembed)
            await msg.edit(embed=discord.Embed(color=int("#f54287".replace("#", "0x"), 0)).set_author(name=text))
        else:
            await ctx.send("This command can only be used in embed mode.")

    @Ghost.command(name="coinflip", description="Flip a coin.", usage="coinflip", aliases=["flipacoin"])
    async def coinflip(ctx):
        choices = ["Heads", "Tails"]
        choice = random.choice(choices)
        if __embedmode__:
            embed = discord.Embed(title=f"{choice}", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(choice)

    @Ghost.command(name="dice", description="Roll a dice.", usage="dice", aliases=["rolladice"])
    async def dice(ctx):
        choice = random.randint(1,6)
        if __embedmode__:
            embed = discord.Embed(title=f"{choice}", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(choice)

    @Ghost.command(name="rps", description="Rock, paper, scissors.", usage="rps", aliases=["rockpaperscissors"])
    async def rps(ctx, move = None):
        if move is not None:
            choices = ["Rock", "Paper", "Scissors"]
            computer = random.choice(choices)

            try:
                try:
                    player = move

                    if player == computer:
                        e = discord.Embed(title=f'Tie!', description=f'We chose the same!', color=__embedcolour__)

                    elif player == 'Rock' and computer == 'Scissors':
                        e = discord.Embed(title=f'Player wins!', description=f'{player} smashes {computer}!', color=__embedcolour__)

                    elif player == 'Rock' and computer == 'Paper':
                        e = discord.Embed(title=f'Computer wins!', description=f'{computer} covers {player}!', color=__embedcolour__)

                    elif player == 'Paper' and computer == 'Rock':
                        e = discord.Embed(title=f'Player wins!', description=f'{player} covers {computer}!', color=__embedcolour__)

                    elif player == 'Paper' and computer == 'Scissors':
                        e = discord.Embed(title=f'Computer wins!', description=f'{computer} cuts {player}!', color=__embedcolour__)

                    elif player == 'Scissors' and computer == 'Paper':
                        e = discord.Embed(title=f'Player wins!', description=f'{player} cuts {computer}!', color=__embedcolour__)

                    elif player == "Scissors" and computer == 'Rock':
                        e = discord.Embed(title=f'Computer wins!', description=f'{computer} smashes {player}!', color=__embedcolour__)

                    else:
                        e = discord.Embed(title=f'Invalid play', description=f'Try either Rock, Paper or Scissors.', color=__embedcolour__)

                    e.set_thumbnail(url=__embedimage__)
                    e.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                    e.timestamp = datetime.now()
                    await ctx.send(embed=e)

                except IndexError:
                    e = discord.Embed(title=f'Invalid play', description=f'Try either Rock, Paper or Scissors.', color=__embedcolour__)
                    e.set_thumbnail(url=__embedimage__)
                    e.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                    e.timestamp = datetime.now()
                    await ctx.send(embed=e)
            except:
                pass
        else:
            e = discord.Embed(title=f'Invalid play', description=f'Try either Rock, Paper or Scissors.', color=__embedcolour__)
            e.set_thumbnail(url=__embedimage__)
            e.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            e.timestamp = datetime.now()
            await ctx.send(embed=e)

    @Ghost.command(name="8ball", description="Ask the magic eight ball a question.", usage="8ball [question]", aliases=["eightball", "magic8ball"])
    async def eightball(ctx, *, question):
        choices = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it."]
        choice = random.choice(choices)
        choice = "8ball says, " + choice
        if __embedmode__:
            embed = discord.Embed(title=f"{question}", description=choice, color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(question + "\n" + choice)

    @Ghost.command(name="choice", description="Pick a random choice.", usage="choice [choice1] [choice2]", aliases=["pick"])
    async def choice(ctx, choice1, choice2):
        choices = [choice1, choice2]
        choice = random.choice(choices)
        if __embedmode__:
            embed = discord.Embed(title=f"{choice}", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(choice)

    # @Ghost.command(name="wyr", description="Would you rather questions.", usage="wyr")
    # async def wyr_(ctx):
    #     question, _ = wyr()

    #     embed = discord.Embed(title="Would You Rather", description=question, color=__embedcolour__)
    #     embed.set_thumbnail(url=__embedimage__)
    #     embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
    #     embed.timestamp = datetime.now()
    #     await ctx.send(embed=embed)

    #     # await message.add_reaction("\U0001F7E6")
    #     # await message.add_reaction("\U0001F7E5")

    @Ghost.command(name="dox", description="Dox the mentioned user.", usage="dox [@user]")
    async def dox(ctx, *, user: discord.User):
        randint1 = random.randint(100, 270)
        randint2 = random.randint(100, 270)
        randint3 = random.randint(10, 40)
        randint4 = random.randint(100, 270)
        countries = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia &amp; Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kuwait","Kyrgyz Republic","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Namibia","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre &amp; Miquelon","Samoa","San Marino","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","South Africa","South Korea","Spain","Sri Lanka","St Kitts &amp; Nevis","St Lucia","St Vincent","St. Lucia","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad &amp; Tobago","Tunisia","Turkey","Turkmenistan","Turks &amp; Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]
        computer = ['Windows', 'Mac', 'Linux', 'IOS', 'Android', 'Unknown']
        if __embedmode__:
            embed = discord.Embed(title=f"Doxxed {user.name}", color=__embedcolour__)
            embed.add_field(name="IP Address", value=f"```{randint1}.{randint2}.{randint3}.{randint4}```")
            embed.add_field(name="Country", value="```" + random.choice(countries) + "```")
            embed.add_field(name="Computer", value="```" + random.choice(computer) + "```")
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Doxxed {user.name}\nIP Address: {randint1}.{randint2}.{randint3}.{randint4}\nCountry: " + random.choice(countries) + "\nComputer: " + random.choice(computer))

    @Ghost.command(name="fakenitro", description="Hide a link in a nitro URL.", usage="fakenitro [url]")
    async def fakenitro(ctx, *, url):
        code = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))
        nitro = "https://discord.gift/" + code
        if __embedmode__:
            embed = discord.Embed(title=f"Nitro", color=__embedcolour__, description=f"[{nitro}]({url})")
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send("This command can only be used in embed mode.")

    @Ghost.command(name="nitrogen", description="Generate a nitro code.", usage="nitrogen", aliases=["nitrogenerate", "generatenitro", "gennitro"])
    async def nitrogen(ctx):
        code = ''.join(random.choice(string.ascii_letters + string.digits ) for i in range(19))
        nitro = "https://discord.gift/" + code
        if __embedmode__:
            embed = discord.Embed(title=f"Nitro", color=__embedcolour__, description=f"{nitro}")
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(nitro)

    @Ghost.command(name="tokengen", description="Generate a discord user token.", usage="tokengen", aliases=["generatetoken", "tokengenerate", "gentoken"])
    async def tokengen(ctx):
        authorId = str(ctx.author.id)

        message_bytes = authorId.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)

        token1 = base64_bytes.decode('ascii')
        token2 = ''.join(random.choice(string.ascii_letters + string.digits ) for i in range(6))
        token3 = ''.join(random.choice(string.ascii_letters + string.digits ) for i in range(27))

        token = f"{token1}.{token2}.{token3}"
        if __embedmode__:
            embed = discord.Embed(title=f"Token Generator", color=__embedcolour__, description=f"{token}")
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(token)

    @Ghost.command(name="identitygen", description="Generate a fake identity.", usage="identitygen", aliases=["identitygenerate", "generateidentity", "genidentity"])
    async def identitygen(ctx):

        firstname = fake.first_name()
        lastname = fake.last_name()
        address = fake.address()
        job = fake.job()
        phone = fake.phone_number()
        emails = ["gmail.com", "yahoo.com", "yahoo.co.uk"]
        emailchoice = random.choice(emails)
        email = f"{firstname}.{lastname}@{emailchoice}"
        birthdate = fake.date_of_birth()
        genderchoices = ["Male", "Female"]
        gender = random.choice(genderchoices)

        if __embedmode__:
            embed = discord.Embed(title=f"Identity Generator", color=__embedcolour__)
            embed.add_field(name="Full Name", value=f"{firstname} {lastname}", inline=True)
            embed.add_field(name="Email", value=f"{email}", inline=True)
            embed.add_field(name="Phone Number", value=f"{phone}", inline=True)
            embed.add_field(name="Occupation", value=f"{job}", inline=True)
            embed.add_field(name="Birthdate", value=f"{birthdate}", inline=True)
            embed.add_field(name="Gender", value=f"{gender}", inline=True)
            embed.add_field(name="Address", value=f"{address}", inline=True)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"""```ini
[ Identity Generator ]

Full Name: {firstname} {lastname}
Email: {email}
Phone Number: {phone}
Occupation: {job}
Birthdate: {birthdate}
Gender: {gender}
Address: {address}


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="passwordgen", description="Generate a secure password.", usage="passwordgen [length]", aliases=["passwordgenerate", "generatepassword", "genpassword"])
    async def passwordgen(ctx, length: int):
        password = ''.join(random.choice(string.ascii_letters) for i in range(length))

        if __embedmode__:
            embed = discord.Embed(title="Password Generator", color=__embedcolour__, description=f"Your generated password is ||{password}||")
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"Password: ||{password}||")

    @Ghost.command(name="ccgen", description="Generate a fake Credit card.", usage="ccgen", aliases=["creditcardgenerate", "creditcardgen", "generatecc", "ccgenerate", "gencreditcard", "generatecreditcard"])
    async def ccgen(ctx):

        name = names.get_full_name()
        address = fake.address()
        cvv = random.randint(100, 999)

        expiremonth = random.randint(1, 12)
        expireyear = now.year + random.randint(1, 4)

        choices = [4,5,6]
        choice = random.choice(choices)
        if choice == 4:
            type = "Visa"
            typeimg = "https://ghost.cool/assets/visa.png"
        elif choice == 5:
            type = "Mastercard"
            typeimg = "https://ghost.cool/assets/mastercard.png"
        elif choice == 6:
            type = "Discover"
            typeimg = "https://ghost.cool/assets/discover.png"

        string1 = random.randint(100, 999)
        string2 = random.randint(1000, 9999)
        string3 = random.randint(1000, 9999)
        string4 = random.randint(1000, 9999)

        if __embedmode__:
            embed = discord.Embed(title="Credit Card Generator", color=__embedcolour__)
            embed.add_field(name="Number", value=f"{choice}{string1} {string2} {string3} {string4}", inline=True)
            embed.add_field(name="Name", value=f"{name}", inline=True)
            embed.add_field(name="CVV", value=f"{cvv}", inline=True)
            embed.add_field(name="Expire Date", value=f"{expiremonth}/{expireyear}", inline=True)
            embed.add_field(name="Type", value=f"{type}", inline=True)
            embed.add_field(name="Address", value=f"{address}", inline=True)

            embed.set_thumbnail(url=typeimg)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"""```ini
[ Credit Card Generator ]

Number: {choice}{string1} {string2} {string3} {string4}
Name: {name}
CVV: {cvv}
Expire Date: {expiremonth}/{expireyear}
Type: {type}
Address: {address}


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="cembed", description="Create a custom embedded message.", usage='cembed [title] [description] [colour]', aliases=["customembed"])
    async def cembed(ctx, title, description, colour):
        if __embedmode__:
            colour = int(colour.replace('#', '0x'), 0)
            embed = discord.Embed(title=title, description=description, color=colour)
            await ctx.send(embed=embed)
        else:
            await ctx.send("This command can only be used in embed mode.")

    @Ghost.command(name="embed", description="Create an embedded message.", usage="embed [title]")
    async def embed(ctx, *, title):
        if __embedmode__:
            embed = discord.Embed(title=title, color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send("This command can only be used in embed mode.")

    @Ghost.command(name="leet", description="Turn your text into 1337 text.", usage="leet [text]", aliases=["1337", "leetspeak"])
    async def leet(ctx, *, text):
        text = text.replace(" ", "+")
        await ctx.send(requests.get(f"https://ghost.cool/api/fun/leet?text={text}").text)

    @Ghost.command(name="zalgo", description="Unleash the zalgo into your message.", usage="zalgo [text]")
    async def zalgo(ctx, *, text):
        text = text.replace(" ", "+")
        await ctx.send(requests.get(f"https://ghost.cool/api/fun/zalgo?text={text}").text)

    @Ghost.command(name="upsidedown", description="Flip your text upsidedown.", usage="upsidedown [text]")
    async def upsidedown(ctx, *, text):
        text = text.replace(" ", "+")
        await ctx.send(requests.get(f"https://ghost.cool/api/fun/upsidedown?text={text}").text)

    @Ghost.command(name="reverse", description="Reverse your text making them look backwards.", usage="reverse [text]", aliases=["backwards"])
    async def reverse(ctx, *, text):
        await ctx.send(''.join(list(reversed(text))))

    @Ghost.command(name="ascii", description="Send your message in ascii.", usage="ascii [text]")
    async def ascii(ctx, *, text):
        message = text
        art = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(message)}+&font=standard').text
        await ctx.send(f"```{art}```")

    @Ghost.command(name="privatemsg", description="Send an encrypted message.", usage="privatemsg [message]", aliases=["b64encode", "privatemessage"])
    async def privatemsg(ctx, *, message):
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        await ctx.send(base64_message)

    @Ghost.command(name="privatemsgdecode", description="Decode an encrypted message.", usage="privatemsgdecode [message]", aliases=["b64decode", "privatemessagedecode"])
    async def privatemsgdecode(ctx, *, message):
        base64_message = message
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')

        await ctx.send(message)

    @Ghost.command(name="encodebinary", description="Encode a message in binary.", usage="encodebinary [message]", aliases=["binaryencode", "binary"])
    async def encodebinary(ctx, *, message):
        translation = ""

    @Ghost.command(name="decodebinary", description="Decode a message in binary.", usage="decodebinary [message]", aliases=["binarydecode", "unbinary"])
    async def decodebinary(ctx, *, message):
        translation = ""

    @Ghost.command(name="encodemorse", description="Encode a message in morsecode", usage="encodemorse [message]", aliases=["morseencode", "morse"])
    async def encodemorse(ctx, *, message):
        text = message.replace(" ", "+")
        await ctx.send(requests.get(f"https://ghost.cool/api/fun/encodemorse?text={text}").text)

    @Ghost.command(name="decodemorse", description="Decode a message in morsecode", usage="decodemorse [message]", aliases=["morsedecode", "unmorse"])
    async def decodemorse(ctx, *, message):
        text = message.replace(" ", "+")
        await ctx.send(requests.get(f"https://ghost.cool/api/fun/decodemorse?text={text}").text)                

    @Ghost.command(name="secret", description="Send all your messages in a secret block.", usage="secret [message]")
    async def secret(ctx, *, message):
        await ctx.send('||' + message + '||')

    @Ghost.command(name="secretletters", description="Put all lettes from your message into separate secret blocks", usage="secretletters [message]")
    async def secretletters(ctx, *, message):
        def split(word):
            return list(word)
        msg = ""
        for letter in split(message):
            msg += "||" + letter +  "||"
        await ctx.send(msg)

    @Ghost.command(name="bold", description="Send all your messages in bold.", usage="bold [message]")
    async def bold(ctx, *, message):
        await ctx.send('**' + message + '**')

    @Ghost.command(name="italic", description="Send all your messages in italics.", usage="italic [message]")
    async def italic(ctx, *, message):
        await ctx.send('*' + message + '*')

    @Ghost.command(name="cpp", description="Send all your messages in a C++ code block.", usage="cpp [message]")
    async def cpp(ctx, *, message):
        await ctx.send(f"""```cpp\n{message}```""")

    @Ghost.command(name="cs", description="Send all your messages in a C Sharp code block.", usage="cs [message]")
    async def cs(ctx, *, message):
        await ctx.send(f"""```cs\n{message}```""")

    @Ghost.command(name="java", description="Send all your messages in a Java code block.", usage="java [message]")
    async def java(ctx, *, message):
        await ctx.send(f"""```java\n{message}```""")

    @Ghost.command(name="python", description="Send all your messages in a Python code block.", usage="python [message]")
    async def python(ctx, *, message):
        await ctx.send(f"""```py\n{message}```""")

    @Ghost.command(name="js", description="Send all your messages in a JavaScript code block.", usage="js [message]")
    async def js(ctx, *, message):
        await ctx.send(f"""```js\n{message}```""")
    @Ghost.command(name="lua", description="Send all your messages in a Lua code block.", usage="lua [message]")
    async def lua(ctx, *, message):
        await ctx.send(f"""```lua\n{message}```""")

    @Ghost.command(name="php", description="Send all your messages in a PHP code block.", usage="php [message]")
    async def php(ctx, *, message):
        await ctx.send(f"""```php\n{message}```""")

    @Ghost.command(name="html", description="Send all your messages in a HTML code block.", usage="html [message]")
    async def html(ctx, *, message):
        await ctx.send(f"""```html\n{message}```""")

    @Ghost.command(name="css", description="Send all your messages in a CSS code block.", usage="css [message]")
    async def css(ctx, *, message):
        await ctx.send(f"""```css\n{message}```""")

    @Ghost.command(name="yaml", description="Send all your messages in a YAML code block.", usage="yaml [message]")
    async def yaml(ctx, *, message):
        await ctx.send(f"""```yaml\n{message}```""")

    @Ghost.command(name="json", description="Send all your messages in a JSON code block.", usage="json [message]")
    async def _json(ctx, *, message):
        await ctx.send(f"""```json\n{message}```""")

    @Ghost.command(name="aesthetic", description="Send your text s p a c e d out.", usage="aesthetic [text]")
    async def aesthetic(ctx, *, text):
        message = text
        msg = ""
        for letter in list(message):
            msg += " " + letter +  " "
        await ctx.send(msg)

    @Ghost.command(name="animate", description="Animate your text.", usage="animate [text]")
    async def animate(ctx, *, text):
        output = ""
        text = list(text)
        msg = await ctx.send(text[0])
        for letter in text:
            output = output + letter + ""
            await msg.edit(content=output)
            await asyncio.sleep(1)

    @Ghost.command(name="chatbypass", description="Bypass chat language restrictions.", usage="chatbypass [text]", aliases=["bypasschat"])
    async def chatbypass(ctx, *, text):
        text = text.lower()

        regional_indicators = {
        'a': '𝚊',
        'b': '𝚋',
        'c': '𝚌',
        'd': '𝚍',
        'e': '𝚎',
        'f': '𝚏',
        'g': '𝚐',
        'h': '𝚑',
        'i': '𝚒',
        'j': '𝚓',
        'k': '𝚔',
        'l': '𝚕',
        'm': '𝚖',
        'n': '𝚗',
        'o': '𝚘',
        'p': '𝚙',
        'q': '𝚚',
        'r': '𝚛',
        's': '𝚜',
        't': '𝚝',
        'u': '𝚞',
        'v': '𝚟',
        'w': '𝚠',
        'x': '𝚡',
        'y': '𝚢',
        'z': '𝚣'
        }

        output = ""
        text = list(text)
        for letter in text:
            if letter in regional_indicators:
                output = output + regional_indicators[letter] + ""
            else:
                output = output + letter
        await ctx.send(output)

    @Ghost.command(name="regional", description="Replace all letters with emoji.", usage="regional [text]")
    async def regional(ctx, *, text):
        text = text.lower()

        regional_indicators = {
        'a': '<:regional_indicator_a:803940414524620800>',
        'b': '<:regional_indicator_b:803940414524620800>',
        'c': '<:regional_indicator_c:803940414524620800>',
        'd': '<:regional_indicator_d:803940414524620800>',
        'e': '<:regional_indicator_e:803940414524620800>',
        'f': '<:regional_indicator_f:803940414524620800>',
        'g': '<:regional_indicator_g:803940414524620800>',
        'h': '<:regional_indicator_h:803940414524620800>',
        'i': '<:regional_indicator_i:803940414524620800>',
        'j': '<:regional_indicator_j:803940414524620800>',
        'k': '<:regional_indicator_k:803940414524620800>',
        'l': '<:regional_indicator_l:803940414524620800>',
        'm': '<:regional_indicator_m:803940414524620800>',
        'n': '<:regional_indicator_n:803940414524620800>',
        'o': '<:regional_indicator_o:803940414524620800>',
        'p': '<:regional_indicator_p:803940414524620800>',
        'q': '<:regional_indicator_q:803940414524620800>',
        'r': '<:regional_indicator_r:803940414524620800>',
        's': '<:regional_indicator_s:803940414524620800>',
        't': '<:regional_indicator_t:803940414524620800>',
        'u': '<:regional_indicator_u:803940414524620800>',
        'v': '<:regional_indicator_v:803940414524620800>',
        'w': '<:regional_indicator_w:803940414524620800>',
        'x': '<:regional_indicator_x:803940414524620800>',
        'y': '<:regional_indicator_y:803940414524620800>',
        'z': '<:regional_indicator_z:803940414524620800>'
        }

        output = ""
        text = list(text)
        for letter in text:
            if letter in regional_indicators:
                output = output + regional_indicators[letter] + " "
            else:
                output = output + letter
        await ctx.send(output)

    @Ghost.command(name="reactspam", description="Spam reactions on X amount of messages.", usage="reactspam [emoji] [messages]", aliases=["spamreactions", "spamreact"])
    async def reactspam(ctx, emoji, messages: int):
        if __riskmode__:
            #channel = Ghost.get_channel(ctx.channel.id)
            msgs = await ctx.channel.history(limit=messages).flatten()

            for msg in msgs:
                try:
                    await msg.add_reaction(emoji)
                except:
                    pass
        else:
            if __embedmode__:
                embed = discord.Embed(title=f"Abusive Commands", color=__embedcolour__, description=f"You have risk mode disabled, you cant use this command.")
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)      
            else:
                await ctx.send(f"""```ini
[ Abuse Commands ]

You have risk mode disabled, you cant use this command.


# {__embedfooter__}```""", delete_after=__deletetimeout__)                              

    @Ghost.command(name="uppercase", description="Send your message in uppercase.", usage="uppercase [msg]")
    async def uppercase(ctx, *, msg):
        string = msg.upper()
        await ctx.send(string)

    @Ghost.command(name="lowercase", description="Send your message in lowercase.", usage="lowercase [msg]")
    async def lowercase(ctx, *, msg):
        string = msg.lower()
        await ctx.send(string)

    @Ghost.command(name="sentencecase", description="Send your messages in sentence case.", usage="sentencecase [msg]")
    async def sentencecase(ctx, *, msg):
        sentenceList = msg.split(". ")
        sentenceList2 = []
        for string in sentenceList:
            string = string[:1].upper() + string[1:]
            sentenceList2.append(string)
        
        sentence = ". ".join(sentenceList2)
        await ctx.send(sentence)

    @Ghost.command(name="banlist", description="See the server's ban list.", usage="banlist")
    async def banlist(ctx):
        if ctx.author.guild_permissions.manage_guild:
            msg = ""
            banlist = await ctx.guild.bans()
            for ban in banlist:
                #username = user[0].name
                msg += f"{ban.user.name}#{ban.user.discriminator} ({ban.user.id})\n"
            if __embedmode__:
                embed = discord.Embed(title=ctx.guild.name + "'s banned member list", description=msg, color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send(f"""```ini
[ {ctx.guild.name}'s banned member list ]

{msg}


# {__embedfooter__}```""", delete_after=__deletetimeout__)

        else:
            if __embedmode__:
                embed = discord.Embed(title="You dont have the required permissions", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Invalid permissions.")

    @Ghost.command(name="ban", description="Ban the mentioned user.", usage="ban [@user]")
    async def ban(ctx, *, user: discord.Member):
        if ctx.author.guild_permissions.ban_members:
            await user.ban()
            if __embedmode__:
                embed = discord.Embed(title=user.name + " has been banned", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send(f"{user.name} has been banned")
        else:
            if __embedmode__:
                embed = discord.Embed(title="You dont have the required permissions", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Invalid permissions.")

    @Ghost.command(name="unban", description="Unban the mentioned id.", usage="unban [id]")
    async def unban(ctx, *, id: int):
        if ctx.author.guild_permissions.ban_members:
            user = await Ghost.fetch_user(id)
            await ctx.guild.unban(user)
            if __embedmode__:
                embed = discord.Embed(title=user.name + " has been unbanned", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send(f"{user.name} has been unbanned")
        else:
            if __embedmode__:
                embed = discord.Embed(title="You dont have the required permissions", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Invalid permissions.")

    @Ghost.command(name="kick", description="Kick the mentioned user.", usage="kick [@user]")
    async def kick(ctx, user: discord.Member):
        if ctx.author.guild_permissions.kick_members:
            await user.kick()
            if __embedmode__:
                embed = discord.Embed(title=user.name + " has been kicked", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send(f"{user.name} has been kicked")
        else:
            if __embedmode__:
                embed = discord.Embed(title="You dont have the required permissions", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Invalid permissions.")

    @Ghost.command(name="mute", description="Mute the menitioned user.", usage="mute [@user]")
    async def mute(ctx, user: discord.Member):
        if ctx.author.guild_permissions.mute_members:
            if get(ctx.guild.roles, name="Muted"):
                mutedrole = get(ctx.guild.roles, name="Muted")
            else:
                await ctx.guild.create_role(name="Muted")
                mutedrole = get(ctx.guild.roles, name="Muted")

            for channel in ctx.guild.channels:
                if channel.type == "Text":
                    await channel.set_permissions(mutedrole, send_messages=False)
                else:
                    await channel.set_permissions(mutedrole, send_messages=False, connect=False)
            await user.add_roles(mutedrole)

            if __embedmode__:
                embed = discord.Embed(title=user.name + " has been muted", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send(f"{user.name} has been muted")
        else:
            if __embedmode__:
                embed = discord.Embed(title="You dont have the required permissions", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Invalid permissions.")

    @Ghost.command(name="unmute", description="Unmute the mentioned user.", usage="unmute [@user]")
    async def unmute(ctx, user: discord.Member):
        if ctx.author.guild_permissions.mute_members:
            mutedrole = get(ctx.guild.roles, name="Muted")
            if mutedrole in user.roles:
                if __embedmode__:
                    await user.remove_roles(mutedrole)
                    embed = discord.Embed(title=user.name + " has been unmuted", color=__embedcolour__)
                    embed.set_thumbnail(url=__embedimage__)
                    embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                    embed.timestamp = datetime.now()
                    await ctx.send(embed=embed, delete_after=__deletetimeout__)
                else:
                    await ctx.send(f"{user.name} has been unmuted")
            else:
                if __embedmode__:
                    embed = discord.Embed(title=user.name + " is not muted", color=__embedcolour__)
                    embed.set_thumbnail(url=__embedimage__)
                    embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                    embed.timestamp = datetime.now()
                    await ctx.send(embed=embed, delete_after=__deletetimeout__)
                else:
                    await ctx.send(f"{user.name} is not muted")
        else:
            if __embedmode__:
                embed = discord.Embed(title="You dont have the required permissions", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Invalid permissions.")

    @Ghost.command(name="newrole", description="Create a new role.", usage="newrole [name]", aliases=["createrole"])
    async def newrole(ctx, *, name):
        if ctx.author.guild_permissions.manage_roles:
            await ctx.guild.create_role(name=name)
            if __embedmode__:
                embed = discord.Embed(title="@" + name + " has been created", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send(f"@{name} has been created")
        else:
            if __embedmode__:
                embed = discord.Embed(title="You dont have the required permissions", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Invalid permissions.")

    @Ghost.command(name="delrole", description="Delete the mentioned role.", usage="delrole [@role]", aliases=["deleterole"])
    async def delrole(ctx, *, role: discord.Role):
        if ctx.author.guild_permissions.manage_roles:
            await role.delete()
            if __embedmode__:
                embed = discord.Embed(title="@" + role.name + " has been deleted", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send(f"@{role.name} has been deleted")
        else:
            if __embedmode__:
                embed = discord.Embed(title="You dont have the required permissions", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Invalid permissions.")

    @Ghost.command(name="purge", description="Purge X amount of messages.", usage="purge [amount]")
    async def purge(ctx, amount: int):
        if ctx.author.guild_permissions.manage_messages:
            history = await ctx.channel.history(limit=amount).flatten()
            deletedamount = 0
            for message in history:
                try:
                    deletedamount+=1
                    await message.delete()
                    await asyncio.sleep(1)
                except:
                    pass
            if __embedmode__:
                embed = discord.Embed(title=f"Deleted {deletedamount} messages", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send(f"Deleted {deletedamount} messages")
        else:
            if __embedmode__:
                embed = discord.Embed(title="You dont have the required permissions", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Invalid permissions.")

    @Ghost.command(name="purgeself", description="Purge your messages.", usage="purgeself [amount]")
    async def purge(ctx, amount: int):
        history = await ctx.channel.history(limit=amount).flatten()
        deletedamount = 0
        for message in history:
            if message.author.id == Ghost.user.id:
                try:
                    deletedamount+=1
                    await message.delete()
                    await asyncio.sleep(1)
                except:
                    pass
        if __embedmode__:
            embed = discord.Embed(title=f"Deleted {deletedamount} messages", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send(f"Deleted {deletedamount} messages")                       

    @Ghost.command(name="lock", description="Lock the command channel.", usage="lock")
    async def lock(ctx):
        if ctx.author.guild_permissions.manage_channels:
            await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=False)
            if __embedmode__:
                embed = discord.Embed(title=f"Channel Locked", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Channel Locked")
        else:
            if __embedmode__:
                embed = discord.Embed(title="You dont have the required permissions", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Invalid permissions.")

    @Ghost.command(name="unlock", description="Unlock the command channel.", usage="unlock")
    async def unlock(ctx):
        if ctx.author.guild_permissions.manage_channels:
            await ctx.channel.set_permissions(ctx.guild.default_role, read_messages=True)
            if __embedmode__:
                embed = discord.Embed(title=f"Channel Unlocked", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Channel Unlocked")
        else:
            if __embedmode__:
                embed = discord.Embed(title="You dont have the required permissions", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Invalid permissions.")

    @Ghost.command(name="lockdown", description="Lock the entire server.", usage="lockdown")
    async def lockdown(ctx):
        if ctx.author.guild_permissions.manage_guild:
            for channel in ctx.guild.channels:
                await channel.set_permissions(ctx.guild.default_role, read_messages=False)
            channel = await ctx.guild.create_text_channel('lockdown-chat')
            if __embedmode__:
                embed = discord.Embed(title=f"Server Lockdown Enabled!", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await channel.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await channel.send("Server Lockdown Enabled!")
        else:
            if __embedmode__:
                embed = discord.Embed(title="You dont have the required permissions", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Invalid permissions.")

    @Ghost.command(name="unlockdown", description="Unlock the entire server.", usage="lockdown")
    async def unlockdown(ctx):
        if ctx.author.guild_permissions.manage_guild:
            for channel in ctx.guild.channels:
                await channel.set_permissions(ctx.guild.default_role, read_messages=True)
            if __embedmode__:
                embed = discord.Embed(title=f"Server Lockdown Disabled!", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Server Lockdown Disabled")
        else:
            if __embedmode__:
                embed = discord.Embed(title="You dont have the required permissions", color=__embedcolour__)
                embed.set_thumbnail(url=__embedimage__)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed, delete_after=__deletetimeout__)
            else:
                await ctx.send("Invalid permissions.")

    @Ghost.command(name="tokeninfo", description="Information about a token.", usage="tokeninfo [token]")
    async def tokeninfo(ctx, *, token):
        request = requests.get("https://discord.com/api/users/@me", headers={"Authorization": token})
        
        if request.status_code == 200:
            request = request.json()

            id = request["id"]
            username = request["username"]
            discriminator = request["discriminator"]
            avatar = avatarUrl(id, request["avatar"])
            publicflags = request["public_flags"]
            bio = request["bio"]
            nitro = ""
            if "premium_type" in request:
                if request["premium_type"] == 0:
                    nitro = "None"
                elif request["premium_type"] == 1:
                    nitro = "Classic Nitro"
                elif request["premium_type"] == 2:
                    nitro = "Nitro"
            else:
                nitro = "None"
            email = request["email"]
            phone = request["phone"]

            if bio == "":
                bio = " "

            if __embedmode__:
                embed = discord.Embed(title=user.name + " token information", color=__embedcolour__)
                embed.add_field(name="Token", value="```" + str(token) + "```", inline=False)
                embed.add_field(name="Username", value="```" + str(username) + "```")
                embed.add_field(name="Email", value="```" + str(email) + "```")
                embed.add_field(name="Phone", value="```" + str(phone) + "```")
                embed.add_field(name="Discriminator", value="```" + str(discriminator) + "```")
                embed.add_field(name="User ID", value="```" + str(id) + "```")
                embed.add_field(name="Bio", value="```" + str(bio) + "```")
                embed.add_field(name="Nitro", value="```" + str(nitro) + "```")
                embed.set_thumbnail(url=avatar)
                embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            else:
                createdAt = user.created_at.strftime("%d %B, %Y")
                await ctx.send(f"""```ini
[ {username}'s token Information ]

Token: {token}
Username: {username}
Email: {email}
Phone: {phone}
Discriminator: {discriminator}
User ID: {id}
Bio: {bio}
Nitro: {nitro}


# {__embedfooter__}```{avatar}""")  

        else:
            await ctx.send("Failed to get information about this token. Probably invalid or from a delete user.")                  

    @Ghost.command(name="userinfo", description="Information about the mentioned user.", usage="userinfo [@user]", aliases=["userlookup", "lookupuser"])
    async def userinfo(ctx, *, user: discord.User):
        if __embedmode__:
            embed = discord.Embed(title=user.name + " Information", color=__embedcolour__)
            embed.add_field(name="Username", value="```" + str(user.name) + "```")
            embed.add_field(name="Discriminator", value="```" + str(user.discriminator) + "```")
            embed.add_field(name="User ID", value="```" + str(user.id) + "```")
            embed.add_field(name="Created At", value="```" + str(user.created_at.strftime("%d %B, %Y")) + "```")
            embed.set_thumbnail(url=avatarUrl(user.id, user.avatar))
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            createdAt = user.created_at.strftime("%d %B, %Y")
            await ctx.send(f"""```ini
[ {user.name} Information ]

Username: {user.name}
Discriminator: {user.discriminator}
User ID: {user.id}
Created At: {createdAt}


# {__embedfooter__}```{avatarUrl(user.id, user.avatar)}""")

    @Ghost.command(name="serverinfo", description="Information about the command server.", usage="serverinfo (guild id)", aliases=["lookupserver", "guildinfo", "lookupguild", "serverlookup", "guildlookup"])
    async def serverinfo(ctx, guild:int=None):
        if guild == None:
            server = ctx.message.guild
        else:
            server = await Ghost.fetch_guild(int(guild))
        if __embedmode__:
            embed = discord.Embed(title=server.name + " Information", color=__embedcolour__)
            embed.add_field(name="Name", value="```" + str(server.name) + "```")
            embed.add_field(name="Owner", value="```" + str(server.owner) + "```")
            try:
                embed.add_field(name="Member Count", value="```" + str(server.member_count) + "```")
            except:
                pass
            embed.add_field(name="Server ID", value="```" + str(server.id) + "```")
            embed.add_field(name="Created At", value="```" + str(server.created_at.strftime("%d %B, %Y")) + "```")
            embed.set_thumbnail(url=str(server.icon))
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            createdAt = server.created_at.strftime("%d %B, %Y")
            try:
                await ctx.send(f"""```ini
[ {server.name} Information ]

Name: {server.name}
Owner: {server.owner}
Member Count: {server.member_count}
Server ID: {server.id}
Created At: {createdAt}


# {__embedfooter__}```{str(server.icon)}""")
            except:
                await ctx.send(f"""```ini
[ {server.name} Information ]

Name: {server.name}
Owner: {server.owner}
Server ID: {server.id}
Created At: {createdAt}


# {__embedfooter__}```{str(server.icon)}""")                        

    @Ghost.command(name="avatar", description="Get the mentioned user's avatar.", usage="avatar [@user]", aliases=["pfp", "profilepicture"])
    async def avatar(ctx, *, user: discord.User):
        if __embedmode__:
            embed = discord.Embed(title=user.name + "'s Avatar", color=__embedcolour__)#
            embed.set_image(url=avatarUrl(user.id, user.avatar))
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(avatarUrl(user.id, user.avatar))

    @Ghost.command(name="servericon", description="Get the server's icon.", usage="servericon", aliases=["guildicon"])
    async def servericon(ctx):
        if __embedmode__:
            embed = discord.Embed(title=ctx.guild.name + "'s Icon", color=__embedcolour__)
            embed.set_image(url=iconUrl(ctx.guild.id, ctx.guild.icon))
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        else:
            await ctx.send(iconUrl(ctx.guild.id, ctx.guild.icon))

    @Ghost.command(name="afkmode", description="Toggle afk mode.", usage="afkmode")
    async def afkmode(ctx):
        global afkMode
        afkMode = not afkMode
        cfg = Config.getConfig()
        cfg["afkmode"]["enabled"] = afkMode
        Config.saveConfig(cfg)
        if afkMode:
            await ctx.send("Afk mode has been enabled.")
        else:
            await ctx.send("Afk mode has been disabled.")

    @Ghost.command(name="settings", description="The bot's settings.", usage="settings")
    async def settings(ctx):
        totalguilds = len(Ghost.guilds)
        totalcommands = len(Ghost.commands) + len(ccmd)

        uptime = int(round(time.time() - botStartTime))
        uptimeText = str(timedelta(seconds=uptime))

        delta_uptime = datetime.now() - Ghost.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        logins = open('data/logins.txt', 'r')
        logindata = logins.read()
        base64_message = logindata
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        logindata_decoded = message_bytes.decode('ascii')

        if __embedmode__:
            embed = discord.Embed(title=f"Settings", color=__embedcolour__)
            embed.add_field(name="Commands", value=f"```{totalcommands}```")
            embed.add_field(name="Logins", value=f"```{logindata_decoded}```")
            embed.add_field(name="Version", value=f"```{version}```")
            embed.add_field(name="Prefix", value=f"```{Ghost.command_prefix}```")
            embed.add_field(name="UID", value=f"```{__uid__}```")
            embed.add_field(name="Servers", value=f"```{totalguilds}```")
            #embed.add_field(name="Uptime", value=f"```{days}d, {hours}h, {minutes}m, {seconds}s```")
            embed.add_field(name="Uptime", value=f"```{uptimeText}```")
            embed.add_field(name="Credits", value="""Thanks to all the below people for helping with some of Ghost's commands.
```
Imf44 : Fox command.
Qoft : Proxy related commands.
```
            """, inline=False)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send(f"""```ini
[ Settings ]

Commands: {totalcommands}
Logins: {logindata_decoded}
Version: {version}
Prefix: {Ghost.command_prefix}
UID: {__uid__}
Servers: {totalguilds}
Uptime: {days}d, {hours}h, {minutes}m, {seconds}s


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    '''@Ghost.command(name="snipers", description="All snipers.", usage="snipers")
    async def snipers(ctx):
        if __nitrosniper__ == True:
            nitro = "Enabled"
        else:
            nitro = "Disabled"
        if __privnotesniper__ == True:
            privnote = "Enabled"
        else:
            privnote = "Disabled"
        if __giveawaysniper__ == True:
            giveaway = "Enabled"
        else:
            giveaway = "Disabled"
        try:
            embed = discord.Embed(title=f"Snipers", color=__embedcolour__)
            embed.add_field(name="Nitro", value=f"```{nitro}```")
            embed.add_field(name="Privnote", value=f"```{privnote}```")
            embed.add_field(name="Giveaway", value=f"```{giveaway}```")
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        except discord.HTTPException:
            await ctx.send(f"""```ini
[ Snipers ]

Nitro: {nitro}
Privnote: {privnote}
Giveaway: {giveaway}


# {__embedfooter__}```""", delete_after=__deletetimeout__)'''

    @Ghost.command(name="playing", description="Set a playing status.", usage="playing [text]")
    async def playing(ctx, *, text):
        if requests.get("https://discord.com/api/users/@me/settings", headers={"Authorization": __token__}).status_code == 200:
            status = requests.get("https://discord.com/api/users/@me/settings", headers={"Authorization": __token__}).json()["status"]
        else:
            status = "online"                
        await Ghost.change_presence(activity=discord.Game(text), status=discord.Status.try_value(status))
        try:
            embed = discord.Embed(title=f"Playing Status", description=f"Status changed to: Playing {text}", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        except discord.HTTPException:
            await ctx.send(f"""```ini
[ Playing Status ]

Status changed to: Playing {text}


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="streaming", description="Set a streaming status.", usage="streaming [text]")
    async def streaming(ctx, url, *, text):
        if requests.get("https://discord.com/api/users/@me/settings", headers={"Authorization": __token__}).status_code == 200:
            status = requests.get("https://discord.com/api/users/@me/settings", headers={"Authorization": __token__}).json()["status"]
        else:
            status = "online"                  
        await Ghost.change_presence(activity=discord.Activity(type=1, name=f"{text}", url=f"{url}"), status=discord.Status.try_value(status))
        try:
            embed = discord.Embed(title=f"Streaming Status", description=f"Status changed to: Streaming {text}", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        except discord.HTTPException:
            await ctx.send(f"""```ini
[ Streaming Status ]

Status changed to: Streaming {text}


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="listening", description="Set a listening to status.", usage="listening [text]")
    async def listening(ctx, *, text):
        if requests.get("https://discord.com/api/users/@me/settings", headers={"Authorization": __token__}).status_code == 200:
            status = requests.get("https://discord.com/api/users/@me/settings", headers={"Authorization": __token__}).json()["status"]
        else:
            status = "online"                  
        await Ghost.change_presence(activity=discord.Activity(type=2, name=f"{text}"), status=discord.Status.try_value(status))
        try:
            embed = discord.Embed(title=f"Listening Status", description=f"Status changed to: Listening to {text}", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        except discord.HTTPException:
            await ctx.send(f"""```ini
[ Listening Status ]

Status changed to: Listening to {text}


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="watching", description="Set a watching status.", usage="watching [text]")
    async def watching(ctx, *, text):
        if requests.get("https://discord.com/api/users/@me/settings", headers={"Authorization": __token__}).status_code == 200:
            status = requests.get("https://discord.com/api/users/@me/settings", headers={"Authorization": __token__}).json()["status"]
        else:
            status = "online"                  
        await Ghost.change_presence(activity=discord.Activity(type=3, name=f"{text}"), status=discord.Status.try_value(status))
        try:
            embed = discord.Embed(title=f"Watching Status", description=f"Status changed to: Watching {text}", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        except discord.HTTPException:
            await ctx.send(f"""```ini
[ Watching Status ]

Status changed to: Watching {text}


# {__embedfooter__}```""", delete_after=__deletetimeout__)

    @Ghost.command(name="clearstatus", description="Clear your status.", usage="clearstatus")
    async def clearstatus(ctx):
        await Ghost.change_presence(activity=discord.Activity(type=-1), status=discord.Status.try_value(status))
        try:
            embed = discord.Embed(title=f"Status Cleared", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        except discord.HTTPException:
            await ctx.send("Status Cleared")

    @Ghost.command(name="nickname", description="Set your nickname to anything.", usage="nickname [text]")
    async def nickname(ctx, *, text):
        await ctx.author.edit(nick=nickname)
        if __embedmode__:
            embed = discord.Embed(title=f"Nickname changed to {text}", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send(f"Nickname changed to {text}")
    print(fg.cWhite + "")

    @Ghost.command(name="clearnickname", description="Clear your nickname.", usage="clearnickname")
    async def clearnickname(ctx):
        await ctx.author.edit(nick="")
        if __embedmode__:
            embed = discord.Embed(title=f"Nickname cleared", color=__embedcolour__)
            embed.set_thumbnail(url=__embedimage__)
            embed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed, delete_after=__deletetimeout__)
        else:
            await ctx.send("Nickname cleared")

    Ghost.run(__token__)

    # GhostDiscum = discum.Client(token=__token__, log=False, user_agent=get_random_user_agent())

    # @GhostDiscum.gateway.command
    # def discumevents(resp):
    #     if resp.event.typing:
    #         rawevent = resp.raw
    #         parsedevent = resp.parsed.auto()
    #         print(rawevent)

    # GhostDiscum.gateway.run()

except Exception as e:
    if "improper token" in str(e).lower():
        print("The Discord token that Ghost has been given to use is no longer working or is invalid.")
        print("Please put a new token in to the config (config.json).")
    else:
        print(e)
    logging.exception(str(e))
    if os.name == "nt":
        os.system("pause")
    if os.name == "posix":
        input("Press enter to close . . .")
