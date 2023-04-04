# given an array of integers. Calculate sum and multiplication of elements.
# Return the list, calcalated sum and multiplication of elements
# example: [1,7,3] Return [11, 21]

def sum_and_mult(arr):
    new_list = []
    sum_list = 0
    mult_list = 1
    for element in arr:
        sum_list = sum_list + element
        mult_list = mult_list * element
    new_list.append(sum_list)
    new_list.append(mult_list)
    return new_list
test_list = [1, 7, 3]
result = sum_and_mult(test_list)
print(result)
