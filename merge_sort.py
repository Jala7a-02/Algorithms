def bi_search(array,target) :
    l = 0
    r = len(array)-1

    while l <= r :
        m = (l+r) // 2

        if array[m] == target :
            return m
        elif array[m] < target :
            l = m 
        else :
            r = m 
    return -1


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


print(bi_search([1,2,3,4,5,6,7,8,9,10],4))