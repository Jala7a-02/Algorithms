def binary_search(array , target) :

    lowest_index = 0
    highest_index = len(array) - 1

    while lowest_index <= highest_index :

        middle_index = (lowest_index + highest_index) // 2

        if array[middle_index] == target :

            return middle_index
        
        elif array[middle_index] < target :

            lowest_index = middle_index + 1

        else :

            highest_index = middle_index - 1

    return -1
        

print(binary_search([1,2,3,4,5,6,7,8,9,10],4))