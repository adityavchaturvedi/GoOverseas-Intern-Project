#! /usr/bin/env python

import csv

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

i = 0
for row in FormattedCsvFile:
	name = row[5]
	nam = str(i) + name + ".txt"
	OutputFile = open(nam, "w")
	j = 10
	OutputFile.write(row[0])
	OutputFile.write("\n\n")
	OutputFile.write(row[5])
	OutputFile.write("\n\n")
	OutputFile.write(row[8])
	OutputFile.write("\n\nBio:\n")
	OutputFile.write(row[9])
	OutputFile.write("\n\n")
	#name = name[0]
	name = name.split()[0]
	for Question in QuestionList:
		if row[j]=="":
			j = j + 1
		else:
			OutputFile.write("\n<h3>")
			OutputFile.write(Question)
			OutputFile.write(" </h3>\n\n<p><strong>")
			OutputFile.write(name)
			OutputFile.write(": </strong>")
			OutputFile.write(row[j])
			OutputFile.write("</p>\n")
			OutputFile.write("\n\n")
			j = j+1

	OutputFile.close()
	i = i+1

RawCsvFile.close()