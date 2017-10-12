import sys


def reverse_str(value):
    """
    >>> reverse_str("1234")
    '4321'
    """
    return ''.join(list(reversed(value)))


def get_next_palindrome(value):
    """
    >>> get_next_palindrome('1234')
    '1331'
    >>> get_next_palindrome('9999')
    '10001'
    >>> get_next_palindrome('302')
    '303'
    >>> get_next_palindrome('102')
    '111'
    >>> get_next_palindrome('929')
    '939'
    >>> get_next_palindrome('928')
    '929'
    >>> get_next_palindrome('999')
    '1001'
    >>> get_next_palindrome('101')
    '111'
    """
    if len(value) % 2 == 0:
        left = value[:len(value) // 2]
        right = value[len(value) // 2:]
        if left > right:
            right = reverse_str(left)
            return left + right
        else:
            new_left = str(int(left) + 1)
            if len(new_left) == len(left):
                return new_left + reverse_str(new_left)
            else:
                return new_left + reverse_str(new_left)[1:]
    else:
        left = value[:len(value) // 2]
        right = value[len(value) // 2 + 1:]
        if left > right:
            return left + value[len(value) // 2] + reverse_str(left)
        elif left == right:
            mid = value[len(value) // 2]
            if mid == '9':
                new_left = str(int(left) + 1)
                return new_left + reverse_str(new_left)
            else:
                return left + str(int(value[len(value) // 2]) + 1) + right
        else:
            mid = value[len(value) // 2]
            if mid == '9':
                new_left = str(int(left) + 1)
                return new_left + reverse_str(new_left)
            else:
                return left + str(int(value[len(value) // 2]) + 1) + reverse_str(left)


if __name__ == '__main__':
    first_line = sys.stdin.readline()
    count = int(first_line)

    for i in range(count):
        line = sys.stdin.readline()[:-1]
        print(get_next_palindrome(line))
