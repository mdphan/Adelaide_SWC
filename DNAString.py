# gc_content
# base_count('G')
# reverse_complement()

class NucleotideString:
    base_complement = {'A':'T', 'T':'A', 'G':'C','C':'G'}

    def __init__(self, seq_name, seq):
        self.seq_name = seq_name
        self.seq = seq
        self.bases = {}

    def base_count(self, base):
        '''Count the number of times the specified base occurs in the sequence.'''
        if base in self.bases:
            return self.bases[base]
        else self.bases[base] = self.seq.count(base)
        return self.bases[base]

    def gc_content(self):
        return (self.base_count('G') + self.base_count('C'))/ float(len(self.seq))    

    def reverse_complement(self):        
        complement = ''
        for base in self.seq:
            complement = base_complement[base] + complement
        return complement
        
        
class DNAString(NucleotideString):
    pass

class RNAString(NucleotideString):
    base_complement = {'A':'U', 'U':'A', 'G':'C','C':'G'}


