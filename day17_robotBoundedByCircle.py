'''
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot 
can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never 
leaves the circle.
'''

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        direction = (0,1)
        start = [0,0]
        
        for inst in instructions:
            
            if inst=='G':
                start[0] += direction[0]
                start[1] += direction[1]
            
            elif inst=='L':
                direction = (-direction[1],direction[0])
            
            else:
                direction = (direction[1],-direction[0])
                
        return start==[0,0] or direction != (0,1)
    
print(Solution().isRobotBounded('GGLLGG'))