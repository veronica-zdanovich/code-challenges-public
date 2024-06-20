from threading import Lock, Thread


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = Lock()
        self.even_lock = Lock()
        self.odd_lock = Lock()

        self.even_lock.acquire()
        self.odd_lock.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zero_lock.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.even_lock.release()
            else:
                self.odd_lock.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.even_lock.acquire()
            printNumber(i)
            self.zero_lock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()


class Solution:
    def run(self, n: int):
        zeroEvenOdd = ZeroEvenOdd(n)

        thread_zero = Thread(target=zeroEvenOdd.zero, args=(lambda n: print(n, end=''),))
        thread_even = Thread(target=zeroEvenOdd.even, args=(lambda n: print(n, end=''),))
        thread_odd = Thread(target=zeroEvenOdd.odd, args=(lambda n: print(n, end=''),))

        threads = [thread_zero, thread_even, thread_odd]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
