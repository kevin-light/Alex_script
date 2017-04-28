for n in fib(6):
    print(n)
g = fib(6)
while True:
    try:
       x = next(g)
       print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break