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
	print i
	j = 9
	for Question in QuestionList:
		OutputFile.write("\n<h3>")
		OutputFile.write(Question)
		OutputFile.write(" </h3>\n\n<p><strong>")
		OutputFile.write(name)
		OutputFile.write("</strong> </p>\n")
		OutputFile.write(row[j])
		OutputFile.write("\n\n")
		j = j+1

	OutputFile.close()
	i = i+1

f.close()