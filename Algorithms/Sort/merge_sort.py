
#ideal: Cat mang thanh 2 phan 2 phan cat sao cho 1 mang chi con 1 phan tu
# so sanh phan tu cua mang trai va mang phai
# thuc hien merging va sorting cung 1 luc
# do phuc tap: o(n log(n))
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2  #lam tron
        arr_left = arr[:mid]
        arr_right = arr[mid:]

        merge_sort(arr_left)
        merge_sort(arr_right)
        
        i = j = k = 0
        # #copy data to temp arrays arrLeft[] and arrRight[]
        while i < len(arr_left) and j < len(arr_right):
            print(arr_left[i] , arr_right[j])
            if arr_left[i] < arr_right[j]:
                arr[k] = arr_left[i]
                i += 1
            else:
                arr[k] = arr_right[j]
                j += 1
            k += 1
        
        #check if any element was left
        while i < len(arr_left):
            arr[k] = arr_left[i]
            i += 1
            k += 1
        while j < len(arr_right):
            arr[k] = arr_right[j]
            j += 1
            k += 1

test_array = [5,1,2,4,3]        
merge_sort(test_array)
print(test_array)
