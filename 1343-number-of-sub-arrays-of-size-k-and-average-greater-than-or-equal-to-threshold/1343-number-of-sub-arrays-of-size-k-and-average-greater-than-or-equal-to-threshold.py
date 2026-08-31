class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_slide = sum(arr[:k])
        count = 0
        if window_slide >= threshold * k:
            count += 1
        for i in range (k, len(arr)):
            window_slide += arr[i] - arr [i - k]
            if window_slide >= threshold * k:
                count += 1
        return count        