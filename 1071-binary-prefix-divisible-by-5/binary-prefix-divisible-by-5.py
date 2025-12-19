class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        binary = ""
        res = []
        for num in nums:
            binary += f'{num}'
            number = int(binary, 2)
            res.append(True if not number % 5 else False)
        return res