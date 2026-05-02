class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotation = {'0':'0', '1':'1', '2':'5', '5':'2', '6':'9', '8':'8', '9':'6'}
        def check(num: int) -> bool:
            num = str(num)
            new = ''
            for digit in num:
                if digit in rotation.keys():
                    new+=rotation[digit]
                else: return False
            return num != new
        count = 0
        for i in range(1,n+1):
            count+=1 if check(i) else 0
        return count