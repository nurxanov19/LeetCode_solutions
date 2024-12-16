from os import system
system('clear')
from functools import reduce


class Solution(object):         #
    def isValid(self, s):
        stack = []

        matching_pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matching_pairs.values():
                stack.append(char)

            elif char in matching_pairs:
                if len(stack) == 0 or stack.pop() != matching_pairs[char]:
                    return False
            else:
                return False

        return not stack


obj = Solution()

print(obj.isValid("()"))
print(obj.isValid("()[]{}"))
print(obj.isValid("(]"))
print(obj.isValid("([])"))


class Solution(object):
    def majorityElement(self, nums):

        nums.sort()
        return nums[len(nums) // 2]

obj = Solution()

print(obj.majorityElement([2,2,1,1,1,2,2]))
print(obj.majorityElement([3,2,3]))


