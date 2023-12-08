def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Nhập vào một số nguyên n: "))
s  = []
for i in range(1, n + 1):
    s.append(fibonacci(i))
print(f"Các số Fibonacci cho đến {n} là: {s}")
