class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def findProd(num):
            prod = 1
            while num:
                dig = num%10
                prod*=dig
                num//=10
            return prod

        while True:
            if findProd(n)%t==0:
                return n 
            else:
                n+=1

