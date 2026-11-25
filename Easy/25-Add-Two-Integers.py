# DATE: 25/11/2026
#
# PROBLEM LINK: https://leetcode.com/problems/add-two-integers/description/
# PROBLEM STATEMENT:Add Two Integers
# DIFFICULTY: Easy
# __________________________________________________
# 
# Given two integers num1 and num2, return the sum of the two integers.
# Example 1:
# Input: num1 = 12, num2 = 5
# Output: 17
# Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
# Example 2:
# Input: num1 = -10, num2 = 4
# Output: -6
# Explanation: num1 + num2 = -6, so -6 is returned.
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# 1. Used the + operator to add two integers.
# 2. return sends the computed result back to the caller.
# 3. Python supports adding positive, negative and zero values.
# 4. No loops or additional data structures are required.
# 5. Time Complexity: O(1)
# 6. Space Complexity: O(1)
# 7. Always prefer the simplest solution when the problem
#    does not require a complicated algorithm.
# __________________________________________________


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2