# DATE: 03/11/2026
#
# PROBLEM LINK: https://leetcode.com/problems/minimize-the-maximum-value-of-gcd-connected-array
# PROBLEM STATEMENT: Minimize the Maximum Value of GCD-Connected Array
# DIFFICULTY: Medium
# __________________________________________________
# 
# You are given three integers n, index, and value.
# An integer array nums of length n is called GCD-Connected if:
# nums[i] > 0 for 0 <= i <= n - 1.
# nums[i] < nums[i + 1] for 0 <= i <= n - 2.
# nums[index] = value.
# gcd(nums[i], nums[i + 1]) > 1 for 0 <= i <= n - 2.
# Return the minimum possible maximum value, nums[n - 1], among all GCD-Connected arrays nums. If no such array exists, return -1.
#
# Example 1:
# Input: n = 4, index = 2, value = 8
# Output: 10
# Explanation:
# The GCD-Connected array will look like: ​​​​​​​nums = [?, ?, 8, ?] since nums[2] = 8.
# Since nums[3] > 8 and gcd(8, 9) = 1, every valid GCD-Connected array must have nums[3] >= 10.
# One optimal array satisfying all conditions is [2, 4, 8, 10].
# Thus, the minimum possible value of nums[3] is 10.
#
# Example 2:
# Input: n = 2, index = 1, value = 3
# Output: -1
# Explanation:
# The GCD-Connected array will look like: nums = [?, 3] since nums[1] = 3.
# Since we need 0 < nums[0] < nums[1] = 3, there are only two possible arrays: [1, 3] and [2, 3]. Neither of them satisfies gcd(nums[0], nums[1]) > 1.
# Therefore, no valid GCD-Connected array exists, and the answer is -1.
#
# Example 3:
# Input: n = 2, index = 0, value = 3
# Output: 6
# Explanation:
# The GCD-Connected array will look like: nums = [3, ?] since nums[0] = 3.
# Since nums[1] > 3 and gcd(3, 4) = gcd(3, 5) = 1, every valid GCD-Connected array must have nums[1] >= 6.
# One optimal array is [3, 6].
# Thus, the minimum possible value of nums[1] is 6.
#
# Constraints:
# 2 <= n <= 10^9
# 1 <= value <= 10^9
# 0 <= index <= n - 1
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# 1. Core fact: consecutive integers are always coprime (gcd = 1).
#    So in a strictly increasing chain with gcd(adjacent) > 1, every step is >= 2.
#
# 2. RIGHT MOVE (after index):
#    - Naive thought: next = value + 1. Wrong, gcd(value, value+1) = 1.
#    - Fix: next element must share a prime factor with value, so the smallest
#      jump is p = smallest prime factor of value -> next = value + p.
#    - value + p is always even, so after that, +2 per step is the minimum.
#    - Formula: value + p + 2 * (right - 1), where right = n - index - 1.
#
# 3. LEFT MOVE (before index):
#    - Naive thought: just go down by 1 each step. Wrong, same coprime issue.
#    - Fix: the element just before value is at most value - p
#      (largest multiple of p below value; larger primes give a smaller number).
#    - Going further left, each step down is >= 2, and nums[0] >= 2
#      (1 can never have gcd > 1), so nums[index-1] >= 2 * index.
#    - Feasibility check: 2 * index <= value - p, else return -1.
#
# 4. Why the bounds are tight: all-even chain 2, 4, ..., value - p, value, ...
#    achieves both limits, so no tighter bound exists.
#
# 5. Smallest prime factor: loop i from 2 to sqrt(value); if none divides,
#    value is prime and p = value.
#
# 6. Edge cases: value == 1 -> -1; right == 0 -> return value;
#    prime value works only when index == 0.
#
# 7. Pattern: "minimize the maximum" problems don't always need binary search.
#    Sometimes the left side only gives a feasibility check and the right side
#    gives the closed-form answer.
# __________________________________________________


class Solution:
    def minimumMaxValue(self, n: int, index: int, value: int) -> int:
        if value == 1:
            return -1
        
        smallest_factor = value
        
        for i in range(2, int(value**0.5)+1):
            if value % i == 0:
                smallest_factor = i
                break
                
        available_space = value - smallest_factor
        required_space = 2 * index

        if available_space < required_space:
            return -1

        right = n-index-1

        if right == 0:
            return value
        
        return value + smallest_factor + 2* (right -1)
        