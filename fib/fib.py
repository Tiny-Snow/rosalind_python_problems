# F_{n} = F_{n-1} + k * F_{n-2}  

n, k = map(int, input().split())
Fib = [0 for _ in range(n + 1)]
Fib[1] = Fib[2] = 1

def Fibonacci(n, k):
    if Fib[n] != 0:
        return Fib[n]
    else:
        return Fibonacci(n - 1, k) + k * Fibonacci(n - 2, k)

print(Fibonacci(n, k))