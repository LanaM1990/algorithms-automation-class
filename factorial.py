def factorial(n: int):
    result = 1  #step 1
    for i in range(2, n + 1):
        print(f'Step: {i}')       #  2     3    4     5   result
        result *= i  # result * i  1*2 = 2*3= 6*4= 24*5 = 120
    print(f'Factorial of {n} is {result}')


number = 5
factorial(5)

