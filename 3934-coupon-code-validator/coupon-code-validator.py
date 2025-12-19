import re
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        electronics, grocery, pharmacy, restaurant = [], [], [], []
        for i in range(len(code)):
            if bool(re.fullmatch(r'[A-Za-z0-9_]+', code[i])):
                if isActive[i]:
                    if businessLine[i] == "electronics":
                        electronics.append(code[i])
                    elif businessLine[i] == "grocery":
                        grocery.append(code[i])
                    elif businessLine[i] == "pharmacy":
                        pharmacy.append(code[i])
                    elif businessLine[i] == "restaurant":
                        restaurant.append(code[i])
        return sorted(electronics) + sorted(grocery) + sorted(pharmacy) + sorted(restaurant)
        
                    


