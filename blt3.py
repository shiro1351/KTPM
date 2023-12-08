#câu 1
def giai_thua(n):
    if n < 0:
        print("Khong ton tai")
    if n == 0:
        return 1
    else:
        return n * giai_thua(n - 1)

#câu 2
def is_Prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#câu 3
def tinh_tong():
    list = input("Nhap day so can truyen vao cach nhau boi dau phay: ").split(', ')

    if all(n.replace('-', '').replace('-', '').isdigit() for n in list):
        list = [int(n) for n in list]
        tong = sum(list)
        print(tong)
    else:
        print("day so ko hop le")

tinh_tong()
#vd nhap 2, 3, 4  ket qua = 9

#câu 4
def tim_kiem(a,b,c):
    so_be = min(a, b, c)
    so_lon = max(a, b, c)
    return so_be, so_lon

a, b, c = 3, 4, 5
so_be, so_lon = tim_kiem(a, b, c)
print("so be nhat trong ba so", a, b, c, "la:", so_be)
print("so lon nhat trong ba so", a, b, c, "la:", so_lon)

#câu 5
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
  
s = input("Nhap vo 1 chuoi: ")
  
print("Chuỗi ban đầu là : ", end='')
print(s)
  
print("Chuỗi đã được đảo ngược (sử dụng vòng lặp) là : ",reverse(s), end='')

