def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def is_prime(num):
    num = float(num)
    for divisor in xrange(2, int(num**0.5)+1):
        if num % divisor == 0:
            return False

    return True

def answer(floor, start=0):
    num = fib(start)

    if is_prime(num):
        if num > floor:
            return num

    return answer(floor=floor, start=(start+1))

