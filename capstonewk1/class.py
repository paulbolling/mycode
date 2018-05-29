#!/usr/bin/env python3

#Paul Bolling

round = 0
while(True): 									#Question 1
	round = round + 1
	print('How many people are in this class?')
	answer = int(input())
	if answer == int('13'):
		print('		Correct		')
		print()
		break
	elif answer < int('13'):
		print('		Who did you forget?		')
		print()
	elif answer ==int('14'):
		print('		Remember Mahad is not here anymore.		')
		print()
	elif answer > int('14'):
		print('		Are you sure? That seems a bit high.		')
		print()
	elif(round==5):
		print('		Sorry the answer was 13. If all else fails you can just count.')
		print()
		break
	else:	
		print('Try agian?')
		print()

round = 0
while(True):									#Question 2
	round = round + 1
	print('Do you like this classroom? Yes or No')
	answer = input()
	if answer.lower() == 'yes':
		print('		That is what TLG likes to hear.')
		print()
		break
	elif(round==3):
		print('		You had a 50/50 chance if getting it right!!')
		print()
		break
	else:	
		print('		The room maybe bugged...try agian')
		print()
round = 0
while(True):									#Question 3
	round = round + 1
	print('What time does class start? __am')
	answer = int(input())
	if answer == int('8'):
		print('		Five days a week, well four days this week.')
		print()
		break
	
	elif answer > int('8'):
		print('		As great as it would be, it is still not the right answer.')
		print()
	elif answer < int('8'):
		print('		That is way too early. Have fun alone.')
		print()

	elif(round==3):
		print('		Look at the board')
		print()
		break
	else:	
		print('		Try agian')
		print()