import sys
import os
from collections import Counter

if __name__ == '__main__':
    first_line = sys.stdin.readline()
    count = int(first_line)

    results = []
    accounts = []

    for i in range(count):
        acc_num_line = sys.stdin.readline()
        acc_num = int(acc_num_line)
        for n in range(acc_num):
            accounts.append(sys.stdin.readline().strip())
        acc_count = Counter(accounts)
        for k in sorted(acc_count):
            results.append(k + ' ' + str(acc_count[k]))
        results.append('')
        accounts = []

        if i < count - 1:
            sys.stdin.readline()

    print(os.linesep.join(results))





