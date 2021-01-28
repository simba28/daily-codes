class Solution:
    def distributeCandies(self, candies, num_people):
        
        res = [0]*num_people
        
        
        turn = 0
        while candies > 0:
            
            n = int(num_people/2*(2*(turn*num_people+1) + (num_people-1)))
            if candies>=n:
                res = [res[i]+(turn*num_people)+i+1 for i in range(num_people)]
                candies -= n
                turn += 1
            else:
                i = 0
                n = turn*num_people
                while True:
                    if candies>=n+i+1:
                        res[i] += n+i+1
                        candies -= n+i+1
                        i += 1
                    else:
                        res[i] += candies
                        candies = 0
                        break
                        
        return res
    
    
#         idx, count = 0,1
        
#         while candies>0:
#             res[idx] += count
#             candies -= count
#             count += 1
#             idx += 1
#             if idx == num_people: idx=0
#             if count>candies: count = candies
        
#         return res
                
print(Solution().distributeCandies(80,5))        