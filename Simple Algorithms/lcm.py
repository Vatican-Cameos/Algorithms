# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def lcm_efficient(a, b):
    return ((a * b) // gcd_efficient(a, b))


def gcd_efficient(a, b):
    if (b == 0):
        return int(a)
    a, b = b, a % b
    return gcd_efficient(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(int(lcm_efficient(a, b)))
