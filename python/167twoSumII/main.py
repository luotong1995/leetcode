def two_sum(numbers, target):
    i = 0
    j = len(numbers) - 1
    while True and i != j:
        if numbers[i] + numbers[j] == target:
            return [i, j]
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            j -= 1


if __name__ == '__main__':
    numbers = [2,3,4]
    target = 6
    print(two_sum(numbers, target))
