# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

# 'abcde' compare each character to find out if all unique characters --> True
# 'aabcde' compare to find out duplicates --> False

my_string1 = 'abcde'
my_string2 = 'aabcde'

def verify_unique_characters(string):
    for i in string[:(len(string))]:

        if string.count(i) > 1:
            return False

    return True


print(verify_unique_characters(my_string1))
print(verify_unique_characters(my_string2))






# def string_duplicates(s):


# string = 'abccc'
# string_duplicates(string)




