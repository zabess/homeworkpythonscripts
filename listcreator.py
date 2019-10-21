# ! /usr/bin/env python

listofnumbers = ['22', '26', '92', '88', '54', '46']
#Begin with a specified list of numbers
newlist =  list()
#Creates an empty list where the new numbers will be stored
for number in listofnumbers:
#loops through each number in the list
	newnumber = int(number) + 1
#adds 1 to each of the numbers in the list
	newlist.append(newnumber)
#appends each additional new number to the previously empty list
print("Original list: ", listofnumbers)
print("New list: ", newlist)
#prints the original and newly generated list
