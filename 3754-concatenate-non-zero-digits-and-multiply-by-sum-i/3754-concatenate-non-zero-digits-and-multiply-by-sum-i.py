class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num=n
        x=0
        total=0
        if n==0:
            total=0
        else:
            while num>0:
                last_digit=num%10
                if last_digit != 0:
                    x+=last_digit
                    total=total*10+last_digit
                num=num//10
        rev=0
        while total>0:
            last_digit=total%10
            rev=rev*10+last_digit
            total //=10

        
        return x*rev

        