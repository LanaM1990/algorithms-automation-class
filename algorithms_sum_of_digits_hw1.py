#0(n)

def sum_of_digits(n: int):
    # sum = 1
    for i in range(2, n+1): # 2    3   4    5 = result
        sum = sum+i        # 1+2+3+3=6+4=10+5= 15

    print(f'Sum of {n} is {sum}')

# def sum_of_digits(n: int):
#     final_sum = (n * (n + 1))//2
#     return final_sum

# def sum_of_digits(n: int):
#     sum_num = 0            #index 0      1      2      3   4
#     for i in range(n + 1):      #  1     2      3      4   5 = result
#         sum_num = sum_num + i   #0+1 = 1+2 = 3+3 = 6+4=10+ 5 = 15
#     return sum_num

num = 5
result = sum_of_digits(num)
print(result)
