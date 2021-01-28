class Solution:
    def search(self, i, j, idx):
        
        if len(self.word)-1 == idx: return True
        
        temp = self.board[i][j]
        self.board[i][j] = ' '
        
        if i>0 and self.board[i-1][j] == self.word[idx+1] and self.search(i-1, j, idx+1) :
            return True
        if j>0 and self.board[i][j-1] == self.word[idx+1] and self.search(i, j-1, idx+1):
            return True
        if i<len(self.board)-1 and self.board[i+1][j] == self.word[idx+1] and self.search(i+1, j, idx+1):
            return True
        if j<len(self.board[0])-1 and self.board[i][j+1] == self.word[idx+1] and self.search(i, j+1, idx+1):
            return True
        
        self.board[i][j] = temp
        return False
    
    def exist(self, board, word):
        
        self.board = board
        self.word = word
        
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == self.word[0] and self.search(i, j, 0):
                    return True
        
        return False   

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],'ABCED'))