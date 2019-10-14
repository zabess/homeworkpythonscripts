#! /usr/bin/env python
#Shebang established in above line
number = input("Enter a number of any length: ")
#Above line asks for a number of infinite length
numbertosearch = input("For which digit (0-9) would you like to count the number of occurrences?")
#Above line asks the user to specify which digit they want counted
Number2 = number.count(numbertosearch)
#Counts the number of specified digit
print("# of %s's: %d" % (numbertosearch, Number2))
#Returns the number of specified digit
