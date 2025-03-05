class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


s = Solution()
