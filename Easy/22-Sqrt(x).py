# DATE: 07/11/2026
#
# PROBLEM LINK: https://leetcode.com/problems/sqrtx/description/
# PROBLEM STATEMENT: Sqrt(x)
# DIFFICULTY: Easy
# __________________________________________________
# 
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
# The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#
# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
#
# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
#
# Constraints:
# 0 <= x <= 2^31 - 1
#
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# 1. "Binary search on answer" pattern: jab answer ek monotonic range mein ho
#    (yahan 0 se x), toh direct array na ho tab bhi binary search lag sakta hai.
#    Condition: mid*mid <= x  -> True...True False...False (monotonic).
#
# 2. Floor behavior: jab mid*mid <= x ho, ans = mid save karo aur RIGHT jao
#    (aur bada candidate dhundo). Loop khatam hone par ans = last valid mid = floor(sqrt(x)).
#
# 3. Overflow safe mid: mid = low + (high - low) // 2
#    (Python mein overflow nahi hota, par C++/Java mein (low+high)/2 overflow kar sakta hai).
#
# 4. Edge cases: x = 0 -> 0, x = 1 -> 1. Dono handle ho jaate hain.
#
# 5. Optimization: high = x // 2 + 1 (x >= 2 ke liye). Alternative: Newton's method
#    r = (r + x // r) // 2, jo quadratically converge karta hai.
#
# 6. Template yaad rakho (upper-bound type):
#    if condition(mid): ans = mid; low = mid + 1
#    else: high = mid - 1
# __________________________________________________


class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2

            if mid * mid <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
