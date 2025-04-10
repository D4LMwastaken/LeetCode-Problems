def findLHS(nums):
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    
    max_length = 0
    
    for num in counter:
        if num + 1 in counter:
            current_length = counter[num] + counter[num + 1]
            max_length = max(max_length, current_length)
        
    return max_length

print(findLHS([1,3,2,2,5,2,3,7]))