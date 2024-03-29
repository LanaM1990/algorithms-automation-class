# Write a program that takes as input a sorted array and updates it so that all duplicates
# have been removed and the remaining elements have been shifted left to fill the emptied indices.
# Fill the remaining indices with zeroes.
# Return the number of valid elements.
# You cannot use sets for this coding challenge.


# code here
# O(n)
def delete_duplicates(arr: list):
    write_index = 1

    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1

    for i in range(write_index, len(arr)):
        arr[i] = 0

    print(arr)
    return write_index

test_list = [2, 5, 5, 6, 7, 7, 7, 9, 10]  # 6, [2, 5, 6, 7, 9, 10, 0, 0, 0]
test_result = delete_duplicates(test_list)
print(test_result)