class Solution:
    def search(self, arr: List[int], target: int) -> int:
        start= 0
        end = len(arr) - 1
        ans = -1
        while start <= end:
            mid = (start + end)//2
            if (arr[mid] >= arr[0] and target < arr[0]):
                start = mid + 1
            elif (arr[mid] < arr[0] and target >= arr[0]):
                end = mid - 1
            else:
                if (arr[mid] < target):
                    start = mid + 1
                elif (arr[mid] > target):
                    end = mid - 1
                else:
                    ans = mid
                    break
        return ans
