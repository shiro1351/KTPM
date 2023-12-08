#caau 1
def doi_xung(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True

n = input()
kq = doi_xung(n)

if kq:
    print(n)
else:
    print("ko doi xung")

#caua 2
def uoc(a, b):
    while b:
        a, b = b, a % b
    return a

a= int(input())
b = int(input())
print("uoc chung cua hai so la:", uoc(a, b))
#cau 3

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

#cau 5
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

#cau 4
def tong_chu_so(s):
    n = str(s)
    tong = 0

    for digit in n:
        total += int(digit)
    return tong

a = int(input())
print("tong cac chu so la", tong_chu_so(a))

