def largest_sum_of_non_adjacent_numbers(array=[]):
    incl = 0
    excl = 0
    excl_new = None

    for num in array:
        if incl > excl:
            excl_new = incl
        else:
            excl_new = excl
        
        incl = excl + num
        excl = excl_new
    
    return incl if incl > excl else excl

print( largest_sum_of_non_adjacent_numbers([2, 4, 6, 2, 5]) )
print( largest_sum_of_non_adjacent_numbers([5, 1, 1, 5]) )