#Exercise 7

input = open('Pitching.csv','r')
line = input.readline()
sum = 0
avg = 0
count = 0

while line != '':
    line = input.readline()
    list = line.split(',')
    value = list[12]
    sum += float(value)
    count += 1
input.close()

print float(sum/count)
