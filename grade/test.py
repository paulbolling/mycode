#!/usr/bin/env python3

sentence = input("Enter a sentence you want to convert to pig latin: ")

sentence = sentence.split()
for i in range(len(sentence)):
    if sentence[i][0] in "aeiou":
        sentence[i] += 'yay'
    else:
        sentence[i]=sentence[i][1:]+sentence[i][0]
        sentence[i]+='ay'
sentence = ' '.join(sentence)

print(sentence)