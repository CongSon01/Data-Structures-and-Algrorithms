
def linear_search(arr, target):
    for index, item in enumerate(arr):
        if item == target:
            return index
    return -1

arr = [1,2,3,4,5]
kq = linear_search(arr, 0)
if kq < 0:
    print('Vi tri can tim la: ', kq)
else:
    print('khong tim thay')
