###########################
##  Caitlin J. Corbin    ##
##  "Entropy calculator"  ##
###########################

import math

print("Enter the weighted motifs percentage.\n")
a = float(input("a: "))
t = float(input("t: "))
c = float(input("c: "))
g = float(input("g: "))

if a == 0:
    pass
else:
    a = (a * (math.log2(a)))
if t == 0:
    pass
else:
    t = (t * (math.log2(t))) 
if c == 0:
    pass
else:
    c = (c * (math.log2(c)))
if g == 0:
    pass
else:
    g = (g * (math.log2(g)))

output = abs((a + t + c + g))



print(output)
