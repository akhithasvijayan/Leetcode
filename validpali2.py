class Solution(object):
    def validPalindrome(self, s):

        def isPal(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return isPal(left + 1, right) or isPal(left, right - 1)

            left += 1
            right -= 1

        return True