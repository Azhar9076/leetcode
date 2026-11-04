class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        n  = len(numbers)
        for i in range(n):
            required = target - numbers[i]
            low = i + 1
            high = len(numbers) - 1

            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == required:
                    return [i+1, mid+1]
                elif numbers[mid] < required:
                    low = mid + 1
                else:
                    high = mid - 1
                        
