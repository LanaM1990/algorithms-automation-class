
def increment_list(digits):
    # Start with carry = 1 since we want to increment the number by 1
    carry = 1
    n = len(digits)
    # go over the digits in reverse order
    for i in range(n-1, -1, -1):
        # Add the carry to the current digit
        digits[i] += carry
        # If the sum exceeds 9, we have a carry
        if digits[i] > 9:
            digits[i] = 0
            carry = 1
        else:
            # No carry, we're done
            carry = 0
            break
    return digits
increment_number = [1, 2, 9]
result = increment_list(increment_number)
print(result)