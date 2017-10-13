import sys

import os

def get_prime_numbers_str(start_str, stop_str):
    """
    >>> get_prime_numbers_str('2', '8')
    ['2', '3', '5', '7', '']
    >>> get_prime_numbers_str('10', '19')
    ['11', '13', '17', '19', '']
    >>> get_prime_numbers_str('18', '25')
    ['19', '23', '']
    """

    start = int(start_str)
    stop = int(stop_str)

    result =[]
    num = start
    while num <= stop:
        if num == 1:
            num +=1
        elif num == 2:
            result.append('2')
        else:
            for n in range(2, num):
                if num % n == 0:
                    break
            else:
                result.append(str(num))
        num += 1
    result.append('')
    return result

if __name__ == '__main__':
    first_line = sys.stdin.readline()
    count = int(first_line)

    results = []

    for i in range(count):
        line = sys.stdin.readline()[:-1].split()
        results += iter(get_prime_numbers_str(line[0], line[1]))

    print(os.linesep.join(results))



