class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n

        for i in range(n):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = nums[i - 1] * prefix[i - 1]
        
        for i in reversed(range(n)):
            if i == (n - 1):
                suffix[i] = 1
            else:
                suffix[i] = nums[i + 1] * suffix[i + 1]
        
        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result
