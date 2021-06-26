
"""
ideal: Chia ra 2 phan, 1 phan da sort, 1 phan chua sort
check phan tu dau tien cua ben chua sort voi cac phan tu cua mang da sort
neu nho hon thi swap

* do phuc tap: 
- Neu all data deu phai cap nhat: O(n)
- Neu mang bi nguoc (tu lon -> nho): O(n/2)
--> trung binh O(n^2) 
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        while(i > 0 and arr[i] < arr[i-1]):
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    return arr

arr = [5,1,2,4,3]
print(insertion_sort(arr))