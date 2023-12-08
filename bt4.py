#cau 1
def find_mm(lt):
    if not lt:
        return None, None
    
    so_nho = so_lon = lt[0]
    
    for n in lst[1:]:
        if num < so_nho:
            so_nho = n
        elif num > so_lon:
            so_lon = n

    return min_val, max_val


#câu 2
def so_chia_het(lt, a):
    for n in lt:
        if n % a == 0:
            return n
        else:
            print("Ko co phan tu trong danh sach chia het:", a)


#câu 3
def loai_bo(lst):
    ue = list(set(lst))
    return ue

#câu 4
def tong(lst):
    so_chan = filter(lambda x: x % 2 == 0, lst)
    total = sum(so_chan)
    return total

#câu 5
def tang_dan(list):
    return all(list[i] <= list[i + 1] for i in range(len(list) - 1))