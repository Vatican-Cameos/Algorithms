# Uses python3
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
