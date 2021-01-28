class Solution:
    def leastInterval(self, tasks, n):
        
        char_map = [0]*26
        for i in tasks:
            char_map[ord(i)-65] += 1
            
        char_map.sort(reverse=True)
        
        max_val = char_map[0]-1
        idle = max_val * n
        
        for i in char_map[1:]:
            idle -= min(i, max_val)
            
        return idle+len(tasks) if idle>0 else len(tasks)

print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2))
        