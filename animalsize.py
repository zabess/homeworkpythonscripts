# ! usr/bin/env python
#This script takes a dictionary of animals and their weights, converts to a list, and then prints if the  animal is 'small' or big' if mass is larger than 20.
dictofanimals = {}
#Create dictionary
dictofanimals['python'] = 500
dictofanimals['dog'] = 35000
dictofanimals['hamster'] = 25
dictofanimals['gerbil'] = 15
dictofanimals['praying_mantis'] = 0.5
dictofanimals['mouse'] = 5
#Add dictionary keys and their associative values
print(dictofanimals.keys())
#Print keys of dictionary
animallist = dictofanimals.keys()
#Store keys as a list item
for animal in animallist:
#for loop that loops through each animals
	if dictofanimals[animal] > 20:
		print("%s: big" %(animal))
	#print the animal's name and 'big' if it is larger than 20
	else:
	#print the animal's name and small if it is not larger than 20
		print("%s: small" %(animal))
