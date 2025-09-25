def insertionSort(list): 
    for i in range(1, len(list)):
        value = list[i]
        index = i
        while index > 0 and value < list[index - 1]:
            list[index] = list[index - 1]
            index = index - 1
        list[index] = value
    return list
    
def main():
    list = [3,5,7,2,8,16,10,22,24,57,1,15,14,300,53,34,33]
    sorted_list = insertionSort(list)
    print(sorted_list)

main()
