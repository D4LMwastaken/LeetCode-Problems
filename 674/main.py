"""Steps:
1. Define variables to rack current sequence length and maxium
sequence length
2. Iterate through the array starting from the second element
3. For each element, compare if it's greater than the previous
element
    - If yes, increment current sequence length and update max if
    needed
    - If no, reset current sequence length to 1
4. Return the maxium sequence length found
"""

def findLengthOfLCIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Handle empty array clase
    if not nums:
        return 0
    
    # Initalize variables
    current_length = 1
    max_length = 1
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If current element is greater than previous, increment
        #  current length
        if nums[i] > nums [i-1]:
            current_length += 1
            # Update max_length if current length is larger
            max_length = max(max_length, current_length)
        else:
            # Reset current length if sequence breaks
            current_length = 1
        
    return max_length