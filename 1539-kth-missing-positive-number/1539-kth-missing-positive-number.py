class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        right, left = 0 , len(arr)
        while right < left:
            mid = (right + left) // 2
            missing_no = arr[mid] - (mid+1)
            if missing_no < k:
                right = mid + 1
            else:
                left = mid
        return left + k        