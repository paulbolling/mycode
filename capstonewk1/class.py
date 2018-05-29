#!/usr/bin/env python3

#Paul Bolling

round = 0
while(True): 									#Question 1
	round = round + 1
	print('How many people are in this class?')
	answer = int(input())
	if(round==5):
		print('		Sorry the answer was 13. If all else fails you can just count.')
		print()
		quit()	
	elif answer == float('13'):
		print('		Correct		')
		print()
		break
	elif answer < float('13'):
		print('		Who did you forget?		')
		print()
	elif answer ==float('14'):
		print('		Remember Mahad is not here anymore.		')
		print()
	elif answer > float('14'):
		print('		Are you sure? That seems a bit high.		')
		print()
	
	else:	
		print('Try agian?')
		print()

round = 0
while(True):									#Question 2
	round = round + 1
	print('Do you like this classroom? Yes or No')
	answer = input()
	if answer.lower() == 'yes':
		print('		That\'s what TLG likes to hear.')
		print()
		break
	elif(round==2):
		print('		You had a 50/50 chance if getting it right!!')
		print()
		quit
	else:	
		print('		The room maybe bugged...try agian')
		print()
round = 0
while(True):									#Question 3
	round = round + 1
	print('What time does class start? __am')
	answer = int(input())
	if answer == int('8'):
		print('		5 days a week, well 4 days this week.')
		print()
		break
	
	elif answer > int('8'):
		print('		It would be GREAT, but still not the right answer.')
		print()
	elif answer < int('8'):
		print('		That is way too early. Have fun alone.')
		print()

	elif(round==3):
		print('		Look at the board')
		print()
		quit
	else:	
		print('		Try agian')
		print()