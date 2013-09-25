#Exercise 2:
#given a string (a sentence), find out how many
#unique letters A-Z it contains - capital and
#lower case shouldn't be double-counted
#'AaAa'
#input: some string
#input_string = 'some string here'
#print (the number of unique letters in the string)

string = raw_input('Enter a string: ')

my_set = set(string.lower())

all_letters = set('abcdefghijklmnopqrstuvwxzy')

letters = my_set.intersection(all_letters)

#print my_set

print 'The number of unique letters in the string: ' + str(len(letters))


#extra credit:
#given two sentences, find the # of letters they have in common, and
#the number of letters that are unique to each

sentence1 = raw_input('Enter sentence 1: ')
sentence2 = raw_input('Enter sentence 2: ')

set1 = set(sentence1.upper())
set2 = set(sentence2.upper())

set1 = set1.intersectional(all_letters)
set2 = set2.intersectional(all_letters)

common = set1.intersection(set2)

print 'The number of common letters: ' + str(len(common))


print 'The number of unique letters: ' + str(len(unique))



