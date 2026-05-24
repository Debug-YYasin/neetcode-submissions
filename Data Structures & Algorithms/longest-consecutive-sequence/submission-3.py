class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        nums = sorted(nums)

        seen = defaultdict(set)
        keycounter = 0

        if len(nums) == 1:
            return 1

        seen[keycounter].add(nums[0])
        for i in range(1, len(nums)):

            if nums[i] == nums[i - 1]:
                seen[keycounter].add(nums[i])
                continue
            
            if (nums[i] - nums[i - 1]) == 1:
                seen[keycounter].add(nums[i])
            else:
                keycounter += 1
                seen[keycounter].add(nums[i])
        
        largest = 0
        for sets in seen.values():
            if len(sets) > largest:
                largest = len(sets)

        return largest
        

