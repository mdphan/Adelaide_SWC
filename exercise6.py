#Exercise 6:
#1) Read the contents of the file pg76.txt
#2) get the length of each line and sum the lines as you go
#3) count the total number of lines in the file

text_file = open('pg76.txt', 'r')
line = 'a'
length = 0
line_number = -1

while line != '':
    line = text_file.readline()
    length += len(line) 
    line_number += 1
text_file.close()

#print "Total length: " + str(length)
#print "Line count: " + str(line_number)

print 'Total length: %d, line count: %d' % (length, line_number)
