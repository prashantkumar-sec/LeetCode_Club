# DATE: 26/11/2026
#
# PROBLEM LINK: https://leetcode.com/problems/power-of-two/
# PROBLEM STATEMENT: Power of Two
# DIFFICULTY: Easy
# __________________________________________________
# 
# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.
#
# Example 1:
# Input: n = 1
# Output: true
# Explanation: 20 = 1
#
# Example 2:
# Input: n = 16
# Output: true
# Explanation: 24 = 16
#
# Example 3:
# Input: n = 3
# Output: false
#
# Constraints:
# -2^31 <= n <= 2^31 - 1
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# A power of two has exactly one set bit (1) in its binary representation
# The expression n & (n - 1) removes the rightmost set bit from a number
# If n is a power of two, removing its only set bit results in 0
# Therefore, n > 0 and (n & (n - 1)) == 0 checks whether n is a power of two
# n > 0 is necessary to exclude zero and negative numbers
# Bit manipulation trick: n & (n - 1) clears the lowest set bit
# Time complexity: O(1)
# Space complexity: O(1)
# __________________________________________________


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0