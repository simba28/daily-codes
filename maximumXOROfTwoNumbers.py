'''
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.
'''

class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insertBits(self, num):
        bitNum = bin(num)[2:].zfill(32)
        node = self.root
        for bit in bitNum:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
            
    
    def findMaxXor(self, num):
        bitNum = bin(num)[2:].zfill(32)
        node = self.root
        maxXor = ''
        
        for bit in bitNum:
            oppBit = '1' if bit=='0' else '0'
            if oppBit in node.children:
                maxXor += oppBit
                node = node.children[oppBit]
            else:
                maxXor += bit
                node = node.children[bit]
                
        return int(maxXor,2)^num
                
    
    def findMaximumXOR(self, nums):
        
        for num in nums:
            self.insertBits(num)
            
        max_ = 0
        for num in nums:
            max_ = max(max_, self.findMaxXor(num))
            
        return max_
        

print(Solution().findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))

