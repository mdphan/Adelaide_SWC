# Exercise 8
#given a string 'dna', remove all 'N', return the GC-content
dna  = 'ATGCNNNNNNNN'
dna2 = 'NGGGGGGGGGGGC'
dna3 = 'GTGTGTGTGTGTTT'

def GC_content(dna):
    dna = dna.replace('N','')
    countG = dna.count('G')
    countC = dna.count('C')
    results = (countG + countC) / float(len(dna))
    return results

print GC_content(dna)
print GC_content(dna2)
print GC_content(dna3)
