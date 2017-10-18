import sys
import os

if __name__ == '__main__':
    first_line = sys.stdin.readline()
    count = int(first_line)

    results = []

    for i in range(count):
        line = sys.stdin.readline().strip()
        s = ''
        operators = []
        for n in range(len(line)):
            if line[n].islower():
                s += line[n]
            elif line[n] == '+' or line[n] == '-' or line[n] == '*' or line[n] == '/' or line[n] == '^':
                operators.append(line[n])
            elif line[n] == ')':
                s += operators[-1]
                operators.pop()

        results.append()

    print(os.linesep.join(results))



