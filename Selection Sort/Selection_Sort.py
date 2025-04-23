"""
SELECTION SORT
"""

def findSmallest(arr):
    smallest = arr[0] #Stores the smallest value
    smallest_index = 0 #Stores the index of the small value
    for i in range(1, len(arr)): #Loop through the array from 2nd index to the end
        if arr[i] < smallest: #Check if current element is smaller than smallest
            smallest = arr[i] #If the current element is smaller, updates smallest to this new value.
            smallest_index = i #Update the index of the new smallest element.
    return smallest_index # Returns smallest value
        
def selectionSort(arr): #sorts arry
    newArr = [] #Initializes an empty array
    for i in range(len(arr)): #Loops according to the lenght of the array
        smallest = findSmallest(arr) #Get the index of the smallest remaining element in array
        newArr.append(arr.pop(smallest))#Finds the smallest element in the arry & adds it into the newArr
    return newArr
    
print(selectionSort([5,3,6,2,10]))

