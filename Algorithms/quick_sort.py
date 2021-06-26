
"""
ideal:
Chọn phần tử cuối làm pivot
chia 2 phần
- phan 1: < pivot
- phan 2: > pivot
Tiếp tục đệ quy cho từng phần

* Độ phức tạm: O(n log n).
"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    greater, lesser = [], []
    for item in arr:
        if item > pivot:
            greater.append(item)
        else:
            lesser.append(item)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

arr = [5,1,3,2,4]
print(quick_sort(arr))