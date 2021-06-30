
'''
B1: Build a max heap from the input data (parent node is always greater than or equal to child nodes)
B2: Swap first and last node and delete the last node from heap
B3: heapify
'''
def heapify(arr, heap_size, root_index):
    largest = root_index
    left_child = (2*root_index) + 1
    right_child = (2*root_index) + 2

    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        heapify(arr, heap_size, largest)

def heap_sort(arr):
    n = len(arr)

    #maxheap
    #i: chay tu n -> 0
    for i in range(n, -1 , -1):
        heapify(arr, n, i)
    
    #move the root of the max heap to the end of
    for i in range(n -1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

random_list_of_nums = [35, 12, 43, 8, 51]
heap_sort(random_list_of_nums)
print(random_list_of_nums)