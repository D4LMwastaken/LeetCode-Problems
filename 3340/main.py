# Lol, too slow

def isBalanced(num):
    """
    :type num: str
    :rtype: bool
    """
    even_sum = 0 # Creation of empty variable to hold sum of all even indices
    odd_sum = 0 # Creation of empty variable to hold sum of all odd indices

    for i in range(len(num)):
        digit = int(num[i]) # conversion to integer

        if i % 2 == 0: # If index is even
            even_sum += digit
        else: # If index is odd
            odd_sum += digit

    return even_sum == odd_sum # Check if both are equal...

print(isBalanced("24123"))
