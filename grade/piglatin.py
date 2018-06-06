#!/usr/bin/env python3

#Made by Paul Bolling

#This is a super high speed low drag translator for the very complex lost language of Pig Latin
import os
os.system('cls' if os.name == 'nt' else 'clear')						#Clears screen. I got the code from Google

def  piglat(word):										#Function
    first_letter = word.lower()[0]
    
    												#Check if word starts with a vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:											#If not a vowel add the first letter to the end and add ay
        pig_word = word[1:] + first_letter + 'ay'
        
    return pig_word

pig_word_list = []				

print('Enter a word to translate to Pig Latin :')
word = input()             									#Ask for a word
word_list = word.split()

for x in word_list:
    pig_word_list.append(piglat(x))

pig_latin = " ".join(pig_word_list)
print('That is ' + pig_latin + ' in Pig Latin') 
f = open('output.txt','a')									#Output translated word

############working on getting more words as input##########