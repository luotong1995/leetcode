def main():
    input_str = input()
    str_list = input_str.split(";")
    result = [0, 0]
    for item in str_list:
        if item and item[0] in ['A', 'D', 'W', 'S'] and item[1:].isdigit():
            x = item[0]
            y = int(item[1:])
            if x == 'A':
                result[0] = result[0] - y
            elif x == 'D':
                result[0] = result[0] + y
            elif x == 'W':
                result[1] = result[1] + y
            elif x == 'S':
                result[1] = result[1] - y
    print('{},{}'.format(result[0], result[1]))


if __name__ == '__main__':
    main()
