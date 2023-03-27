import subprocess
online_loader = []

loader=["127.0.0.1","10.10.10.33","10.10.10.45"]
address = "124.0.2.2"
dest="Destination net unreachable"
dest2="Destination host unreachable"
rto="Request timed out"
for i in loader:
	res = subprocess.run(['ping', '-n','2','-w','100', i], capture_output=True)
	args=""+str(res)

	if dest in args:
		print('ping failed')
	elif rto in args:
		print('ping failed')
	elif dest2 in args:
		print('ping failed')
	else:
		print('ping ok')
		print(res)
		online_loader.append(i)
	

	
#return online_loader	

