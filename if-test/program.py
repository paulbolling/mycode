#!/user/bin/var python3
#make it work

while(True) :
	print('What is your L2 protocol')
	L2proto = input()
	if  L2proto == 'eth': 
		print('ethernet protocol allowed') 
		break
	elif L2proto == 'fc':
		print('fiber channel NOT allowed')
	elif L2proto == 'ifb':
		print('infiniband NOT allowed')
	elif L2proto == 'otn':
		print('Optical Network allowed')
		break
	else:
		print('No idea what that technology is')