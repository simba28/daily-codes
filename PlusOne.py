class Solution:
    def plusOne(self, digits):
        
        # more pythonic code
        digits = list(map(str, digits))
        res = int(''.join(digits))
        res += 1
        res = list(str(res))
        return list(map(int, res))
        

        # with normal approach
        '''
        l = len(digits)
        count = 0
        multiplier = 1
        for i in range(l-1, -1, -1):
            count +=  digits[i] * multiplier
            multiplier *= 10
        
        count += 1
        
        lst = []
        while count>0:
            lst.append(count%10)
            count = count // 10
        
        return lst[::-1]
        '''
        
        # by just looking at the last element
        '''
        i = -1
        l = len(digits)
        while True:
            if digits[i] == 9:
                digits[i] = 0
                if l == (i*-1):
                    digits.insert(0,0)
                i -= 1
            else:
                digits[i] += 1
                break
        return digits
        '''

test = Solution()
print(test.plusOne([9,8,9,6,9,6,8,9,9]))