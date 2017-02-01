"""
You are given a list of size N, initialized with zeroes. 
You have to perform M operations on the list and output the maximum of final values of all the  elements in the list. 
For every operation, you are given three integers a, b and k and you have to add value k to all the elements ranging from index a to b(both inclusive).

Input Format

First line will contain two integers N and M separated by a single space.
Next  lines will contain three integers a, b and k separated by a single space.
Numbers in list are numbered from 1 to N.


Output Format

A single line containing maximum value in the updated list.

Sample Input

5 3
1 2 100
2 5 100
3 4 100

Sample Output

200
"""

import sys

nm = sys.stdin.readline()
nm = nm.split(' ')
n = int(nm[0])
m = int(nm[1])
data = [0] * (n + 1)
max = 0
weight = 0

for i in range(m):
    line = sys.stdin.readline()
    line= line.split(' ')
    a = int(line[0])
    b = int(line[1])
    k = int(line[2])
    data[a-1] += k
    data[b] -= k
    
for j in data:
    weight += j
    if weight > max:
        max = weight
        
print(max)