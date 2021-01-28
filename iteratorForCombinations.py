class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        
        self.q = []
        
        def getCombinations(start, length, txt):
            if length == 0:
                self.q.append(txt)
                return
            
            for i in range(start, len(characters)-length+1):
                getCombinations(i+1, length-1, txt+characters[i])
                
        getCombinations(0, combinationLength, "")
        

    def next(self) -> str:
        return self.q.pop(0)

    def hasNext(self) -> bool:
        return len(self.q)>0
        
