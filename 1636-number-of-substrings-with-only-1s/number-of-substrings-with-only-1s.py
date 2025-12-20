class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0
        n = len(s)
        left = right = 0
        while left <= right and right < n:
            if s[right] == '1':
                cnt += right - left + 1
                right += 1
            elif s[right] == '0':
                right += 1
                left = right
        return cnt%(10**9+7)