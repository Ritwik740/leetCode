class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        mini = nums.index(min(nums))
        maxi = nums.index(max(nums))
        a = max(mini, maxi) + 1
        b = n - min(mini, maxi)
        c = min(mini, maxi) + 1 + n - max(mini, maxi)
        return min(a, b, c)