# Uses python3
#
#Problem Description
#Task. The goal in this problem is to find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.
#Input Format. The input consists of a single integer 𝑚.
#Constraints. 1 ≤ 𝑚 ≤ 103.
#Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.
#Sample 1.
#Input:
#2
#Output:
#2
#2 = 1 + 1.
#
#Sample 2.
#Input:
#28
#Output:
#6
#28 = 10 + 10 + 5 + 1 + 1 + 1.


import sys

def get_change(m):
    #write your code here
    denominations = [10,5,1]
    nCount = 0;
    while(m != 0):
        for denomination in denominations :
            if(denomination <= m):
                m = m - denomination;
                nCount += 1
                break
    return nCount

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
