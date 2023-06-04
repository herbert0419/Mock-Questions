
Problem1: Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Solution:

def moveZeroes(nums):
    """
    Move all 0's to the end of the array while maintaining the relative order of the non-zero elements.
    """
    n = len(nums)
    last_non_zero = 0

    # Traverse the array
    for i in range(n):
        # If the current element is non-zero, move it to the next available position
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1

    # Fill the remaining positions with zeroes
    for i in range(last_non_zero, n):
        nums[i] = 0

    return nums

# Example usage:
nums = [0, 1, 0, 3, 12,6,8,9,0,0,0]
result = moveZeroes(nums)
print(result)

nums = [0]
result = moveZeroes(nums)
print(result)
