def insertionSort(list): 
    for i in range(1, len(list)):
        value = list[i]
        index = i
        while index > 0 and value < list[index - 1]:
            list[index] = list[index - 1]
            index = index - 1
        list[index] = value
    return list
def binarySearch(sorted_list, target):
    low= 0
    high= len(sorted_list) - 1
    mid= 0
    found= False

    while not found and low <= high:
        mid = (low + high) // 2

        if target == sorted_list[mid]:
            found = True
        elif target > sorted_list[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return found

    

def main():
    list = [23, 87, 45, 12, 67, 34, 98, 56, 3, 72, 41, 89, 25, 64, 77, 9, 50, 31, 92, 18,
            81, 6, 39, 70, 14, 53, 96, 28,62, 47, 85, 11, 33, 78, 20, 59, 94, 36, 8, 71,
            42, 99, 26, 65, 88, 13, 51, 30, 93, 19, 82, 5, 38, 69, 15, 54, 97, 27, 61, 46, 84, 10, 32, 79,
            21, 58, 95,37, 7, 73, 43, 100, 24, 66, 86, 16, 52, 29, 91, 17,
            80, 4, 40, 68, 22, 55, 90, 35, 63, 48, 83, 1, 49, 74, 2, 60, 44, 76, 75, 57]
    print("unsorted list: ", list,"          ")
    sorted_list = insertionSort(list)
    print("sorted list:",sorted_list)
    target = int(input("Enter a target to search for: "))
    found = binarySearch(sorted_list, target)
    if found == True:
        print("Target is found")
    else:
        print("Target not found")

main()
