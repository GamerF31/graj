def number(i):
    if i<0:
        return
    print(f'i:{i}')
    number(i-1)

number(9)


def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fib(n - 1) + fib(n - 2)

print(fib(8))
