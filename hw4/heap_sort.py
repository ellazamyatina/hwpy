def heap_sort(arr: list) -> list:
    def heapify(n: int, i: int) -> None:
        largest = i
        left = i * 2 + 1
        right = i * 2 + 2

        if left < n and arr[largest] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            heapify(n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)
    return arr


try:
    in_array = list(map(int, input("Введите числа:\n").split()))
    print(heap_sort(in_array))
except:  # noqa: E722
    print("Введите числа!")
