import os


def read_file(filename):
    lines = []
    with open(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'src', filename))) as f:
        for line in f:
            lines.append(line.strip('\n').split(','))

    return lines


def compare_report(lines1, lines2, fn1, fn2):
    results = []
    if len(lines1) != len(lines2):
        results.append('The lines of the two files are not the same.')
    else:
        for i in range(1, len(lines1)):
            if len(lines1[i]) != len(lines2[i]):
                results.append('The character numbers in line {} of the two files are not the same'.format(i))
            else:
                for j in range(len(lines1[i])):
                    if lines1[i][j] != lines2[i][j]:
                        results.append('The {0} in line {1} of the two files are not the same. In file {2}: the {0} is {4}. In file {3}: the {0} is {5}'.format(lines1[0][j], j, fn1, fn2, lines1[i][j], lines2[i][j]))
    return results


if __name__ == '__main__':
    filename1 = 'a.txt'
    filename2 = 'b.txt'
    data1 = read_file(filename1)
    data2 = read_file(filename2)
    reports = compare_report(data1, data2, filename1, filename2)
    for n in range(len(reports)):
        print(reports[n])


