#
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements
                swapped = True
        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

# Example usage:
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    bubble_sort(arr)
    print("Sorted array is:", arr)
    #

