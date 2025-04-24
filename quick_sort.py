def quick_sort(array) :

    if len(array) < 2 :

        return array
    
    else :

        pivot = array.pop()

    left_side = [x for x in array if x <= pivot]
    
    right_side = [x for x in array if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort([10,9,8,7,6,5,4,3,2,1]))