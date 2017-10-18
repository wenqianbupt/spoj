import sys
import os
import re


def fun(a, b, operator):
    c = []
    if operator == '+':
        c.append(a + b)
        return c
    if operator == '-':
        c.append(a - b)
        return c
    if operator == '*':
        tmp = b
        if b < 10:
            c.append(a * tmp)
        else:
            for i in range(len(str(b))):
                c.append(a * (b % 10))
                b //= 10
            c.append(a * tmp)
        return c


def get_result(left, right, values, operator):
    right = operator + right
    max_len = max(len(left), len(right), len(values[-1]))
    result = []
    result.append(left.rjust(max_len))
    result.append(right.rjust(max_len))
    length = max(len(right), len(values[0]))
    result.append(''.ljust(length, '-').rjust(max_len, ' '))

    if len(values) == 1:
         result.append(values[0].rjust(max_len))
    else:
        for i in range(len(values) - 1):
            values[i] = values[i].ljust(int(len(values[i]) + i), ' ')
            result.append(values[i].rjust(max_len))
        result.append(''.ljust(len(values[-1]), '-').rjust(max_len, ' '))
        result.append(values[-1].rjust(max_len))

    return result

if __name__ == '__main__':
    first_line = sys.stdin.readline()
    count = int(first_line)

    results = []

    for i in range(count):
        s1, opr, s2 = re.split(r'(\+|\-|\*)', str(sys.stdin.readline().strip()))
        s3 = list(map(str, fun(int(s1), int(s2), opr)))
        results.extend(get_result(s1, s2, s3, opr))
        results.append('')

    print(os.linesep.join(results))
