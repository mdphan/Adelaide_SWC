#Exercise 3:
#input_string = "GATCAGTCGATCGACTGCTAGCTAGCTAGTACGGCGTATA"
#create a dictionary in the following format:
#{'G': (# of occurences in the string),
#'A': ...
#}
#print the dictionary
#dna_dict = {'G'


input_string = "GATCAGTCGATCGACTGCTAGCTAGCTAGTACGGCGTATA"

countA = input_string.count('A')
countT = input_string.count('T')
countG = input_string.count('G')
countC = input_string.count('C')

dna_dict = {'A':countA, 'T':countT, 'G':countG, 'C': countC}
print dna_dict


#extra credit: print the GC content (the proportion of the string that is either G's or C's, from 0 to 1)

GCcontent = float(dna_dict['G'] + dna_dict['C'] / len(input_string))

print GCcontent
