def binarySearch(list, target):
    low= 0
    high= len(list) - 1
    mid= 0
    found= False

    while not found and low <= high:
        mid = (low + high) // 2

        if target == list[mid]:
            found = True
        elif target > list[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return found

def main():
    list = [2,4,5,6,7,8,9,10,22,25]
    target = 2
    found = binarySearch(list, target)
    print(found)

main()
