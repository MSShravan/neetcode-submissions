class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp1 = [-1] * len(nums)
        dp2 = [-1] * len(nums)
        def dfs(i, flag, dp):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(nums[i] + dfs(i+2, flag, dp), dfs(i+1, flag, dp))
            return dp[i]
        
        return max(dfs(0, True, dp1), dfs(1, False, dp2))