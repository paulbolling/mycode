#!/usr/bin/env python3

#Made by Paul Bolling


def  piglat(word):										#function
    first_letter = word.lower()[0]
    
    												#check if word starts with a vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:											#if not a vowel add the first letter to the end and add ay
        pig_word = word[1:] + first_letter + 'ay'
        
    return pig_word

print('Enter a word to translate to Pig Latin :')
word = input()             									#ask for a word
print('That is ' + piglat(word) + ' in Pig Latin') 						#output translated word

############working on getting more words as input##########


