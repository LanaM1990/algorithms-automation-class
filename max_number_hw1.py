0(1)
def find_max(a, b, c):
    if a > b and a > c:  # 10>20 and 10>40
        return a         # 10
    if b > a and b > c:  # 20>10 and 20>40
        return b         # 20
    return c              #40

result = find_max(10, 20, 40)
print(result)

# my_list = [124, 21, 31]
#
# print(max(my_list))

# def my_list(n):
#     new_list = []
#     while n > 0:
#         new_list.append(n % 10)
#         n = (n - n % 10) // 10
#     print(new_list)
#
# list_1 = 35231
# my_list(list_1)

