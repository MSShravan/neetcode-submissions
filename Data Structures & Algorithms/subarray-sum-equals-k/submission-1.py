class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        preSums = {0:1}

        for n in nums:
            curSum += n
            diff = curSum - k
            res += preSums.get(diff, 0)
            preSums[curSum] = 1 + preSums.get(curSum, 0)
        
        return res