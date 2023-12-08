#câu 1
def tinh_tong(tuple):
    tong = 0 
    for x in tuple:
        tong += x
    return tong

#câu 2
def check(x, tuple):
    return x in tuple

#câu 3
def ket_hop(tuple):
    result = ''.join(tuple)
    return result

#câu 4
def search(a, b):
    return a.intersection(b)

#câu 5
def union_intersection(a,b):
    Union = a.union(b)
    Intersection = a.intersection(b)
    return Union, Intersection

#câu 6
def check(List):
    list_set = list(List)

    if len(list_set) <= 1:
        return True
    
    for i in range(1, len(list_set)):
        if list_set[i] <= list_set[i - 1]:
            return False
    return True

#câu 7
def dem(String):
    reusult = {}

    for x in String:
        reusult[x] = reusult.get(x, 0) + 1
    return reusult

#câu 8
def khoa(x , Dict):
    return x in Dict

#câu 9
def tong(Dict):
    tong = sum(Dict.values())
    return tong

#câu 10
def xoa(Dict, lock):

    if lock in Dict:
        new_Dict = dict(Dict)
        del new_Dict[lock]
        return new_Dict
    else:
        return Dict

