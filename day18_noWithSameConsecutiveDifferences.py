class Solution:
    def numsSameConsecDiff(self, N, K):
        
        self.res = []
        self.K = K
        self.N = N
        if self.N==1:
            self.res.append(0)
        
        for i in range(1,10):
            self.helper(str(i))
                
        return self.res
    
    def helper(self, tmp):
        if len(tmp)==self.N:
            self.res.append(int(tmp))
            return
        
        ch = int(tmp[-1])
        if ch >= self.K:
            self.helper(tmp+str(ch-self.K))
        if self.K!=0 and ch+self.K<10:
            self.helper(tmp+str(ch+self.K))
        
        return

print(Solution().numsSameConsecDiff(3,7))