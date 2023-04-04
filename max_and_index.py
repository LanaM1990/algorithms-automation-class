#given a list of random numbers
#Find and return the max element and the index of this element
#Example: [1, 45, 33, 76, 9, 10] print [3, 76]

def find_max_and_index(arr): # [1, 45, 33, 76, 9, 10]
    new_list = []

    max_index = 0             # 0  1 3
    max_num = arr[max_index]  # 1  45 76

    for i in range(1, len(arr)):#i:1,2,3
        if arr[i] > max_num:
            max_num = arr[i]
            max_index = i

    new_list.append(max_index)
    new_list.append(max_num)
    return new_list

test = [1, 45, 33, 76, 9, 10]
result = find_max_and_index(test)
print(result)

