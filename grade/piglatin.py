#!/usr/bin/env python3

#Made by Paul Bolling

#This is a super high speed low drag translator for the very complex lost language of Pig Latin

def  piglat(word):										#Function
    first_letter = word.lower()[0]
    
    												#Check if word starts with a vowel
    if first_letter in 'aeiou':
        pig_word = word + 'AY'
    else:											#If not a vowel add the first letter to the end and add ay
        pig_word = word[1:] + first_letter.upper() + 'AY'
        
    return pig_word

import os
os.system('cls' if os.name == 'nt' else 'clear')						#Clears screen. I got the code from Google

print('Enter a word to translate to Pig Latin :')
word = input()             									#Ask for a word

print('That is ' + piglat(word.upper()) + ' in Pig Latin') 					#Output translated word

############working on getting more words as input##########


