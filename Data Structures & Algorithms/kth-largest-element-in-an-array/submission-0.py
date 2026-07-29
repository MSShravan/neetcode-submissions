class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-n for n in nums]
        heapq.heapify(minHeap)

        res = None
        while k > 0:
            res = heapq.heappop(minHeap)
            k -= 1
        
        return -res
