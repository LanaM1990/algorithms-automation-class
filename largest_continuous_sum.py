def find_sum(arr):
    max_sum = arr[0] # 1
    current_sum = arr[0] # 1

    for num in arr[1:]:
        current_sum = max(current_sum + num, num) #1 + 2 , 2 => 3 + (-1), -1 => 2
        max_sum = max(current_sum, max_sum) # 3, 1 => 3

    return max_sum

test_arr = [1, 2, -1, 3, 4, 10, 10, -10, -1]
result = find_sum(test_arr)
print(result)

