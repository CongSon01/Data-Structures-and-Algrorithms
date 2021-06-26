
#độ phức tạp: o(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#Có thể đạt được trường hợp độ phức tạp o(n)
#optimizes on bubble sort
def bubble_sort_optimized(arr):
    has_swapped = True

    n_of_iterations = 0

    while has_swapped:
        has_swapped = False
        for i in range(len(arr) - n_of_iterations - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                has_swapped = True
        n_of_iterations += 1
    return arr


arr = [5,1,3,2,4]
print(bubble_sort_optimized(arr))
