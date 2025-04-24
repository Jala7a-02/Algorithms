def bubble_sort(array) :

    swap = True

    end = len(array)

    while swap :

        swap = False

        for i in range(1,end) :

            if array[i] < array[i-1] :

                array [i-1] , array[i] = array[i] , array[i-1]

                swap = True

        end -= 1
        
    return array

print(bubble_sort([1,7,2,95,2,4,1,2,87,12,10]))