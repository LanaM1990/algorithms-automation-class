# def swap_variables(a: int, b: int):
#     c = a
#     a = b
#     b = c
#     print(f'After swap: a = {a}, b = {b}')
#
#
# a = 5
# b = 10
# swap_variables(5, 10)

# def swap_variables(a: int, b: int):
#     a = a + b
#     b = a - b
#     a = a - b
#     print(f'After swap: a = {a}, b = {b}')


# a = 50
# b = 100
# swap_variables(50, 100)

def swap_variables(a: int, b: int):
   a, b = b, a
   print(f'After swap: a = {a}, b = {b}')


test_a = 500
test_b = 1000
swap_variables(test_a, test_b)
