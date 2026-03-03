class Solution:
    def sortColors(self, nums):
        low = 0          # position for next 0
        mid = 0          # current element
        high = len(nums) - 1   # position for next 2

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1