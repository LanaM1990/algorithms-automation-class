def odd_and_even(n):
    even_numbers = []
    odd_numbers = []
    for i in range(len(n)):
        if i % 2 == 0:
            even_numbers.append(i)

        else:
            odd_numbers.append(i)

    print(even_numbers)
    print(odd_numbers)

num = '34560'
odd_and_even(num)
