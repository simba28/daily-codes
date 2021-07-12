# KMP Algorithm

def createSuffixArray(string):
    if len(string)<=1:
        return [0]

    i = 0
    j = 1
    arr = [0]
    while j < len(string):
        if string[j] != string[i]:
            if i > 0:
                i = arr[i-1]
                continue
            arr.append(0)
            j += 1
        else:
            arr.append(i+1)
            i += 1
            j += 1

    return arr

def isStringPresent(string, sub):
    if not sub:
        return True
    if not string:
        return False

    suffArr = createSuffixArray(sub)

    i, j = 0, 0

    while i < len(string):

        if string[i] == sub[j]:
            i += 1
            j += 1

        else:
            if j > 0:
                j = suffArr[j-1]
                continue
            i += 1
        
        if j == len(sub):
            return True

    return False

print(isStringPresent('abxabcabcaby', 'abcabz'))