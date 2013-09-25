# Exercise 9

#Given a string 'filename', write a function which opens that file, #iterates over all sequences, and writes a bit of stats about each #sequence:
#- print the name of each sequence
#- Count of Ns
#- GC-content
#Print amount of sequences in that file.
#Tips: 
#-  if line.startswith('>') - give the name

def GC_content(dna):
    dna = dna.replace('N','')
    countG = dna.count('G')
    countC = dna.count('C')
    results = (countG + countC) / float(len(dna))
    return results

def dna_summary(filename):
    file = open(filename, 'r')    
    line = file.readline()
    while line != '':              
        if line.startswith('>'):
            name = line.replace('>','')
            name = name.replace('\n','')
            print "Name of sequence: ", name
        else:
            print "Count of Ns: ", line.count('N')
            print "GC content: ", GC_content(line) , "\n"
        line = file.readline()

print dna_summary('seq1.fasta')


            
