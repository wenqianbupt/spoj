import sys
import os

def reverse(value):
    return int(''.join(list(reversed(str(value)))))

if __name__ == '__main__':
    first_line = sys.stdin.readline()
    count = int(first_line)

    results = []

    for i in range(count):
        a, b = map(int, sys.stdin.readline().strip().split())
        c = reverse(a) + reverse(b)
        results.append(str(reverse(c)))

    print(os.linesep.join(results))