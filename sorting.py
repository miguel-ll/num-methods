# for string sorting
def countSort(arr):
    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]
  
    # Create a count array to store count of individual
    # characters and initialize count array as 0
    count = [0 for i in range(256)]
  
    # For storing the resulting answer since the 
    # string is immutable
    ans = ["" for _ in arr]
  
    # Store count of each character
    for i in arr:
        count[ord(i)] += 1
  
    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i-1]
  
    # Build the output character array
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
  
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans 

def heapify(arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, N, largest)
 
def heapSort(arr):
    N = len(arr)
 
    # Build a maxheap.
    for i in range(N//2 - 1, -1, -1):
        heapify(arr, N, i)
 
    # One by one extract elements
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
