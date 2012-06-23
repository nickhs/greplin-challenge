def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def is_prime(num):
    num = num * 1.0
    for divisor in xrange(2, int(num**0.5)+1):
        if num/divisor == int(num/divisor):
            return False

    return True

def run(floor, start=0):
    size = 5

    fibnums = []

    for i in xrange(start, start+size):
        fibnums.append(fib(i))

    for num in fibnums:
        if is_prime(num):
            if num > floor:
                return num

    return run(floor=floor, start=(start+size))

