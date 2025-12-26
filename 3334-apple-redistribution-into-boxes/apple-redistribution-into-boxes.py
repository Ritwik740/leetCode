class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        totalApples = sum(apple)
        count = 0
        capacity.sort(reverse=True)
        for c in capacity:
            totalApples -= c
            count+=1
            if totalApples <= 0: return count