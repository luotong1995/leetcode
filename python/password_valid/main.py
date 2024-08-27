import sys


def valid(str_input):
    if len(str_input) <= 8:
        print('NG')
        return
    count = [0, 0, 0, 0]
    for i in str_input:
        if i.isdigit():
            count[0] = 1
        elif i.islower():
            count[1] = 1
        elif i.isupper():
            count[2] = 1
        else:
            count[3] = 1
    if sum(count) < 3:
        print('NG')
        return
    for i in range(len(str_input) - 2):
        a_str = str_input[i:i + 3]
        for j in range(i + 3, len(str_input) - 2):
            b_str = str_input[j:j + 3]
            if b_str == a_str:
                print('NG')
                return
    print('OK')


for line in sys.stdin:
    a = line.split()
    valid(a[0])
