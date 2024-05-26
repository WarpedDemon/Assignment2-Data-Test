import os
import random
import time

#SelectionSort
def SelectionSort(Data):

    NumberOfComparisons = 0  # O(1) - Initialization
    for l in range(0, len(Data) - 1):  # O(n) - Outer loop runs 'n' times
        p = l  # O(1)
        for i in range(l+1, len(Data)):  # O(n^2) - Inner loop runs 'n' times in the worst case
            NumberOfComparisons += 1  # O(1)
            if Data[i] < Data[p]:  # O(1)
                p = i # O(1)

        NumberOfComparisons += 1  # O(1)
        if p != l:  # O(1)
            Data[p], Data[l] = Data[l], Data[p]  # O(1)

    # Total time complexity: O(n^2) - Quadratic
    # Total space complexity: O(1) - Constant
    return Data, NumberOfComparisons

def SelectionSortHandler(Data):

    StartTime = time.time()  # O(1) - Start time measurement
    Data, NumberOfComparisons = SelectionSort(Data)  # O(n^2) - Perform selection sort
    EndTime = time.time()  # O(1) - End time measurement
    FinalElapsedTime = EndTime - StartTime  # O(1) - Calculate elapsed time

    # Output results
    return "Selection Sort | " + str(len(Data)) + str(" | ") + str(NumberOfComparisons) + " | " + str(FinalElapsedTime*1000) + " (ms.)", NumberOfComparisons, FinalElapsedTime*1000


#InsertionSort
def InsertionSort(Data):

    NumberOfComparisons = 0  # O(1) - Initialization
    for l in range(1, len(Data)):  # O(n) - Outer loop runs 'n-1' times
        current_element = Data[l]  # O(1)
        j = l - 1  # O(1)
        while j >= 0 and Data[j] > current_element:  # O(n^2) - Inner loop may run up to 'n' times in the worst case
            Data[j + 1] = Data[j]  # O(1)
            j -= 1 # O(1)
            NumberOfComparisons += 1  # O(1)

        NumberOfComparisons += 1  # O(1)
        Data[j + 1] = current_element  # O(1)

    # Total time complexity: O(n^2) - Quadratic
    # Total space complexity: O(1) - Constant
    return Data, NumberOfComparisons

def InsertionSortHandler(Data):

    StartTime = time.time()  # O(1) - Start time measurement
    Data, NumberOfComparisons = InsertionSort(Data)  # O(n^2) - Perform insertion sort
    EndTime = time.time()  # O(1) - End time measurement
    FinalElapsedTime = EndTime - StartTime  # O(1) - Calculate elapsed time

    # Output results
    return "Insertion Sort | " + str(len(Data)) + str(" | ") + str(NumberOfComparisons) + " | " + str(FinalElapsedTime*1000) + " (ms.)", NumberOfComparisons, FinalElapsedTime*1000


# Merge Sort
def MergeSort(Data):

    # Helper function to merge two sorted arrays
    def Merge(left, right):
        result = []  # O(1)
        left_index = right_index = 0  # O(1)
        comparisons = 0  # O(1)

        # Merge the two arrays into a single sorted array
        while left_index < len(left) and right_index < len(right):  # O(n)
            comparisons += 1  # O(1)
            if left[left_index] < right[right_index]:  # O(1)
                result.append(left[left_index])  # O(1)
                left_index += 1  # O(1)
            else:
                result.append(right[right_index])  # O(1)
                right_index += 1  # O(1)

        # Append any remaining elements from left or right (if any)
        result.extend(left[left_index:])  # O(n)
        result.extend(right[right_index:])  # O(n)

        return result, comparisons

    # Main MergeSort function
    if len(Data) <= 1:  # O(1)
        return Data, 0  # O(1)

    # Divide the array into two halves and recursively sort them
    mid = len(Data) // 2  # O(1)
    left = Data[:mid]  # O(n)
    right = Data[mid:]  # O(n)

    left, left_comparisons = MergeSort(left)  # T(n/2)
    right, right_comparisons = MergeSort(right)  # T(n/2)
    merge_result, merge_comparisons = Merge(left, right)  # O(n)

    # Calculate total comparisons and return the sorted array
    total_comparisons = left_comparisons + right_comparisons + merge_comparisons  # O(1)
    return merge_result, total_comparisons  # O(1)

def MergeSortHandler(Data):

    StartTime = time.time()  # O(1) - Start time measurement
    Data, NumberOfComparisons = MergeSort(Data)  # O(n log n) - Perform merge sort
    EndTime = time.time()  # O(1) - End time measurement
    FinalElapsedTime = EndTime - StartTime  # O(1) - Calculate elapsed time

    # Output results
    return "Merge Sort | " + str(len(Data)) + str(" | ") + str(NumberOfComparisons) + " | " + str(FinalElapsedTime*1000) + " (ms.)", NumberOfComparisons, FinalElapsedTime*1000


# Quick Sort
def QuickSort(Data):

    # Main QuickSort function
    if len(Data) <= 1:  # O(1)
        return Data, 0  # O(1)

    pivot = Data[len(Data) // 2]  # O(1) - Choosing a pivot element
    left = [x for x in Data if x < pivot]  # O(n) - Elements smaller than the pivot
    middle = [x for x in Data if x == pivot]  # O(n) - Elements equal to the pivot
    right = [x for x in Data if x > pivot]  # O(n) - Elements greater than the pivot

    # Recursively sort left and right sublists
    sorted_left, left_comparisons = QuickSort(left)  # T(n/2)
    sorted_right, right_comparisons = QuickSort(right)  # T(n/2)

    # Counting total comparisons
    total_comparisons = len(Data) - 1 + left_comparisons + right_comparisons  # O(n)

    return sorted_left + middle + sorted_right, total_comparisons  # T(n) = 2T(n/2) + O(n)

def QuickSortHandler(Data):

    StartTime = time.time()  # O(1) - Start time measurement
    Data, NumberOfComparisons = QuickSort(Data)  # T(n) = 2T(n/2) + O(n) - Perform quicksort
    EndTime = time.time()  # O(1) - End time measurement
    FinalElapsedTime = EndTime - StartTime  # O(1) - Calculate elapsed time

    # Output results
    return "Quick Sort | " + str(len(Data)) + str(" | ") + str(NumberOfComparisons) + " | " + str(FinalElapsedTime*1000) + " (ms.)", NumberOfComparisons, FinalElapsedTime*1000


# Heapify
def Heapify(Data, n, i, NumberOfComparisons):

    largest = i  # O(1)
    l = 2 * i + 1  # O(1)
    r = 2 * i + 2  # O(1)

    NumberOfComparisons += 1  # O(1)
    if l < n and Data[largest] < Data[l]:  # O(1)
        largest = l  # O(1)

    if r < n and Data[largest] < Data[r]:  # O(1)
        largest = r  # O(1)

    if largest != i:  # O(1)
        Data[i], Data[largest] = Data[largest], Data[i]  # O(1)
        NumberOfComparisons += 1  # O(1)

        # Total time complexity: O(log(n))
        # Total space complexity: O(1)
        Heapify(Data, n, largest, NumberOfComparisons)  # O(log(n))

def HeapSort(Data):

    n = len(Data)  # O(1)
    NumberOfComparisons = 0 # O(1)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):  # O(n)
        Heapify(Data, n, i, NumberOfComparisons)  # O(log(n))

    # Extract elements one by one
    for i in range(n-1, 0, -1):  # O(n)
        Data[i], Data[0] = Data[0], Data[i]  # O(1)
        NumberOfComparisons += 1  # O(1)
        Heapify(Data, i, 0, NumberOfComparisons)  # O(log(n))

    # Total time complexity: O(n*log(n))
    # Total space complexity: O(1)
    return Data, NumberOfComparisons  # O(1)

def HeapSortHandler(Data):

    StartTime = time.time()  # O(1) - Start time measurement
    Data, NumberOfComparisons = HeapSort(Data)  # O(n*log(n)) - Perform heap sort
    EndTime = time.time()  # O(1) - End time measurement
    FinalElapsedTime = EndTime - StartTime  # O(1) - Calculate elapsed time

    # Output results
    return "Heap Sort | " + str(len(Data)) + str(" | ") + str(NumberOfComparisons) + " | " + str(FinalElapsedTime*1000) + " (ms.)", NumberOfComparisons, FinalElapsedTime*1000


#Counting Sort
def CountingSort(Data):

    UnsortedArray = Data  # O(1)
    FinalArray = [0] * len(UnsortedArray)  # Initialize FinalArray with zeros # O(n)
    NumberOfComparisons = 0 # O(1)

    # Find the maximum and minimum elements in the array
    max_element = max(UnsortedArray)  # O(n)
    min_element = min(UnsortedArray)  # O(n)

    # Adjust the range to include negative numbers
    range_of_numbers = max_element - min_element + 1  # O(1)

    # Initialize count array with zeros
    count = [0] * range_of_numbers  # O(n)

    # Count occurrences of each element
    for num in UnsortedArray:  # O(n)
        count[num - min_element] += 1  # O(1)

    # Update count array to contain actual positions of elements
    for i in range(1, len(count)):  # O(n)
        count[i] += count[i - 1]  # O(1)

    # Place elements in the sorted array
    for num in reversed(UnsortedArray):  # O(n)
        FinalArray[count[num - min_element] - 1] = num  # O(1)
        count[num - min_element] -= 1  # O(1)
        NumberOfComparisons += 1 # O(1)

    return FinalArray, NumberOfComparisons

def CountingSortHandler(Data):

    StartTime = time.time()  # O(1) - Start time measurement
    Data, NumberOfComparisons = CountingSort(Data)  # O(n) - Perform counting sort
    EndTime = time.time()  # O(1) - End time measurement
    FinalElapsedTime = EndTime - StartTime  # O(1) - Calculate elapsed time

    # Output results
    return "Counting Sort | " + str(len(Data)) + str(" | ") + str(NumberOfComparisons) + " | " + str(FinalElapsedTime*1000) + " (ms.)", NumberOfComparisons, FinalElapsedTime*1000


def MenuOption7():

    return False # O(1)


def MenuOption1():

    os.system('clear')  # O(1) - Clear the console
    Menu1Active = True  # O(1) - Set Menu1Active to True
    while Menu1Active:  # O(1) - While loop condition
        Data = []  # O(1) - Initialize an empty array

        RequestLoopCount = input("Please enter the number of elements you would like generated in the array: ")  # O(1) - Get user input
        Count = 0  # O(1) - Initialize a counter
        while int(RequestLoopCount) > 0:  # O(1) - While loop based on user input
            NewItemToAddToArray = random.randint(0, 100)  # O(1) - Generate random number
            Data.insert(int(Count), NewItemToAddToArray)  # O(1) - Insert element into array
            RequestLoopCount = int(RequestLoopCount) - 1  # O(1) - Decrement loop count
        print("Your numbers are: ", Data)  # O(1) - Print array

        if Menu1Active:  # O(1) - Check if Menu1Active is True
            print("------------------------------------------")  # O(1) - Print header
            print("Please Pick One Of The Following Options: ")  # O(1) - Print options
            print("    - Option 1 : Selection Sort")  # O(1) - Print option 1
            print("    - Option 2 : Insertion Sort")  # O(1) - Print option 2
            print("    - Option 3 : Merge Sort")  # O(1) - Print option 3
            print("    - Option 4 : Quick Sort")  # O(1) - Print option 4
            print("    - Option 5 : Heap Sort")  # O(1) - Print option 5
            print("    - Option 6 : Counting Sort")  # O(1) - Print option 6
            print("    - Option 7 : Return To Main Menu")  # O(1) - Print option 7
            print("------------------------------------------")  # O(1) - Print separator

            SecondMenuInput = input("Please enter a menu option number: ")  # O(1) - Get user input

            if SecondMenuInput == "1":  # O(1) - Check if option 1 is chosen
                print("------------------------------------------")  # O(1) - Print header
                print("Sorting algorithm name | Array size | Num. of Comparisons | Run time (in ms.)")
                print(SelectionSortHandler(Data)[0])  # O(1) - Perform selection sort
                Menu1Active = False  # O(1) - Set Menu1Active to False
                Ready = input("Press Any Key To Return To The Main Menu")  # O(1) - Get user input
            if SecondMenuInput == "2":  # O(1) - Check if option 2 is chosen
                print("------------------------------------------")  # O(1) - Print header
                print("Sorting algorithm name | Array size | Num. of Comparisons | Run time (in ms.)")
                print(InsertionSortHandler(Data)[0])  # O(1) - Perform insertion sort
                Menu1Active = False  # O(1) - Set Menu1Active to False
                Ready = input("Press Any Key To Return To The Main Menu")  # O(1) - Get user input
            if SecondMenuInput == "3":  # O(1) - Check if option 3 is chosen
                print("------------------------------------------")  # O(1) - Print header
                print("Sorting algorithm name | Array size | Num. of Comparisons | Run time (in ms.)")
                print(MergeSortHandler(Data)[0])  # O(1) - Perform merge sort
                Menu1Active = False  # O(1) - Set Menu1Active to False
                Ready = input("Press Any Key To Return To The Main Menu")  # O(1) - Get user input
            if SecondMenuInput == "4":  # O(1) - Check if option 4 is chosen
                print("------------------------------------------")  # O(1) - Print header
                print("Sorting algorithm name | Array size | Num. of Comparisons | Run time (in ms.)")
                print(QuickSortHandler(Data)[0])  # O(1) - Perform quick sort
                Menu1Active = False  # O(1) - Set Menu1Active to False
                Ready = input("Press Any Key To Return To The Main Menu")  # O(1) - Get user input
            if SecondMenuInput == "5":  # O(1) - Check if option 5 is chosen
                print("------------------------------------------")  # O(1) - Print header
                print("Sorting algorithm name | Array size | Num. of Comparisons | Run time (in ms.)")
                print(HeapSortHandler(Data)[0])  # O(1) - Perform heap sort
                Menu1Active = False  # O(1) - Set Menu1Active to False
                Ready = input("Press Any Key To Return To The Main Menu")  # O(1) - Get user input
            if SecondMenuInput == "6":  # O(1) - Check if option 6 is chosen
                print("------------------------------------------")  # O(1) - Print header
                print("Sorting algorithm name | Array size | Num. of Comparisons | Run time (in ms.)")
                print(CountingSortHandler(Data)[0])  # O(1) - Perform counting sort
                Menu1Active = False  # O(1) - Set Menu1Active to False
                Ready = input("Press Any Key To Return To The Main Menu")  # O(1) - Get user input
            if SecondMenuInput == "7":  # O(1) - Check if option 7 is chosen
                Menu1Active = MenuOption7()  # O(1) - Set Menu1Active to False


def MenuOption2():

    os.system('clear')  # O(1) - Clear the console
    Menu2Active = True  # O(1) - Set Menu2Active to True
    while Menu2Active:  # O(1) - While loop condition
        Data = []  # O(1) - Initialize an empty array
        RequestLoopCount = input("Please enter the number of elements you would like generated in the array: ")  # O(1) - Get user input
        Count = 0  # O(1) - Initialize a counter
        while int(RequestLoopCount) > 0:  # O(1) - While loop based on user input
            NewItemToAddToArray = random.randint(0, 100)  # O(1) - Generate random number
            Data.insert(int(Count), NewItemToAddToArray)  # O(1) - Insert element into array
            RequestLoopCount = int(RequestLoopCount) - 1  # O(1) - Decrement loop count
        print("Your numbers are: ", Data)  # O(1) - Print array

        if Menu2Active:  # O(1) - Check if Menu2Active is True
            # Print the return data for each sorting algorithm
            print("------------------------------------------")  # O(1) - Print header
            print("Sorting algorithm name | Array size | Num. of Comparisons | Run time (in ms.)")
            print(SelectionSortHandler(Data)[0])  # O(1) - Print return data for selection sort
            print(InsertionSortHandler(Data)[0])  # O(1) - Print return data for insertion sort
            print(MergeSortHandler(Data)[0])  # O(1) - Print return data for merge sort
            print(QuickSortHandler(Data)[0])  # O(1) - Print return data for quick sort
            print(HeapSortHandler(Data)[0])  # O(1) - Print return data for heap sort
            print(CountingSortHandler(Data)[0])  # O(1) - Print return data for counting sort
            print("------------------------------------------")  # O(1) - Print header
            Menu2Active = False  # O(1) - Set Menu2Active to False

        Ready = input("Press Any Key To Return To The Main Menu")  # O(1) - Get user input


def MenuOption3():

    return False # O(1)


def MenuOption4():
    # Initialize arrays to store comparison and time data for different algorithms and array sizes
    Column2000Value = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    Column1000Value = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    Column800Value = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    Column400Value = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    Column200Value = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    Column100Value = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    DataStudyDataSize = 10  # Set the size of the data to study
    DataStudyDataCounter = DataStudyDataSize

    os.system('clear')  # O(1)
    Menu4Active = True  # O(1)

    for IterationCount in range(DataStudyDataCounter):  # Loop through the data study size
        # Reset data and loop count
        Data = []  # O(1)
        RequestLoopCount = 2000  # O(1)
        Count = 0  # O(1)

        # Generate random numbers
        while int(RequestLoopCount) > 0:  # O(1)
            NewItemToAddToArray = random.randint(0, 100)  # O(1)
            Data.insert(int(Count), NewItemToAddToArray)  # O(1)
            RequestLoopCount = int(RequestLoopCount) - 1  # O(1)

        # Test Algorithms and Collect Data
        Column2000Value[0][0] += SelectionSortHandler(Data)[1]  # O(1)
        Column2000Value[0][1] += SelectionSortHandler(Data)[2]  # O(1)

        Column2000Value[1][0] += InsertionSortHandler(Data)[1]  # O(1)
        Column2000Value[1][1] += InsertionSortHandler(Data)[2]  # O(1)

        Column2000Value[2][0] += MergeSortHandler(Data)[1]  # O(1)
        Column2000Value[2][1] += MergeSortHandler(Data)[2]  # O(1)

        Column2000Value[3][0] += QuickSortHandler(Data)[1]  # O(1)
        Column2000Value[3][1] += QuickSortHandler(Data)[2]  # O(1)

        Column2000Value[4][0] += HeapSortHandler(Data)[1]  # O(1)
        Column2000Value[4][1] += HeapSortHandler(Data)[2]  # O(1)

        Column2000Value[5][0] += CountingSortHandler(Data)[1]  # O(1)
        Column2000Value[5][1] += CountingSortHandler(Data)[2]  # O(1)

        #print("Data Testing Done For 2000")

        # Reset Data
        Data = []  # O(1)
        RequestLoopCount = 1000  # O(1)
        Count = 0  # O(1)

        # Generate Numbers
        while int(RequestLoopCount) > 0:  # O(1)
            NewItemToAddToArray = random.randint(0, 100)  # O(1)
            Data.insert(int(Count), NewItemToAddToArray)  # O(1)
            RequestLoopCount = int(RequestLoopCount) - 1  # O(1)

        # Test Algorithms and Collect Data
        Column1000Value[0][0] += SelectionSortHandler(Data)[1]  # O(1)
        Column1000Value[0][1] += SelectionSortHandler(Data)[2]  # O(1)

        Column1000Value[1][0] += InsertionSortHandler(Data)[1]  # O(1)
        Column1000Value[1][1] += InsertionSortHandler(Data)[2]  # O(1)

        Column1000Value[2][0] += MergeSortHandler(Data)[1]  # O(1)
        Column1000Value[2][1] += MergeSortHandler(Data)[2]  # O(1)

        Column1000Value[3][0] += QuickSortHandler(Data)[1]  # O(1)
        Column1000Value[3][1] += QuickSortHandler(Data)[2]  # O(1)

        Column1000Value[4][0] += HeapSortHandler(Data)[1]  # O(1)
        Column1000Value[4][1] += HeapSortHandler(Data)[2]  # O(1)

        Column1000Value[5][0] += CountingSortHandler(Data)[1]  # O(1)
        Column1000Value[5][1] += CountingSortHandler(Data)[2]  # O(1)

        #print("Data Testing Done For 1000")

        # Reset Data
        Data = []  # O(1)
        RequestLoopCount = 800  # O(1)
        Count = 0  # O(1)
                
        # Generate Numbers
        while int(RequestLoopCount) > 0:  # O(1)
            NewItemToAddToArray = random.randint(0, 100)  # O(1)
            Data.insert(int(Count), NewItemToAddToArray)  # O(1)
            RequestLoopCount = int(RequestLoopCount) - 1  # O(1)

        # Test Algorithms and Collect Data
        Column800Value[0][0] += SelectionSortHandler(Data)[1]  # O(1)
        Column800Value[0][1] += SelectionSortHandler(Data)[2]  # O(1)

        Column800Value[1][0] += InsertionSortHandler(Data)[1]  # O(1)
        Column800Value[1][1] += InsertionSortHandler(Data)[2]  # O(1)

        Column800Value[2][0] += MergeSortHandler(Data)[1]  # O(1)
        Column800Value[2][1] += MergeSortHandler(Data)[2]  # O(1)

        Column800Value[3][0] += QuickSortHandler(Data)[1]  # O(1)
        Column800Value[3][1] += QuickSortHandler(Data)[2]  # O(1)

        Column800Value[4][0] += HeapSortHandler(Data)[1]  # O(1)
        Column800Value[4][1] += HeapSortHandler(Data)[2]  # O(1)
                                
        Column800Value[5][0] += CountingSortHandler(Data)[1]  # O(1)
        Column800Value[5][1] += CountingSortHandler(Data)[2]  # O(1)

        #print("Data Testing Done For 800")

        #Reset Data
        Data = [] # O(1)
        RequestLoopCount = 400 # O(1)
        Count = 0 # O(1)

        #Generate Numbers
        while int(RequestLoopCount) > 0: # O(1)
            NewItemToAddToArray = random.randint(0,100) # O(1)
            Data.insert(int(Count), NewItemToAddToArray) # O(1)
            RequestLoopCount = int(RequestLoopCount) - 1 # O(1)

        #Test Algorithms and Collect Data
        Column400Value[0][0] += SelectionSortHandler(Data)[1] # O(1)
        Column400Value[0][1] += SelectionSortHandler(Data)[2] # O(1)

        Column400Value[1][0] += InsertionSortHandler(Data)[1] # O(1)
        Column400Value[1][1] += InsertionSortHandler(Data)[2] # O(1)

        Column400Value[2][0] += MergeSortHandler(Data)[1] # O(1)
        Column400Value[2][1] += MergeSortHandler(Data)[2] # O(1)

        Column400Value[3][0] += QuickSortHandler(Data)[1] # O(1)
        Column400Value[3][1] += QuickSortHandler(Data)[2] # O(1)

        Column400Value[4][0] += HeapSortHandler(Data)[1] # O(1)
        Column400Value[4][1] += HeapSortHandler(Data)[2] # O(1)
                    
        Column400Value[5][0] += CountingSortHandler(Data)[1] # O(1)
        Column400Value[5][1] += CountingSortHandler(Data)[2] # O(1)

        #print("Data Testing Done For 400")

        #Reset Data
        Data = [] # O(1)
        RequestLoopCount = 200 # O(1)
        Count = 0 # O(1)

        #Generate Numbers
        while int(RequestLoopCount) > 0: # O(1)
            NewItemToAddToArray = random.randint(0,100) # O(1)
            Data.insert(int(Count), NewItemToAddToArray) # O(1)
            RequestLoopCount = int(RequestLoopCount) - 1 # O(1)

        #Test Algorithms and Collect Data
        Column200Value[0][0] += SelectionSortHandler(Data)[1] # O(1)
        Column200Value[0][1] += SelectionSortHandler(Data)[2] # O(1)

        Column200Value[1][0] += InsertionSortHandler(Data)[1] # O(1)
        Column200Value[1][1] += InsertionSortHandler(Data)[2] # O(1)

        Column200Value[2][0] += MergeSortHandler(Data)[1] # O(1)
        Column200Value[2][1] += MergeSortHandler(Data)[2] # O(1)

        Column200Value[3][0] += QuickSortHandler(Data)[1] # O(1)
        Column200Value[3][1] += QuickSortHandler(Data)[2] # O(1)

        Column200Value[4][0] += HeapSortHandler(Data)[1] # O(1)
        Column200Value[4][1] += HeapSortHandler(Data)[2] # O(1)
                    
        Column200Value[5][0] += CountingSortHandler(Data)[1] # O(1)
        Column200Value[5][1] += CountingSortHandler(Data)[2] # O(1)

        #print("Data Testing Done For 200")

        #Reset Data
        Data = [] # O(1)
        RequestLoopCount = 100 # O(1)
        Count = 0 # O(1)
        
        #Generate Numbers
        while int(RequestLoopCount) > 0: # O(1)
            NewItemToAddToArray = random.randint(0,100) # O(1)
            Data.insert(int(Count), NewItemToAddToArray) # O(1)
            RequestLoopCount = int(RequestLoopCount) - 1 # O(1)

        #Test Algorithms and Collect Data
        Column100Value[0][0] += SelectionSortHandler(Data)[1] # O(1)
        Column100Value[0][1] += SelectionSortHandler(Data)[2] # O(1)

        Column100Value[1][0] += InsertionSortHandler(Data)[1] # O(1)
        Column100Value[1][1] += InsertionSortHandler(Data)[2] # O(1)

        Column100Value[2][0] += MergeSortHandler(Data)[1] # O(1)
        Column100Value[2][1] += MergeSortHandler(Data)[2] # O(1)

        Column100Value[3][0] += QuickSortHandler(Data)[1] # O(1)
        Column100Value[3][1] += QuickSortHandler(Data)[2] # O(1)

        Column100Value[4][0] += HeapSortHandler(Data)[1] # O(1)
        Column100Value[4][1] += HeapSortHandler(Data)[2] # O(1)
                    
        Column100Value[5][0] += CountingSortHandler(Data)[1] # O(1)
        Column100Value[5][1] += CountingSortHandler(Data)[2] # O(1)

        print("Data Testing Running: ", DataStudyDataCounter) # O(1)
    
        DataStudyDataCounter = int(DataStudyDataCounter) - 1 # O(1)

    print("Data Loading Completed ... Printing Averaged Results") # O(1)

    #Create Comparisons Final Table
    ComparisonsFinalTable = [[0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0]]

    ComparisonsFinalTable[0][0] = Column100Value[0][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[0][1] = Column200Value[0][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[0][2] = Column400Value[0][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[0][3] = Column800Value[0][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[0][4] = Column1000Value[0][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[0][5] = Column2000Value[0][0] / DataStudyDataSize  # O(1)

    ComparisonsFinalTable[1][0] = Column100Value[1][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[1][1] = Column200Value[1][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[1][2] = Column400Value[1][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[1][3] = Column800Value[1][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[1][4] = Column1000Value[1][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[1][5] = Column2000Value[1][0] / DataStudyDataSize  # O(1)

    ComparisonsFinalTable[2][0] = Column100Value[2][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[2][1] = Column200Value[2][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[2][2] = Column400Value[2][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[2][3] = Column800Value[2][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[2][4] = Column1000Value[2][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[2][5] = Column2000Value[2][0] / DataStudyDataSize  # O(1)

    ComparisonsFinalTable[3][0] = Column100Value[3][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[3][1] = Column200Value[3][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[3][2] = Column400Value[3][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[3][3] = Column800Value[3][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[3][4] = Column1000Value[3][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[3][5] = Column2000Value[3][0] / DataStudyDataSize  # O(1)

    ComparisonsFinalTable[4][0] = Column100Value[4][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[4][1] = Column200Value[4][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[4][2] = Column400Value[4][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[4][3] = Column800Value[4][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[4][4] = Column1000Value[4][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[4][5] = Column2000Value[4][0] / DataStudyDataSize  # O(1)

    ComparisonsFinalTable[5][0] = Column100Value[5][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[5][1] = Column200Value[5][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[5][2] = Column400Value[5][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[5][3] = Column800Value[5][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[5][4] = Column1000Value[5][0] / DataStudyDataSize  # O(1)
    ComparisonsFinalTable[5][5] = Column2000Value[5][0] / DataStudyDataSize  # O(1)

    # Write Out Data For Average Comparisons

    # Print the header of the table
    print("Sorting Algorithm | n = 100 | n = 200 | n = 400 | n = 800 | n = 1000 | n = 2000")  # O(1)

    # Initialize a variable to track the current row in ComparisonsFinalTable
    ComparisonsFinalTableTrigger = 0  # O(1)

    # Iterate over each row in ComparisonsFinalTable
    for List in ComparisonsFinalTable:  # O(n), where n is the number of rows in ComparisonsFinalTable
        # Determine the sorting algorithm for the current row
        if ComparisonsFinalTableTrigger == 0:  # O(1)
            FinalString = "Selection Sort: "  # O(1)
        if ComparisonsFinalTableTrigger == 1:  # O(1)
            FinalString = "Insertion Sort: "  # O(1)
        if ComparisonsFinalTableTrigger == 2:  # O(1)
            FinalString = "Merge Sort: "  # O(1)
        if ComparisonsFinalTableTrigger == 3:  # O(1)
            FinalString = "Quick Sort: "  # O(1)
        if ComparisonsFinalTableTrigger == 4:  # O(1)
            FinalString = "Heap Sort: "  # O(1)
        if ComparisonsFinalTableTrigger == 5:  # O(1)
            FinalString = "Counting Sort: "  # O(1)
        
        # Append the number of comparisons for each input size to the final string
        for Item in List:  # O(n), where n is the number of elements in the current row
            FinalString = FinalString + " | " + str(Item)  # O(1)
        
        # Print the final string for the current sorting algorithm
        print(FinalString)  # O(1)

        ComparisonsFinalTableTrigger += 1  # O(1)

    #Print A Space
    print("------------------------------------------") # O(1)

    # Create Average Time Taken Final Table
    AverageTimeFinalTable = [[0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]]

    AverageTimeFinalTable[0][0] = Column100Value[0][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[0][1] = Column200Value[0][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[0][2] = Column400Value[0][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[0][3] = Column800Value[0][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[0][4] = Column1000Value[0][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[0][5] = Column2000Value[0][1] / DataStudyDataSize  # O(1)

    AverageTimeFinalTable[1][0] = Column100Value[1][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[1][1] = Column200Value[1][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[1][2] = Column400Value[1][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[1][3] = Column800Value[1][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[1][4] = Column1000Value[1][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[1][5] = Column2000Value[1][1] / DataStudyDataSize  # O(1)

    AverageTimeFinalTable[2][0] = Column100Value[2][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[2][1] = Column200Value[2][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[2][2] = Column400Value[2][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[2][3] = Column800Value[2][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[2][4] = Column1000Value[2][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[2][5] = Column2000Value[2][1] / DataStudyDataSize  # O(1)

    AverageTimeFinalTable[3][0] = Column100Value[3][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[3][1] = Column200Value[3][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[3][2] = Column400Value[3][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[3][3] = Column800Value[3][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[3][4] = Column1000Value[3][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[3][5] = Column2000Value[3][1] / DataStudyDataSize  # O(1)

    AverageTimeFinalTable[4][0] = Column100Value[4][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[4][1] = Column200Value[4][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[4][2] = Column400Value[4][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[4][3] = Column800Value[4][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[4][4] = Column1000Value[4][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[4][5] = Column2000Value[4][1] / DataStudyDataSize  # O(1)

    AverageTimeFinalTable[5][0] = Column100Value[5][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[5][1] = Column200Value[5][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[5][2] = Column400Value[5][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[5][3] = Column800Value[5][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[5][4] = Column1000Value[5][1] / DataStudyDataSize  # O(1)
    AverageTimeFinalTable[5][5] = Column2000Value[5][1] / DataStudyDataSize  # O(1)

    # Write Out Data For Average Time Taken
    print("Sorting Algorithm | n = 100 | n = 200 | n = 400 | n = 800 | n = 1000 | n = 2000")  # O(1)

    AverageTimeFinalTableTrigger = 0  # O(1)
    for List in AverageTimeFinalTable:  # O(n), where n is the number of rows in AverageTimeFinalTable
        if AverageTimeFinalTableTrigger == 0:  # O(1)
            FinalString = "Selection Sort: "  # O(1)
        if AverageTimeFinalTableTrigger == 1:  # O(1)
            FinalString = "Insertion Sort: "  # O(1)
        if AverageTimeFinalTableTrigger == 2:  # O(1)
            FinalString = "Merge Sort: "  # O(1)
        if AverageTimeFinalTableTrigger == 3:  # O(1)
            FinalString = "Quick Sort: "  # O(1)
        if AverageTimeFinalTableTrigger == 4:  # O(1)
            FinalString = "Heap Sort: "  # O(1)
        if AverageTimeFinalTableTrigger == 5:  # O(1)
            FinalString = "Counting Sort: "  # O(1)
        
        for Item in List:  # O(m), where m is the number of elements in the current row
            FinalString = FinalString + " | " + str(Item)  # O(1)
        
        print(FinalString)  # O(1)

        AverageTimeFinalTableTrigger += 1  # O(1)

    Ready = input("Press Any Key To Return To The Main Menu")  # O(1)

    Menu4Active = False # O(1)

def MainMenu(Active):

    while Active:  # O(1) - While loop condition
        os.system('clear')  # O(1) - Clear the console

        # Print the main menu options
        print("Please Pick One Of The Following Options: ")  # O(1)
        print("    - Option 1 : Test One Algorithm")  # O(1)
        print("    - Option 2 : Test All Algorithms")  # O(1)
        print("    - Option 3 : Exit Program")  # O(1)
        print("    - Option 4 : Data Study")  # O(1)
        print("------------------------------------------")  # O(1)

        FirstMenuInput = input("Please enter a menu option number: ")  # O(1)

        if FirstMenuInput == "1":  # O(1) - Check if option 1 is chosen
            MenuOption1()  # O(1) - Call MenuOption1 function
            FirstMenuInput = None  # O(1) - Reset FirstMenuInput
        if FirstMenuInput == "2":  # O(1) - Check if option 2 is chosen
            MenuOption2()  # O(1) - Call MenuOption2 function
            FirstMenuInput = None  # O(1) - Reset FirstMenuInput
        if FirstMenuInput == "3":  # O(1) - Check if option 3 is chosen
            Active = MenuOption3()  # O(1) - Call MenuOption3 function and update Active
        if FirstMenuInput == "4":  # O(1) - Check if option 4 is chosen
            MenuOption4()  # O(1) - Call MenuOption4 function

MainMenu(True) # O(1)