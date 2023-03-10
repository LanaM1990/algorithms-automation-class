def sum_of_three(n: int):
    result = 0
    temp_n = n
    while n != 0:
        result = result + (n % 10)
        n = n // 10

    print(f'Sum of all digits {temp_n} is {result}')

test = 125
sum_of_three(test)

