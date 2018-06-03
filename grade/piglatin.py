#!/usr/bin/env python3

#Made by Paul Bolling


def  piglat(word):
    first_letter = word[0]
    
    #check if word starts with a vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
        
    return pig_word

print('Enter word to translate to Pig Latin :')
word = input()

print('That is ' + piglat(word) + ' in Pig Latin')

############working on getting to be interactive on the command line##########


