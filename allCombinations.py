'''
given a string and a array of strings, return an all possible combinations 
from the array which can combine to make the word.
'''


def allConstruct(target, wordBank, memo={}):
    if (target in memo):
        return memo[target]
    if (target == ''):
        return [[]]

    result = []

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank, memo)
            targetWays = list(map(lambda arr: [word]+arr, suffixWays))
            result.extend(targetWays)

    memo[target] = result
    return result


print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(allConstruct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab',
                   ['a', 'aaa', 'aaaa', 'aaaaaa', 'aaaaaa']))
