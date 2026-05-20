class Solution(object):
    def isPalindrome(self, s):
        filtered = ""

        for ch in s:
            if ch.isalnum():
                filtered += ch.lower()

        left, right = 0, len(filtered) - 1

        while left < right:
            if filtered[left] != filtered[right]:
                return False

            left += 1
            right -= 1

        return True