def DNA_strand1(dna):
    complements = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }
    return ''.join([complements[a] for a in dna])
    

def DNA_strand2(dna):
    # code here
    dnaComplement=""
    for string in dna:
        if string=="A":
            dnaComplement+="T"
        elif string =="T":
            dnaComplement+="A"
        elif string =="G":
            dnaComplement+="C"
        elif string == "C":
            dnaComplement+="G"
    return dnaComplement