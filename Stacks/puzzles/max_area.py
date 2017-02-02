"""
There are N buildings in a certain two-dimensional landscape. Each building has a height h(i). 
If you join K adjacent buildings, they will form a solid rectangle of area  K * min(h(i), h(i+1)... h(i+k-1)).

Given N buildings, find the greatest such solid area formed by consecutive buildings.

Input Format 
The first line contains N, the number of buildings altogether. 
The second line contains N space-separated integers, each representing the height of a building.

Output Format 
One integer representing the maximum area of rectangle formed.

Sample Input

5
1 2 3 4 5
Sample Output

9
"""


import sys

n = int(sys.stdin.readline())

data = sys.stdin.readline()
data = data
data = data.split(' ')
data.append(0)

max_area = -1
S = Stack()

for height in data:
    height = int(height)
    k = 0
    while (not S.is_empty()) and height < S.top():
        k += 1
        max_area = max(max_area, k * S.pop())
        
    for i in range(k + 1):
        S.push(height)
        
print max_area