def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def fibonaccic(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
sayi = int(input("Kaç terimli Fibonacci dizisi oluşturmak istiyorsunuz? "))
 
for i in range(sayi):
    print(fibonacci(i), end=", ")
    