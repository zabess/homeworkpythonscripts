#! /usr/bin/env python
sentence = input("Enter a sentence and this script will count the number of non-space characters:")
#Above line prompts the user to enter a sentence
sentence = sentence.lower().replace(" ","")
#Above line converts sentence by removing spaces and turning all characters into lower-case letters.
length = len(sentence)
#Above line calculates the length of the sentence (not including spaces)>
print("Length of sentence:", length)
#Above line returns the length
