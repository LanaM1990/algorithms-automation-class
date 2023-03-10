def sum_of_digits(n: int):
    sum = 1
    for i in range(2, n+1):
        sum = sum+i

    print(f'Sum of {n} is {sum}')

num = 5
sum_of_digits(num)
