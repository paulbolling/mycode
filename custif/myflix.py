#!/usr/bin/env python3
message = 'The movie is about to begin, we recommend '
print('Pick a number between 1 and 100')
connection = float(input())
if connection <= 100:
    message = message + 'Way to go!! Aim for the stars.'
elif connection <= 75:
    message = message + 'You\'re getting there.'
elif connection >= 50:
    message = message + 'It is a bit low for a guess.'
else:
    message = message + 'OK....'
print(message)