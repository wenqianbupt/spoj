import sys
import os

if __name__ == '__main__':
    first_line = sys.stdin.readline()
    count = int(first_line)

    results = []

    for i in range(count):
        line = sys.stdin.readline().strip()
        str = ''
        operators = []
        for n in range(len(line)):
            if line[n].islower():
                str += line[n]
            elif line[n] == '+' or line[n] == '-' or line[n] == '*' or line[n] == '/' or line[n] == '^':
                operators.append(line[n])
            elif line[n] == ')':
                str += operators[-1]
                operators.pop()

        results.append(str)

    print(os.linesep.join(results))



