# If you need to import additional packages or classes, please import here.

def func():
    s = input()
    words = s.split(' ')
    result = sum([len(item) for item in words]) / len(words)
    print('%.2f' % result)


if __name__ == "__main__":
    func()
