def bubble_sort_2d(arr):
    n = len(arr)
    m = len(arr[0])
    total_elements= n* m

    for i in range(total_elements - 1):
 #outer loop : goes through all the elements in 2d array
        for j in range(total_elements -1 - i):
            #Inner loop: gies through the elements, reducing the comparison range each time
            #calculte current position in 2D terms
            row1 = j//m
            col1 = j%m
            #Calculate next position (right next to current position)

            row2 = (j+1)// m
            col2 = (j+1)% m

            # Compare and possibly swap elements
            if arr[row1][col1] > arr[row2][col2]:
                #If the current element is greater than the next stepis to swap them
                arr[row1][col2],arr[row2][col2] = arr[row2][col2], arr[row1][col1]
def search_element(arr, element):
    found = False #Initialze a flag to track if the element is found
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == element:
                print(f"Element found at position: row = {i}, column = {j}")
                found = True
                return #exist the function after finding the elements
    if not found:
        print("Element not found in the given array")

    #example usage
arr = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

print(arr)
bubble_sort_2d(arr)
print(arr)

#Search for an element
search = int(input("Enter the element to search: "))
search_element(arr, search)