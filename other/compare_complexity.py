import time


def measure_time(func, arguments):
    start = time.process_time()
    result = func(arguments)
    stop = time.process_time()
    return result, stop - start


def linear(n: int) -> int:
    count = 0
    for i in range(0, n):
        count += 1

    return count


def quadratic(n: int) -> int:
    count = 0
    for i in range(0, n):
        for j in range(0, n):
            count += 1

    return count


def cubic(n: int) -> int:
    count = 0
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                count += 1

    return count


def logarithmic(n: int) -> int:
    count = 0
    while n > 0:
        count += 1
        n /= 2
        n = int(n)

    return count


def n_logarithmic(n: int) -> int:
    count = 0
    for i in range(0, n):
        k = n
        while k > 0:
            count += 1
            k /= 2
            k = int(k)

    return count


n = 500

count_linear, time_linear = measure_time(linear, n)
print(f"Linear: {count_linear} operations, {time_linear} seconds")

count_quadratic, time_quadratic = measure_time(quadratic, n)
print(f"Quadratic: {count_quadratic} operations, {time_quadratic} operations")

count_cubic, time_cubic = measure_time(cubic, n)
print(f"Cubic: {count_cubic} operations, {time_cubic} seconds")

count_logarithmic, time_logarithmic = measure_time(logarithmic, n)
print(f"Logarithmic: {count_logarithmic} operations, {time_logarithmic} seconds")

count_n_logarithmic, time_n_logarithmic = measure_time(n_logarithmic, n)
print(f"N Logarithmic: {count_n_logarithmic} operations, {time_n_logarithmic} seconds")
