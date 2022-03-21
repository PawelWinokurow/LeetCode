class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_length = 1
        max_palindrome = s[0]
        dp = [[0] * n for _ in range(n)]
        for s_idx in range(n):
            dp[s_idx][s_idx] = True
        for s_idx in range(n-1):
            if s[s_idx] == s[s_idx+1]:
                dp[s_idx][s_idx+1] = True
                max_length = 2
                max_palindrome = s[s_idx:s_idx+max_length]
        for k in range(3, n+1):
            for s_idx in range(n - k + 1):
                e_idx = s_idx + k - 1
                if dp[s_idx+1][e_idx-1] and s[s_idx] == s[e_idx]:
                    dp[s_idx][e_idx] = True
                    if k > max_length:
                        max_length = k
                        max_palindrome = s[s_idx:s_idx + max_length]
        return max_palindrome
