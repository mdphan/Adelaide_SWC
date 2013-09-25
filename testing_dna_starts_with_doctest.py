class UnknownBaseException(Exception):
    pass

def dna_starts_with(string, prefix):
    '''Check whether a DNA string starts with the prefix
    Run: python testing_dna_stars_with_doctest.py -v
    >>> dna_starts_with('atga', 'a')
    True
    >>> dna_starts_with('atga', '')
    True
    >>> dna_starts_with('atga', 'atgaca')
    False
    >>> dna_starts_with('atga', 'ATG')
    False
    '''
    if 'N' in string:
        raise UnknownBaseException()
    return string[0:len(prefix)]==prefix   

try:
    dna_starts_with()
except UnkownBaseException:
    
     

if __name__ == '__main__':
    import doctest
    doctest.testmod()

