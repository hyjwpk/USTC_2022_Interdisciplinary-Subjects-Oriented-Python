import numpy
import scipy.integrate
import time

def integrate():
    def integrate1():
        for i in range(0, 10000):
            v, err = scipy.integrate.dblquad(lambda x, y: (y + x ** 2) ** 0.5, 0, 1, lambda x: (-x), lambda x: x)
        print(v)

    def integrate2():
        for i in range(0, 10000):
            result = 0
            length = 1000
            for x in numpy.linspace(0, 1, length):
                start = -x
                stop = x
                y = numpy.linspace(start, stop, length)
                f = (x + y ** 2) ** 0.5
                result += (sum(f * (stop - start) / length)) / length
        print(result)

    start1 = time.perf_counter()
    integrate1()
    elapsed1 = (time.perf_counter() - start1)

    start2 = time.perf_counter()
    integrate2()
    elapsed2 = (time.perf_counter() - start2)

    print(elapsed2 / elapsed1)

integrate()
