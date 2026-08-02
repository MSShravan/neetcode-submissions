class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(sub):
            rob1, rob2 = 0, 0
            for n in sub:
                temp = max(rob2, n + rob1)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        
        return max(helper(nums[:n-1]), helper(nums[1:]))