##################################################
## Caitlin J. Corbin                            ##
## Translating RNA into Proteins                ##
## Codon Table:                                 ##
## UUU F      CUU L      AUU I      GUU V       ##
## UUC F      CUC L      AUC I      GUC V       ##
## UUA L      CUA L      AUA I      GUA V       ## 
## UUG L      CUG L      AUG M      GUG V       ##
## UCU S      CCU P      ACU T      GCU A       ##
## UCC S      CCC P      ACC T      GCC A       ##
## UCA S      CCA P      ACA T      GCA A       ##
## UCG S      CCG P      ACG T      GCG A       ##
## UAU Y      CAU H      AAU N      GAU D       ##
## UAC Y      CAC H      AAC N      GAC D       ##
## UAA Stop   CAA Q      AAA K      GAA E       ##
## UAG Stop   CAG Q      AAG K      GAG E       ##
## UGU C      CGU R      AGU S      GGU G       ##
## UGC C      CGC R      AGC S      GGC G       ##
## UGA Stop   CGA R      AGA R      GGA G       ##
## UGG W      CGG R      AGG R      GGG G       ##
##################################################

rna_string = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
protein_stack = []

i = 0
rna_array = [rna_string[i:i+3] for i in range(0, len(rna_string), 3)]

for n in range (len(rna_array)):
    if rna_array[n] == 'UUU' or rna_array[n] == 'UUC':
        protein_stack.append('F')

    elif(rna_array[n] == 'UUA' or rna_array[n] == 'UUG' or 
        rna_array[n] == 'CUU' or rna_array[n] == 'CUC' or 
        rna_array[n] == 'CUA' or rna_array[n] == 'CUG'):
        protein_stack.append('L')

    elif(rna_array[n] == 'UCU' or rna_array[n] == 'UCC' or 
        rna_array[n] == 'UCA' or rna_array[n] == 'UCG' or 
        rna_array[n] == 'AGU' or rna_array[n] == 'AGC'):
        protein_stack.append('S')

    elif rna_array[n] == 'UAU' or rna_array[n] == 'UAC':
        protein_stack.append('Y')

#    elif(rna_array[n] == 'UAA' or rna_array[n] == 'UAG' or 
#        rna_array[n] == 'UGA'):
#        protein_stack.append(' STOP ')

    elif rna_array[n] == 'UGU' or rna_array[n] == 'UGC':
        protein_stack.append('C')

    elif rna_array[n] == 'UGG':
        protein_stack.append('W')

    elif(rna_array[n] == 'CCU' or rna_array[n] == 'CCC' or 
        rna_array[n] == 'CCA' or rna_array[n] == 'CCG'):
        protein_stack.append('P')

    elif rna_array[n] == 'CAU' or rna_array[n] == 'CAC':
        protein_stack.append('H')

    elif rna_array[n] == 'CAA' or rna_array[n] == 'CAG':
        protein_stack.append('Q')

    elif(rna_array[n] == 'CGU' or rna_array[n] == 'CGC' or 
        rna_array[n] == 'CGA' or rna_array[n] == 'CGG' or 
        rna_array[n] == 'AGA' or rna_array[n] == 'AGG'):
        protein_stack.append('R')

    elif(rna_array[n] == 'AUU' or rna_array[n] == 'AUC' or 
        rna_array[n] == 'AUA'):
        protein_stack.append('I')

    elif rna_array[n] == 'AUG':
        protein_stack.append('M')

    elif(rna_array[n] == 'ACU' or rna_array[n] == 'ACC' or 
        rna_array[n] == 'ACA' or rna_array[n] == 'ACG'):
        protein_stack.append('T')

    elif rna_array[n] == 'AAU' or rna_array[n] == 'AAC':
        protein_stack.append('N')

    elif rna_array[n] == 'AAA' or rna_array[n] == 'AAG':
        protein_stack.append('K')

    elif(rna_array[n] == 'GUU' or rna_array[n] == 'GUC' or 
        rna_array[n] == 'GUA' or rna_array[n] == 'GUG'):
        protein_stack.append('V')

    elif(rna_array[n] == 'GCU' or rna_array[n] == 'GCC' or 
        rna_array[n] == 'GCA' or rna_array[n] == 'GCG'):
        protein_stack.append('A')

    elif rna_array[n] == 'GAU' or rna_array[n] == 'GAC':
        protein_stack.append('D')
        
    elif rna_array[n] == 'GAA' or rna_array[n] == 'GAG':
        protein_stack.append('E')

    elif(rna_array[n] == 'GGU' or rna_array[n] == 'GGC' or 
        rna_array[n] == 'GGA' or rna_array[n] == 'GGG'):
        protein_stack.append('G')

protein_str = ''.join(protein_stack)

print(protein_str)