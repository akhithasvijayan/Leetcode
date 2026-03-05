class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        
        # Count frequency of each number
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Sort numbers based on frequency (descending)
        sorted_nums = sorted(count, key=count.get, reverse=True)
        
        # Return first k elements
        return sorted_nums[:k]