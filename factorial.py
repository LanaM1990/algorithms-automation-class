def factorial(n: int):
    result = 1  #step 1
    for i in range(2, n + 1):
        print(f'Step: {i}')
        result *= i  # result * i
    print(f'Factorial of {n} is {result}')


number = 5
factorial(5)

