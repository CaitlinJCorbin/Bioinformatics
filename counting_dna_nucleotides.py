#################################################
## Caitlin J. Corbin                           ##
## List the number of individual nucleotides   ##
#################################################

nucleotides = 'TGTCAAGCTACGGCCGCAAGGAAGGGGCGAACTTGCCCTCCCAATAATCTGGGTTTTAGTAATTAACTAACATCGGATCCGAGTTCATTAATTCGATTATACGCAGGGGGGGCTGCGGTCTATTCATTGCCCTTTTGGACAGTTGTAGGGTGGGAGCCTTGCGTACATTGGTATGTAGGTGTTATCGTTTCAAGTTGCATTAATGCAATTCCCAGTCGAACCAGATCCTTGAAGCATAAGACGGAGGGCGGACATCCAATGTGTAATACGCGCAAGGCCGGACCCTCAGGTTCCACACGGCCGCACAGTGATTAATCGTAGCGTAGTGACTGCTTGCGATTGTAGGTATTATATTCCGTGCCGGTGTGCGCGGCCTCATTTGCGACTGCCGATGGGAACCGTTCATGTTCTTTTCGTAATGGAGAGTATACCGGGCTTTAGAGCTTTTCATGGAAACTACATAACGGACGATCCCCTCTTCGCTTCCTCTTTAACACCTAATCTGACGCTCCCGTACTGTGAACGAGGCCACGAGGGCCCGTACGGGCTATGATGATGATCGCGTACAGGCTTCGGCGCATCCCGTCTTTTACTCCCACCGTCCACAGTGACAGTATGATGTGATGAAGAATTAAACTTTGACCCGTAGGAATGCGTCCCGGCCTAACTGGTCACACGGCCACCATTCATAAATACCCTACAGAGGGTGGAGGTGCATGTCCGTGCGTATACCTCGACAAAATTATTGTCGAACTGAGTAGTCACTCAGGTAACAACGGGTTAAGTCCCGTTAATCCCGTCAGCGGCAATCACTACTGAAATATTGCAGAGCACAGTGTGCGGGTATTCACTGATCTAGGCGACTCGTGATCATATCACATTTG'
arr = list(nucleotides)

a = 0
c = 0
g = 0
t = 0
x = 0
for x in arr:
    if x == 'A':
        a += 1
    elif x == 'C':
        c += 1
    elif x == 'G':
        g += 1
    elif x == 'T':
        t += 1

print(a, " ", c, " ", g, " ", t)


