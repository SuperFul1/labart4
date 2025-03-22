from typing import List


def fib(n: int) -> List[int]: 

    if n < 0:
        return []
    if n == 0:
        return [0]
    else:
        fib_list = [0, 1]
        while fib_list[-1] + fib_list[-2] < n:
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list


class FibonacchiLst:
    def __init__(self, instance: List[int]):
        self.instance = instance   
        self.idx = 0 

    def __iter__(self):
        return self 

    def __next__(self): 
        while True:
            try:
                res = self.instance[self.idx] 

            except IndexError as e:
                raise StopIteration from e

            num1 = 5 * res ** 2 + 4 
            num2 = 5 * res ** 2 - 4
            if (num1 > 0) and (num1 ** 0.5 % 1 == 0) or (num2 > 0) and (num2 ** 0.5 % 1 == 0):
                self.idx += 1
                return res

            self.idx += 1


def gen_fib():

    prev, curr = 0, 1
    while True:
        yield prev
        prev, curr = curr, prev + curr

def fib_iter(start: int, stop: int):

    from itertools import islice
    return islice(FibonacchiLst(list(range(stop**2))), start, stop)

def test_fib_1():

    assert fib(1) == [0, 1], "Тривиальный случай n = 1, список [0, 1]"


def test_fib_2():

    assert fib(4) == [0, 1, 1, 2, 3], "fib(4) должно быть [0, 1, 1, 2, 3]"

def test_fib_3():

    assert list(fib_iter(1, 7)) == [ 1, 2, 3, 5, 8, 13]

def test_fib_4():

    fib_gen = gen_fib()
    test_list = []
    for _ in range(10):
        test_list.append(next(fib_gen))

    assert test_list == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

if 1 == 1:
    test_fib_1()
    test_fib_2()
    test_fib_3()
    test_fib_4()
