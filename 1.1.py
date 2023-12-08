n = int(input("Nhap n: "))
tong = 0
for i in range(1, n+1):
    tong += i
print("tong cac so tu 1 den n:",tong) 

print("Cac so chan tu 1 den", n,":", end=' ')
for i in range(0, n + 1, 2):
    print( i,end=' ')

print()

print("Cac so le tu 1 den", n ,":",end=' ')
for i in range(1, n + 1, 2):
    print(i, end=' ')

print()

tong_so_chia_het_cho_3 = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        tong_so_chia_het_cho_3 += i
print("tong cua so chia het cho 3:",tong_so_chia_het_cho_3)
print()


for i in range(1, 11):
    print("Bang cuu chuong cua", i,end=' ')
    print()
    for j in  range(1, 11):
        print(i,"*",j, "=" ,i * j, end=' ')
        print()