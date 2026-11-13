# DATE: 13/11/2026
#
# PROBLEM LINK: https://leetcode.com/problems/count-valid-substrings-i/description/
# PROBLEM STATEMENT: Count Valid Substrings I
# DIFFICULTY: Easy
# __________________________________________________
# You are given a string s consisting only of the characters 'a', 'b', and 'c'.
# A string is called valid if it does not contain "abc" as a substring.
# Return the number of valid substrings in s. Substrings with different starting or ending indices are counted separately.
# Example 1:
# Input: s = "abac"
# Output: 10
# Explanation:
# The following substrings don't contain "abc"​​​​​​​ as a substring:
# s[0..0] = "a"
# s[0..1] = "ab"
# s[0..2] = "aba"
# s[0..3] = "abac"​​​​​​​
# s[1..1] = "b"
# s[1..2] = "ba"
# s[1..3] = "bac"
# s[2..2] = "a"
# s[2..3] = "ac"
# s[3..3] = "c"
# Thus, the answer is 10.
# Example 2:
# Input: s = "abc"
# Output: 5
# Explanation:
# The following substrings don't contain "abc"​​​​​​​ as a substring:
# s[0..0] = "a"
# s[0..1] = "ab"
# s[1..1] = "b"
# s[1..2] = "bc"
# s[2..2] = "c"​​​​​​​
# Thus, the answer is 5.
# Example 3:
# Input: s = "ac"
# Output: 3
# Explanation:
# All substrings in s don't contain "abc" as a substring​​​​​​​. Thus, the answer is 3.
# Constraints:
# 1 <= s.length <= 10^5​​​​​​​
# s only consists of 'a', 'b', and 'c' characters.
# __________________________________________________
#
# INSIGHTS GAIN FROM THIS QUESTION: (ANY NOTES, IDEAS, NEW TRICKS / THIS WILL HELP IN QUICK REVISION)
# __________________________________________________
# 
# 1. Used Sliding Window + Two Pointers technique.
# 2. Instead of generating all substrings, count valid substrings
#    by fixing the ending index i.
# 3. Maintain 'left' as the earliest valid starting index.
# 4. If "abc" is detected, update left = i - 1 because
#    starting from i-1 gives the valid substring "bc".
# 5. Number of valid substrings ending at index i:
#       i - left + 1
# 6. Add this value to count at every iteration.
#
# KEY FORMULA:
# count += (right - left + 1)
#
# PATTERN: Sliding Window / Two Pointers
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
#
# REVISION TIP:
# Count substrings ending at each index instead of
# generating every possible substring.
# __________________________________________________


class Solution:
    def countValidSubstrings(self, s: str) -> int:

        count = 0
        left = 0
        
        for i in range(len(s)):
            if i >= 2 and s[i-2:i+1] == "abc":
                  left = i-1
            count += i-left+1

        return count
            