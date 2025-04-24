def merge_sort(array) :
    if len(array) <= 1 :
        return array
    
    m = len(array) // 2

    left = array[:m]
    right = array[m:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted,right_sorted)


def merge(left,right) :
    
    final_list = []

    i , j = 0 , 0

    while i < len(left) and j < len(right) :

        if left[i] < right[j] :

            final_list.append(left[i])

            i += 1
        
        else :

            final_list.append(right[j])

            j += 1
    
    final_list.extend(left[i:])
    final_list.extend(right[j:])

    return final_list


print(merge_sort([10,9,8,7,6,5,4,1,5,6,3,2,1]))