class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(n-1):
            if not nums[i] < nums[i+1]:
                return nums[i+1]
        return min(nums[0], nums[-1])