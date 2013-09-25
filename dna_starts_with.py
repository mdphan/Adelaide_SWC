# Test dna_starts_with
#
#def dna_starts_with(string, prefix):
#    i = 0
#    correct = 0
#    for base in prefix:
#        if base == string[i]:
#            correct += 1
#        i += 1
#    if correct == len(prefix):
#        print "True"
#    else:
#        print "False"
#
#dna_starts_with("ATGCCC", "TGC")

def dna_starts_with(string, prefix):
    return string[0:len(prefix)]==prefix    

Tests = [
            ['at','a',True],
            ['tag','ta',True],
            ['ctg','t',False]
        ]

for (i, (seq, prefix, expected)) in enumerate(test):
    if dna_stars_with(seq,prefix) == expected:
        
    


