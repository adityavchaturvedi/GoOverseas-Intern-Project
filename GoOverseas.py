#! /usr/bin/env python

import csv

person = raw_input('Your name please: ')
print("Hi " + person + ",\n\nThis the program speaking.\n\nBelow type 1 if you want only your interviews to be converted\nand type 2 if you want all interviews converted.")
print("\nBefore you proceed please make sure the file name for the data file is \"RawFile.csv\"")
choice = raw_input("\nYour choice: ")
RawCsvFile = open('RawFile.csv')

FormattedCsvFile = csv.reader(RawCsvFile)

QuestionList = []
QuestionList.append("Why did you pick this program?")
QuestionList.append("What do you wish someone had told you before you went abroad?")
QuestionList.append("What is the most important thing you learned abroad?")
QuestionList.append("What do you tell your friends who are thinking about going abroad?")
QuestionList.append("What was the hardest part about going abroad?")
QuestionList.append("What's your favorite story to tell about your time abroad?")
QuestionList.append("What made this experience unique and special?")
QuestionList.append("Tell us about an experience you had that you could not have had at home.")
QuestionList.append("What is one piece of advice you'd give to someone going on your program?")
QuestionList.append("What made this trip meaningful to you, or how did this trip change your perceptions or future path?")
QuestionList.append("Write and answer your own question!")

i = 1
for row in FormattedCsvFile:
	if choice=='1':
		if row[0]!=person:
			continue;
	#print("1-It reaches here.")
	name = row[6]
	nam = str(i) + name + ".txt"
	OutputFile = open(nam, "w")
	j = 11
	OutputFile.write(row[1])
	OutputFile.write("\n\n")
	OutputFile.write(row[6])
	OutputFile.write("\n\n")
	OutputFile.write(row[9])
	OutputFile.write("\n\n")
	OutputFile.write(row[10])
	OutputFile.write("\n\n")
	#name = name[0]
	for Question in QuestionList:
		if row[j]=="":
			j = j + 1
		else:
			OutputFile.write("\n<h3>")
			OutputFile.write(Question)
			OutputFile.write(" </h3>\n\n")
			rowsplit = row[j].split('\n')
			for k in rowsplit:
				if k!='':
					OutputFile.write("<p>")
					OutputFile.write(k)
					OutputFile.write("</p>\n\n")
			j = j+1

	OutputFile.close()
	i = i+1

RawCsvFile.close()