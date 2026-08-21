class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0]*1000
        for t in trips:
            diff[t[1]] += t[0]
            diff[t[2]] -= t[0]
        
        currSum = 0
        for d in diff:
            currSum += d
            if currSum > capacity:
                return False
        
        return True
