
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:  
          return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
  

    return -1

def bubble_sort(arr):
    size = len(arr)
    
    for i in range(size):
        swapped = False
        
        for j in range(0 , size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
       
    return arr

def selection_sort(arr):
    size = len(arr)
    
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

        
            

    
option = 'Y'

while option == 'Y':
    print("Welcome to my Menu Driven Program")
    print("Choose an Algorithm that you like:")
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Bubble Sort")
    print("4. Selection Sort")
    print("5. Merge Sort")
    print("6. Quick Sort")
    
    choice = int(input("Enter the number of your choice:"))
    
    if choice == 1:
        print("You are using Linear Search")
        size_arr = int(input("Enter the Size of the Array: "))
        my_arr = []
        for i in range(size_arr):
            user_input = int(input(f"Enter element {i + 1}: "))
            my_arr.append(user_input)
        
        key = int(input("Enter the item that you want to search: "))
        result = linear_search(my_arr,key)
        if result == -1:
            print("Item does not exist")
        else:
           print(f"the item is found at index: {result} and the value is: {key}")
           print("-- Linear Search --")
           
    elif choice == 2:
        print("You are using Binary Search")
        size_arr = int(input("Enter the Size of the Array: "))
        print("Enter sorted number of elements")
        my_arr = []
        
        for i in range(size_arr):
            user_input = int(input(f"Enter Element #{i+1}: "))
            my_arr.append(user_input)
             
        target = int(input("Enter the Item that you want to search: "))    
        result = binary_search(my_arr, target)
        
        if result == -1:
            print("The item is not found")
        else:
            print(f"The item is found at index : {result} and the value is {target} ")
        print("-- Binary Search --")
    elif choice == 3:
        print("You are using Bubble Sort")   
        size_arr = int(input("Enter the Size of the Array: "))
        unsorted = []
        my_arr = []
        for i in range(size_arr):
            user_input = int(input(f"Enter Element #{i+1}: "))
            unsorted.append(user_input)
        
        my_arr = bubble_sort(unsorted.copy())
        print(f"Unsorted Array : {unsorted}")
        print(f"After Bubble Sort: {my_arr}")
        
    elif choice == 4: 
        print("You are using Bubble Sort")   
        size_arr = int(input("Enter the Size of the Array: "))
        unsorted = []
        my_arr = []
        for i in range(size_arr):
            user_input = int(input(f"Enter Element #{i+1}: "))
            unsorted.append(user_input)
        
        my_arr = selection_sort(unsorted.copy())
        print(f"Unsorted Array : {unsorted}")
        print(f"After Selection Sort: {my_arr}")
        print("-- Selection Sort -- ")
        
        
        
        
    option = input("Do you want to choose again? (Y/N): ").upper()

    
    
    