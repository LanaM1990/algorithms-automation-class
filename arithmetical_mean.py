# Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]
#

# find arithmetical mean  = sum of num in the list divided by length
# return list with elements below arithmetical mean
def arithm_mean(original_list):
    new_list = []
    sum_num = 0
    for num in range(0, len(original_list)):
        sum_num = sum_num + original_list[num] #arithmetical mean sum(original_list)/len(original_list)

    arith_m = sum_num/len(original_list)
    print(arith_m)
    for num in range(0, len(original_list)):
        if original_list[num] <= arith_m:
            new_list.append(original_list[num])
    return new_list


test_list = [1, 3, 5, 6, 4, 10, 2, 3]
result = arithm_mean(test_list)
print(result)








