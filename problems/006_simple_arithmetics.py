import sys
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
    if len(values) == 1:
        max_len = max(len(left), len(right), len(values[0]))
        print('')
        print(left.rjust(max_len))
        print(right.rjust(max_len))
        print(''.rjust(max_len, '-'))
        print(values[0].rjust(max_len))
    else:
        pass

if __name__ == '__main__':
    first_line = sys.stdin.readline()
    count = int(first_line)



    for i in range(count):
        s1, opr, s2 = re.split(r'(\+|\-|\*)', str(sys.stdin.readline().strip()))
        s3 = list(map(str, fun(int(s1), int(s2), opr)))
        get_result(s1, s2, s3, opr)
