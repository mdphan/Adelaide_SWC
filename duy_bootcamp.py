import sys

# Get the list of arguments but not the first element
my_arguments = sys.argv[1:]

# sort the list
my_arguments.sort()

# join the list into a string except the last element of the list
combined_words = ', '.join(my_arguments[0:-1])

print combined_words

# add 'and' last element and '.'
combined_words += ', and ' + my_arguments[-1] + '.'

print combined_words.capitalize()




