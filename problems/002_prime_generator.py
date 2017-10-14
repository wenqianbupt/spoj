import sys
import math
import os
from itertools import chain


def get_prime_numbers(start, stop):
    """
    >>> get_prime_numbers(1, 1)
    []
    >>> get_prime_numbers(1, 2)
    [2]
    >>> get_prime_numbers(2, 2)
    [2]
    >>> get_prime_numbers(2, 3)
    [2, 3]
    >>> get_prime_numbers(1, 8)
    [2, 3, 5, 7]
    >>> get_prime_numbers(10, 19)
    [11, 13, 17, 19]
    >>> get_prime_numbers(18, 25)
    [19, 23]
    """

    result = []
    if start == 1 and stop == 1:
        return result
    elif start == 1 and stop == 2:
        result.append(2)
        result.append(None)
        return result
    elif start == 1 and stop > 2:
        start += 1

    if start == 2:
        result.append(2)
        start += 1
    elif start % 2 == 0:
        start += 1

    for num in range(start, stop + 1, 2):
        if num == 3 or num == 5 or num == 7:
            result.append(num)
        else:
            for n in range(3, int(math.sqrt(num)) + 1, 2):
                if num % n == 0:
                    break
            else:
                result.append(num)
    result.append(None)
    return result


if __name__ == '__main__':
    first_line = sys.stdin.readline()
    count = int(first_line)

    numbers = []
    results = []

    for i in range(count):
        line = sys.stdin.readline()[:-1].split()
        numbers = chain(numbers, get_prime_numbers(int(line[0]), int(line[1])))
    for idx in numbers:
        results.append(str(idx))
    print(os.linesep.join(results))
