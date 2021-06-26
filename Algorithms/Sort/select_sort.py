

#ideal: mỗi lần lặp tìm ra 1 thằng nhỏ nhất sau chuyển cho lên đầu
def findMin(arr):
    #find min
    min = arr[0]
    min_index = 0
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
            min_index = i
    return min_index

def select_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest_index = findMin(arr)
        sorted_arr.append(arr.pop(smallest_index))
    return sorted_arr

arr = [2,1,3,5,6,4]
print(select_sort(arr))