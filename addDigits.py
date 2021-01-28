class Solution:
    def addDigits(self, num: int) -> int:
        # time = O(1)
        if num == 0: 
            return 0
        elif num%9==0:
            return 9
        else:
            return num%9
        
        # using recursion
        # if num<10:
        #     return num
        # else:
        #     count = 0
        #     for i in str(num):
        #         count += int(i)
        #     return self.addDigits(count)

print(Solution().addDigits(179))
        