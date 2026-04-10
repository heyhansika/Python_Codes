class Solution:
    def myPow(self, x, n):
        power = n
        
        if power < 0:
            x = 1 / x
            power = -power
        
        result = 1.0
        
        while power > 0:
            if power % 2 == 1:
                result *= x
            x *= x
            power //= 2
        
        return result
