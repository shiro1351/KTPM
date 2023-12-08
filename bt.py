#câu 1
def is_Prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

"""n = int(input("Nhap n: "))
if is_Prime(n):
    print(n,"là số nguyên tố")
else:
    print(n,"khong phai la so nguyen to")"""

#câu 2
def giai_thua(n):
    if n < 0:
        print("Khong ton tai")
    if n == 0:
        return 1
    else:
        return n * giai_thua(n - 1)

"""n = int(input("Nhap n: "))
print("giai thua cua", n,":", giai_thua(n))"""

#câu 3
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        fib_sum = 1
        fib_prev = 1
        for i in range(2, n):
            fib_current = fib_sum
            fib_sum += fib_prev
            fib_prev = fib_current
        return fib_sum

"""n = int(input("Nhap n:"))
print("tong fibonacci tu 1 den", n, ":", fibonacci(n))"""

#câu 4
"""n = int(input("Nhap n: "))
print("Cac so nguyen to tu 1 den", n,":", end=' ')
for i in range(1, n + 1):
    if is_Prime(i):
        print(i, end=' ')"""

#câu 5
import math


def so_perfect(n):
    if n <= 1:
        return False
    tong = 1  
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:
                tong += n // i
    return tong == n

"""n = int(input("Nhap n: "))
if so_perfect(n):
    print(n,"la so hoan hao")
else:
    print("ko phai la so hoan hao")"""