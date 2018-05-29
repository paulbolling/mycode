#!/usr/bin/env python3
round = 0
while(True): 									#Question 1
	round = round + 1
	print('How many people are in this class?')
	answer = input()
	if answer.lower() == '13':
		print('Correct')
		break
	if answer.lower() =='14':
		print('Remember Mahad is not here anymore')
	
	elif(round==6):
		print('Sorry the answer was 13. If all else fails you can just count.')
		break
	else:	
		print('Try agian?')

round = 0
while(True):									#Question 2
	round = round + 1
	print('Do you like this classroom? yes or no')
	answer = input()
	if answer.lower() == 'yes':
		print('That is good to hear.')
		break
	elif(round==3):
		print('You had a 50/50 chance if getting it right!!')
		break
	else:	
		print('The room is bugged...try agian')
round = 0
while(True):									#Question 3
	round = round + 1
	print('What time does class start? __am')
	answer = input()
	if answer.lower() == '8':
		print('Five days a week, well four days this week.')
		break
	elif(round==3):
		print('Look at the board')
		break
	else:	
		print('Try agian')