class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = ''
        lst = S.split()
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        for i,word in enumerate(lst):
            tmp = ''
            if word[0] in vowels:
                tmp = word+'ma'+'a'*(i+1)
            else:
                tmp = word[1:]+word[0]+'ma'+'a'*(i+1)
            res += tmp+' '
            
        return res[:-1]
    
print(Solution().toGoatLatin("I speak Goat Latin"))