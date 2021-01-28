'''
You are driving a vehicle that has capacity empty seats initially available for passengers.  
The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains 
information about the i-th trip: the number of passengers that must be picked up, and the 
locations to pick them up and drop them off.  The locations are given as the number of 
kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all 
the given trips.
'''

class Solution:   
    def carPooling(self, trips, capacity: int) -> bool:
        
        timestamp = []
        
        for trip in trips:
            timestamp.append([trip[1], trip[0]])
            timestamp.append([trip[2], -trip[0]])
            
        timestamp.sort()
        
        load = 0
        for _, passengerChange in timestamp:
            
            load += passengerChange
            if load > capacity:
                return False
            
        return True
        
        # l = len(trips)
        # sTrip = sorted(trips, key = lambda x : x[1])
        # eTrip = sorted(trips, key = lambda x : x[2])
        
        # x, y = 0, 0
        # for i in range(1,sTrip[-1][1]+1):
            
        #     while x<len(sTrip) and sTrip[x][1]<=i:
        #         if sTrip[x][1]==i:
        #             capacity -= sTrip[x][0]
        #         x += 1
                
        #     while y<len(eTrip) and eTrip[y][2]<=i:
        #         if eTrip[y][2] == i:
        #             capacity += eTrip[y][0]
        #         y += 1
                
        #     if capacity < 0 :
        #         return False
            
        # return True
    
print(Solution().carPooling([[3,2,7],[3,7,9],[8,3,9]],11))
            
        