# def odd_and_even(n):
#     even_numbers = []
#     odd_numbers = []
#     for i in range(len(n)):
#         if i % 2 == 0:
#             even_numbers.append(i)
#         else:
#             odd_numbers.append(i)
#
#     print(odd_numbers)
#     print(even_numbers)
#
# num = '34560'
# odd_and_even(num)

# 0(n)
def count_odd_even(n: int):
    odds = 0
    evens = 0

    while n != 0:
        current_digit = n % 10 # 0 8 6 | 5 3
        if current_digit % 2: #  0 0 0 | 1 1
            odds += 1 # got skipped first 3 times  1 1 = 2
        else:
            evens += 1        #  1 1 1 | got skipped two last times  3
        n = n // 10

    print(f'Odds:{odds}')
    print(f'Evens: {evens}')

test_n = 35680
count_odd_even(test_n)



