
def binary_Search(arr, target):
    low = 0
    high = len(arr) - 1
    mid = 0
    while (low <= high):
        mid = (high + low) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1

arr = [1,1,3,4,5]

x = 5
kq = binary_Search(arr, x)

if kq == -1:
    print('khong tim thay') 
else:
    print('O vi tri: ', str(kq))