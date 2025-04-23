"""
BINARY SEARCH
"""

def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2  # 
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None  

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Binary search only works on sorted lists!

print("The length of My list is: " + str(len(my_list)))
print(binary_search(my_list, 5))  # Output: 4 (since 5 is at index 4)
print(binary_search(my_list, 19))  # Output: None (19 not in list)