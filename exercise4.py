#exercise 4

import sys
number = int(sys.argv[1])

if number % 2 == 0:
    print "Number is even."
elif number % 2 == 1:
    print "Number is odd."

if number > 0 and number <= 50:
    print "Minor"
elif number >50 and number <= 100:
    print "Major"
elif number > 100:
    print "Severe"
else:
    print "Negative"

