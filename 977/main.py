
# Note: Kinda different from puzzle due to removal of self...
def sortedSquares(nums):
    sorted_list = [] # Yay! New list!
    
    for num in nums:
        sorted_list.append(num * num) # Wait, a*a = a^2
        
    sorted_list.sort() # D4LM, don't reverse this!
    
    return sorted_list
    
    
print(sortedSquares([-4,-1,0,3,10])) # Debugging line...