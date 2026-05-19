class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        
        # Dictionary to store frequency of prefix sums
        prefix_count = {0: 1}
        
        for num in nums:
            prefix_sum += num
            
            # Check if (current prefix sum - k) exists
            if prefix_sum - k in prefix_count:
                count += prefix_count[prefix_sum - k]
            
            # Store current prefix sum
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        
        return count