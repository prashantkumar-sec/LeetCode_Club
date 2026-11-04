# DATE: 04/11/2026
#
# PROBLEM LINK: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/
# PROBLEM STATEMENT: Minimum Moves to Equal Array Elements III
# DIFFICULTY: Easy
# __________________________________________________
# 
# You are given an integer array nums.
# In one move, you may increase the value of any single element nums[i] by 1.
# Return the minimum total number of moves required so that all elements in nums become equal.
#
# Example 1:
# Input: nums = [2,1,3]
# Output: 3
# Explanation:
# To make all elements equal:
# Increase nums[0] = 2 by 1 to make it 3.
# Increase nums[1] = 1 by 1 to make it 2.
# Increase nums[1] = 2 by 1 to make it 3.
# Now, all elements of nums are equal to 3. The minimum total moves is 3.
#
# Example 2:
# Input: nums = [4,4,5]
# Output: 2
# Explanation:
# To make all elements equal:
# Increase nums[0] = 4 by 1 to make it 5.
# Increase nums[1] = 4 by 1 to make it 5.
# Now, all elements of nums are equal to 5. The minimum total moves is 2.
#
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# - We can only increase, never decrease. So the target has to be max(nums).
#   Going below max is impossible, going above max just wastes moves.
# - Answer = sum of (max - x) for every x. No need to simulate anything.
# - Think of it as bringing everyone up to the topper's marks. Each person
#   needs (topper - their marks), and the total is just all those gaps added.
# - Method-1 loops +1 at a time, so it's O(n * max). Method-2 and the formula are O(n).
# - Don't mix this up with Minimum Moves II, where you can go both ways and
#   the target becomes the median. Here it's only increments, so max.
# __________________________________________________

#________________________________Method-1____________________________________

class Solution1:
    def minMoves(self, nums: list[int]) -> int:
        value = max(nums)
        count = 0
        for i in nums:
            while i < value:
                i += 1
                count += 1
        return count

#________________________________Method-2____________________________________

class Solution2:
    def minMoves(self, nums: list[int]) -> int:
        value = nums[0]

        for i in nums:
            if i > value:
                value = i

        count = 0

        for i in nums:
            count += value - i

        return count