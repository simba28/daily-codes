'''
You are playing the following Bulls and Cows game with your friend: You write down a 
number and ask your friend to guess what the number is. Each time your friend makes a 
guess, you provide a hint that indicates how many digits in said guess match your 
secret number exactly in both digit and position (called "bulls") and how many digits 
match the secret number but locate in the wrong position (called "cows"). Your friend 
will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, 
use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.
'''


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        l = len(secret)
        
        bulls=0
        cows = 0
        sec = list(secret)
        gue = list(guess)
        for i in range(l):
            if guess[i]==secret[i]:
                sec.remove(guess[i])
                gue.remove(guess[i])
                bulls += 1
                
        sec.sort()
        gue.sort()
        for i in gue:
            if i in sec:
                cows += 1
                sec.remove(i)
                
        return str(bulls)+'A'+str(cows)+'B'
        
print(Solution().getHint('1807','7810'))