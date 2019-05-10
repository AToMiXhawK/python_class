
"""Given a number N, check if a number is perfect or not. 
A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number"""

import math
for _ in range(int(input())):
    n=int(input())
    sum=1
    for i in range(2,int(math.sqrt(n)+1)):
        if(n%i==0):
            sum=sum+i+n/i
    if(sum==n):
        print("1")
    else:
        print("0")
    
