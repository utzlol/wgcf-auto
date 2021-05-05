import requests, eventlet, subprocess, time

a = 0
f = 0



while f == 0: 
	subprocess.call(['bash','fast'])
	time.sleep(2)
	with eventlet.Timeout(1):
		try:
			check =	requests.get('https://www.google.com')
			a = 1		
		except:
			print('No Internet')

	if a == 1:
		if check.status_code == 200:
			print('Connection OK')
			f = 1
		else:
			print('The Internet is Bad')
