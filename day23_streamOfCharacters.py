class StreamChecker:

    def __init__(self, words):
        self.trie = dict()
        self.stream = ''
        for word in words:
            self.insert(word[::-1])

    def query(self, letter):
        self.stream = letter+self.stream
        return self.search(self.stream)
    
    def insert(self, word):
        curr = self.trie
        for ch in word:
            if ch not in curr:
                curr[ch] = dict()
            curr = curr[ch]
        curr['_end'] = ''
        
    def search(self, word):
        curr = self.trie
        for ch in word:
            node = curr.get(ch)
            if not node:
                return False
            curr = node
            if '_end' in curr:
                return True
        return False

sol = StreamChecker(['cd','f','kl'])
for i in range(97,109):
    print(sol.query(chr(i)), end=' ')