def selection_sort(array):

    n = len(array)

    for i in range(n - 1) :

        min_index = i 

        for j in range(i+1,n) :

            if array[j] < array[min_index] :

                min_index = j

        min_value = array.pop(min_index)

        array.insert(i,min_value)
    
    return array

print(selection_sort([2,5,1,5,2,3,2,10,35,35,23,12,65,6]))