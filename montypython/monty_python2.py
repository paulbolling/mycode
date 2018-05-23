#!/usr/bin/env python3
round = 0
while(True):
	round = round + 1
	print('Finish the movie title, "Monty Python\'s The Life____"')
	answer = input()
	if answer.lower() == 'brian':
		print('Correct')
		break
	elif(round==3):
		print('Sorry the answer was Brain')
		break
	else:	
		print('Sorry! Try agian!')
