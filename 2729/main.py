def isFascinating(n: int) -> bool: # Function is boolean...
    concatenated = str(n) + str(2 * n) + str(3 * n)
    # concentating = joining two strings
    
    if '0' in concatenated: #0's not allowed...
        return False
    
    if len(concatenated) != 9: 
        """ 
        Just general reason, if the string is not equal 9,
        there is too many or too much digits...
        """ 
        return False
        
    for digit in '123456789':
        if concatenated.count(digit) != 1: # every single digit can only be one...
            return False
            
        
    return True