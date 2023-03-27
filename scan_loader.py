import subprocess
online_loader = []
def check_online_loaders():
	loader=["10.10.10.38","10.10.10.33","10.10.10.18","10.10.10.29","10.10.10.52","10.10.10.59","10.10.10.60","10.10.10.58","10.10.10.66","10.10.10.103","10.10.10.57","10.10.10.102","10.10.10.194","10.10.10.193","10.10.10.65"]
	address = "124.0.2.2"
	dest="Destination net unreachable"
	dest2="Destination host unreachable"
	rto="Request timed out"
	for i in loader:
		res = subprocess.run(['ping', '-n','2','-w','30', i], capture_output=True)
		args=""+str(res)

		if dest in args:
			print('ping failed')
		elif rto in args:
			print('ping failed')
		elif dest2 in args:
			print('ping failed')
		else:
			print('ping ok')
			online_loader.append(i)

	
	return online_loader	

