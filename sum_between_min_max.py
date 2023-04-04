#Find a sum of elements between min and max elements
#min and max elements are not included
#all numbers are unique

# code here
# O(n)
def sum_between_min_and_max(arr):
    if len(arr) <= 2:
        return 0

    min_item = max_item = arr[0]
    min_index = max_index = 0
    i = 1
    while i < len(arr):
        if arr[i] > max_item:
            max_item = arr[i]
            max_index = i
        if arr[i] < min_item:
            min_item = arr[i]
            min_index = i
        i += 1

    print(f"min index: {min_index}, max index: {max_index}")
    return sum(arr[min(min_index, max_index) + 1:max(min_index, max_index)])

test_list1 = [2, 1, 5, 7, 8, 4]  # min_index: 1, max_index: 4, sum: 12
test_list2 = [2, 7, 5, 4, 1, 3]  # min_index: 4, max_index: 1, sum: 9
test_list3 = [1, 2]  # 0

print(test_list1[0 + 1:5])

# test_result1 = sum_between_min_and_max(test_list1)
# print(test_result1)
#
# test_result2 = sum_between_min_and_max(test_list2)
# print(test_result2)

# test_result3 = sum_between_min_and_max(test_list3)
# print(test_result3)