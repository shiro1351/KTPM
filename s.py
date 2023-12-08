n = int(input("Nhập một số nguyên dương n: "))
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print("Tổng các chữ số của", n, "là:", total)