#! /usr/bin/env python

#This script accepts an existing file containing fluorometry data
#and the calibration parameters, and outputs a file that contains the original
#fluorometry data, the calculated chlorophyll and pheophytin concentrations.
#For samples that are duplicates, the relative percent difference.
#It displays these calculations to the command line interface
#and writes them to the output file.

rlow = input("Enter rlow value:") #2.491
rmed = input("Enter rmed value:") #2.417
rhigh = input("Enter rhigh value:") #2.448
fslow = input("Enter fslow value:") #0.995
fsmed = input("Enter fsmed value:") #0.988
fshigh = input("Enter fshigh value:") #0.984
#Inputs prompt the user to enter the values determined during the
#calibration process (rlow, rmed, rhigh, fslow, fsmed, and fshigh).
InFileName = input("Enter file name & extension for raw data:")
OutFileName = input("Enter file name & extension for raw data:")
InFile = open(InFileName, 'r')
OutFile = open(OutFileName, 'w')
#This specifies the files that the results will be written to as well as
#where the initial data will be drawn from.
samplenames = []
#Initializes a list for storing sample names.
originalfile = []
#Initializes a list for storing each for of InFile as a list element.
LineNumber = 1
#Establishes intial LineNumber as 1. This will serve as a counter for the
#loop. LineNumber for the header row will be 1.
for Row in InFile:
	#For each row of the incoming file:
	ChlorophyllA = None
	#Initializes an empty variable for storing the chlorophyll calculation
	#for each loop iteration.
	Pheophytin = None
	#Initializes an empty variable for storing the chlorophyll calculation
	#for each loop iteration.
	Row = Row.strip("\n")
	#Strips the end-of-line break from each row that is read in through
	#each loop iteration.
	Row = Row.split(",")
	#Splits each incoming row into list elements separated by a comma.
	if LineNumber == 1:
		#For the header row:
		Row.extend(('ChlorophyllA', 'Pheophytin', 'Relative%Difference'))
		#Append the header titles to the header row.
	if LineNumber > 1:
		#For all subsequent rows after the header:
		originalfile.append(Row)
		#Store the contents of the row into the originalfile list.
		#Therefore, the first row of the file (not including the
		#header) will be the 0th element of the originalfile list.
		if Row[4] == 'high':
		#If the chlorophyll reading range is "high"
		#(as denoted in the fifth column of the incoming file):
			ChlorophyllA = float(fshigh)*(float(rhigh)/(float(rhigh)-1))*(float(Row[3])-float(Row[5]))*(float(Row[2])/float(Row[1]))*float(Row[7])
			#Use the fshigh and rhigh values to calculate
			#the chlorophyll concentration with the above
			#formula.
		elif Row[4] == "med":
		#If the range is medium:
			ChlorophyllA = float(fsmed)*(float(rmed)/(float(rmed)-1))*(float(Row[3])-float(Row[5]))*(float(Row[2])/float(Row[1]))*float(Row[7])
			#Use the fsmed and rmed values to calculate the
			#chlorophyll concentration with the above formula.
		elif Row[4] == "low":
		#If the range is low:
			ChlorophyllA = float(fslow)*(float(rlow)/(float(rlow)-1))*(float(Row[3])-float(Row[5]))*(float(Row[2])/float(Row[1]))*float(Row[7])
			#Use the fslow and rlow values to calculate the
			#chlorophyll concentration with the above formula.
		else:
		#If the range is not reported:
			pass
			#Don't calculate the chlorophyll concentration.
		if Row[6] == "high":
		#If the pheophytin reading range is "high" (as indicated
		#in column 7 of the incoming file):
			Pheophytin = float(fshigh)*(float(rhigh)/(float(rhigh)-1))*((float(rhigh)*float(Row[5]))-float(Row[3]))*(float(Row[2])/float(Row[1]))*float(Row[7])
			#Calculate the pheophytin concentration with the
			#fshigh and rhigh values in the above formula.
		elif Row[6] == "med":
		#If the pheophytin reading range is medium:
			Pheophytin = float(fsmed)*(float(rmed)/(float(rmed)-1))*((float(rmed)*float(Row[5]))-float(Row[3]))*(float(Row[2])/float(Row[1]))*float(Row[7])
			#Calculate the pheophytin concentration with the
			#fsmed and rmed values in the above formula.
		elif Row[6] == "low":
		#If the pheophytin reading range is low:
			Pheophytin = float(fslow)*(float(rlow)/(float(rlow)-1))*((float(rlow)*float(Row[5]))-float(Row[3]))*(float(Row[2])/float(Row[1]))*float(Row[7])
			#Calculate the pheophytin concentration with the
			#fslow and rlow values in the above formula.
		else:
		#If the pheophytin reading range is not reported:
			pass
			#Don't calculate the chlorophyll concentration.
		Row.extend((str(ChlorophyllA), str(Pheophytin)))
		#Add the calculated chlorophyll-a and pheophytin
		#concentrations to the row list.
		if Row [8] == "yes":
		#If the sample is a duplicate (as indicated in column
		#9 of the incoming file):
			previousrow = originalfile[samplenames.index(Row[0])]
			#Search the samplenames list for a sample that has a name
			#identical to the name of the sample currently being iterated
			#through the loop, and retrieve the original sample's entire
			#row from the originalfile list and store it as a new list
			#called "precedingrow".
			percentdiff = abs(float(Row[3])-float(previousrow[3]))/((float(Row[3])+float(previousrow[3]))/2)*100
			#Calculate the relative percent differences from the fluorometer readings on unacidified samples using
			#the information from the duplicate samples.
			#Print the names of samples for which there are duplicates as well
			#as their respective calculated relative percent differences.
			Row.append(str(percentdiff))
			#Append the relative % difference to the row.
		samplenames.append(Row[0])
		#Now that the loop is finished for this particular iteration, append
		#the name of the sample to this particular row.
		#OutFile.write(','.join(Row) + "\n")
		#Write the row to the output file and join the list elements as
		#string elements separated by commas.
	outputRow = ','.join(Row)
	#Convert the row list to a string.
	print(outputRow)
	#Print the row to the screen.
	OutFile.write(outputRow + "\n")
	#Print the row to the output file.
	LineNumber = LineNumber + 1
	#Adjust the "LineNumber" counter that is used in the loop.
InFile.close()
#Close the incoming file.
OutFile.close()
#Close the outgoing file.
