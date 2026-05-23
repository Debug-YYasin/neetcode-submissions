class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted(nums)
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        sorted_list = dict(sorted(count.items(), key=lambda item:item[1], reverse=True))
        result = []
        for i in sorted_list:
            result.append(i)
            k -= 1      
            if k == 0:
                break
        
        return result

