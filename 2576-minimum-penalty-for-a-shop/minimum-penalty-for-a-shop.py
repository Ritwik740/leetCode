class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count('Y')
        min_pen = penalty
        j = 0
        for i,c in enumerate(customers):
            if c == 'Y':
                penalty-=1
            else:
                penalty +=1
            if penalty < min_pen:
                min_pen = penalty
                j = i+1
        return j