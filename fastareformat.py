#! /usr/bin/env python
#This file reformats the structure of the regex.practice1.fasta file so that
#the name rows are replaced with 'Homo_sapens' followed by the numeric string.

"""Pseudocode:
Import the re module

Open the regex.practice1.fasta file and store it as ‘InFile’
Establish initial line number as 1.
Use a for loop to move through each line in InFile.
	If line number is an even number (protein sequence):
		Strip the end-of-line break
		Print the line
	If line number is an odd number (name row):
		Search the for the following regular expression: ‘^>(\d+_\d+:\d+\S+) {.+}’
		Store the search result
		Print “>Homo_sapens:” followed by the search result
	Reset the line number to the next line."""


import re
#Import re module for working with regular expressions
InFile = open('C:\\Users\\Owner\\Desktop\\scripts\\regex.practice1.fasta', 'r')
#Bring in regex.practice1.fasta file.
LineNumber = 1
#Establish initial LineNumber as 1.
for Line in InFile:
	if (LineNumber % 2) == 0:
	# if the line number is an even number,
		Line = Line.strip('\n')
	#remove the end-of-line break
		print(Line)
	#print the line
	else:
		#if the line number is an odd number,
		SearchStr = '^>(\d+_\d+:\d+\S+) {.+}'
		#search for this particular regular expression
		Result = re.search(SearchStr, Line)
		#store the result of the search
		print(">Homo_sapens:%s" % (Result.group(1)))
		#print the ">Homo_sapens: " followed by the search result
	LineNumber = LineNumber + 1
	#move to the next line and repeat the loop
