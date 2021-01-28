class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.childNodes = {}
        self.isWordEnd = False
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        currNode = self
        for ch in word:
            node = currNode.childNodes.get(ch) or WordDictionary()
            currNode.childNodes[ch] = node
            currNode = node
        currNode.isWordEnd = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        currNode = self
        
        for i in range(len(word)):
            ch = word[i]
            if ch == '.':
                for letter in currNode.childNodes:
                    node = currNode.childNodes.get(letter)
                    if node and node.search(word[i+1:]):
                        return True
                return False
            
            node = currNode.childNodes.get(ch)
            if not node:
                return False
            currNode = node
        
        return currNode.isWordEnd
            
# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('bad')
obj.addWord('dad')
obj.search('pad')
obj.search('.ad')
# obj.addWord(word)
# param_2 = obj.search(word)