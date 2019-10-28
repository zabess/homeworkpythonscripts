#! /usr/bin/env python
#This script reads in the Bloom_etal_2018_Reduced_Dataset displays the Taxa Name,
#the diadromous status of the particular taxa, and it calculates the sum
#of the log body sizes.
InFile = open("Bloom_etal_2018_Reduced_Dataset.csv", 'r')
#Read in the dataset.
LineNumber = 0
#Establish LineNumber as 0.
tobesummed = []
diadromoustally = []
nondiadromoustally = []
#Initialize empty list.
for Line in InFile:
#Use a loop to strip the end-of-line break, splits the lines in the csv by commas,
#print the taxa and its diadromous status and calculates the sum of all of the log body masses.
	if LineNumber > 1:
		Line = Line.strip('\n')
		ElementList = Line.split(',')
		print("Taxa: %s \t Status: %s" %(ElementList[0], ElementList[3]))
		tobesummed.append(float(ElementList[1]))
		if ElementList[3] == 'diadromous':
			diadromoustally.append(1)
		if ElementList[3] == 'non-diadromous':
			nondiadromoustally.append(1)
	LineNumber = LineNumber + 1
total = sum(tobesummed)
print("Sum of all log body sizes: %s" %(total))
#Prints the total log body size.
totaldiadromous = sum(diadromoustally)
print("Count of Diadromous species: %s" %(totaldiadromous))
totalnondiadromous = sum(nondiadromoustally)
print("Count of Non-Diadromous species: %s" %(totalnondiadromous))
InFile.close()
