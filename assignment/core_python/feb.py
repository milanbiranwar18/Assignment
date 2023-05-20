def feb(n, a, b):
    if n == 0:
        return
    c = a + b
    print(c)
    a = b
    b = c
    return feb(n-1, a, b)


if __name__ == '__main__':
    feb(10, 0, 1)
