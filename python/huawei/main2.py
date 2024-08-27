# If you need to import additional packages or classes, please import here.

def func():
    while True:
        try:
            a, b = map(int, input().strip().split())
            print(a + b)
        except EOFError:
            break


if __name__ == "__main__":
    func()
