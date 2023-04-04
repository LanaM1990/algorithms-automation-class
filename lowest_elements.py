# Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def lowest_element(original_list):
    original_list.sort()
    print(original_list[0], original_list[1]) #return original_list[:2]


test_list = [198, 3, 4, 9, 10, 9, 2]
lowest_element(test_list)
