def insertion_sort(array) :

    N = len(array)

    for i in range(1,N) :

        insert_index = i

        current_value = array.pop(i)

        for j in range(i - 1 , -1 , -1) :

            if array[j] > current_value :

                insert_index = j
                
        array.insert(insert_index,current_value)

    return array

print(insertion_sort([10,9,8,7,6,5,4,3,2,1]))