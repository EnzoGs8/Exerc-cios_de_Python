# Função para calcular o N-ésimo Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Leitura do número de casos de teste
T = int(input())

for _ in range(T):
    N = int(input())
    print(f"Fib({N}) = {fibonacci(N)}")
