#1295: Find numbers with even number of digits
#Given an array nums of integers, return how many of them contain an even number of digits.

#Example 1:
#
#Input: nums = [12,345,2,6,7896]
#Output: 2

def count_even_digits(nums):
    count = 0
    for i in range(len(nums)):
        out = list(map(int, str(nums[i])))
        if len(out) % 2 == 0:
            count += 1
    return count

# Example usage
nums = [12, 345, 2, 6, 7896]
result = count_even_digits(nums)
print("Count of numbers with even number of digits:", result)

