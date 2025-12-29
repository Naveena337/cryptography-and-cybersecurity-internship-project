CODE: 
# A Python program to print all  
# permutations using library function  
from itertools import permutations  
# Get all permutations of [1, 2, 3]  
perm = permutations([1, 2, 3])  
# Print the obtained permutations  
for i in list(perm):  
print (i)
Output:
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
