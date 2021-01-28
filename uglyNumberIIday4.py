# Ugly Number - Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        lst = [1]
        
        i = 0
        j = 0 
        k = 0 
        
        for _ in range(1,n):
            
            temp1 = lst[i]*2
            temp2 = lst[j]*3
            temp3 = lst[k]*5
            
            least = min(temp1,temp2,temp3)
            
            if least == temp1:
                i += 1
            if least == temp2:
                j += 1
            if least == temp3:
                k += 1
                
            lst.append(least)
            
        return lst[-1]

# test = Solution()
# print(test.nthUglyNumber(20))