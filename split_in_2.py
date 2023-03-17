# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’




string_1 = 'house'

def swap_middles(string):
    # count the number of characters inside the word
    count = len(string)

    # create the condition, where we can evaluate if the word has odd number os characters or no
    if count % 2 != 0:
        # do something
        # split the word
        middle = len(string) // 2 + 1
        first_middle = string[:middle]
        second_middle = string[middle:]

    else:
        # do something else
        # split the word
        middle = len(string) // 2
        first_middle = string[:middle]
        second_middle = string[middle:]

    # swap the parts
    first_middle, second_middle = second_middle, first_middle

    #  put them back
    result = first_middle + second_middle

    # print('First middle variable:', first_middle)
    # print('Second middle variable:', second_middle)

    print(result)


swap_middles(string_1)


# result = 'sehou'

