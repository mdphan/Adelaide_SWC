Tests = [
            ['ACGTGT', {'A':1, 'C':1, 'G':2, 'T':2}],
            ['CAGGTT', {'A':1, 'C':1, 'G':2, 'T':2}],
            ['acgtgt', {'A':1, 'C':1, 'G':2, 'T':2}],

        ]

def nucleotideContent(dnaString):    
    '''This function must return the contribution    
    of nucleotides ATCG (as uppercase) from a given DNA     
    string inside a dictionary, where each key refers to    
    a nucleotide    
    '''    
    dnaDict = {}    
    uniques=set(dnaString.upper())    
    for nucleotide in uniques:    
        dnaDict[nucleotide]=dnaString.count(nucleotide)    
    
    return dnaDict

# Run and report    
passes = 0    
for (i, (dnaString, dnaDict)) in enumerate(Tests):    
    if nucleotideContent(dnaString) == dnaDict:    
        passes += 1    
    else:    
        print('test %d failed' % int(i+1))    
    
print('%d/%d tests passed' % (passes, len(Tests)))



