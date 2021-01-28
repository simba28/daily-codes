#link => https://leetcode.com/problems/word-ladder/

import collections

class Solution:

    def ladderLength(self, beginWord, endWord, wordList):

        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])

        while queue:
            word, length = queue.popleft()
            if word == endWord: return length

            for i in range(len(word)):

                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = word[:i] + c + word[i+1:]

                    if nextWord in wordList:
                        wordList.remove(nextWord)
                        queue.append([nextWord, length+1])

        return 0

print(Solution().ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
