class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = nums[0:k]
        heapq.heapify(arr)
        
        for i in range(k, len(nums)):
            if (nums[i] >= arr[0]):
                heapq.heappush(arr, nums[i])
                heapq.heappop(arr)
        
        return arr[0]