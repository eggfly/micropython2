import os

def test(value):
    a = 1
    b = 2
    c = 3
    return "do nothing"

def test0():
    pass

def test1():
    pass

def test2():
    a = 1
    b = 2
    for i in range(10):
        print(i)
    if a > 1:
        print('a > 1')
    else:
        if b == 2:
            print('a <= 1, b = 2')
        else:
            print('a <= 1, b != 2')
    while True:
        if b == 2:
            break
        if a == 1:
            continue
    print(print(print(print(print(print(print(print(print()))))))))

def test3():
    def test4(value): pass
    test4('123')
    return None


def test4(test_param=11112222, test_param2=22221111):
    return test_param

def test5():
    a = True
    b = False
    c = a and b

def test6():
    a = []
    b = a[:]
    c = a[:-1]
    d = a[2:]
    e = a[1:2]
