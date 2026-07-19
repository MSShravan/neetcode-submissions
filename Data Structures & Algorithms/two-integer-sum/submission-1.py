class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i, val in enumerate(nums):
            val = nums[i]
            diff = target - val
            if diff in comp:
                return [comp.get(diff), i]
            comp[val] = i
        return []