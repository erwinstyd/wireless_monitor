import subprocess
online_loader = []
def check_online_loaders():
	loader=["10.10.10.66","10.10.10.30","127.0.0.1"]
	address = "124.0.2.2"
	
	for i in loader:
		res = subprocess.call(['ping', '-n','1', i])
		if res == 0:
			print("ping ok", res)
			online_loader.append(i)
		elif res == 2:
			print("no response", res)
		else:
			print("ping failed", res)
		res=1
	return online_loader	

