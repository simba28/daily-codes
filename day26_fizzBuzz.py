from collections import OrderedDict

class Solution:
    def fizzBuzz(self, n):

        res = []
        d = OrderedDict({3:'Fizz',5:'Buzz'})

        for i in range(1,n+1):

            string = ''
            for no in d:
                if i%no==0:
                    string += d[no]

            if not string:
                string = str(i)

            res.append(string)

        return res

print(Solution().fizzBuzz(15))