class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Place each number in its correct position
        # 1 should be at index 0
        # 2 should be at index 1
        # ...
        while True:
            changed = False

            for i in range(n):
                correct_index = nums[i] - 1

                if (
                    1 <= nums[i] <= n and
                    nums[i] != nums[correct_index]
                ):
                    nums[i], nums[correct_index] = nums[correct_index], nums[i]
                    changed = True

            if not changed:
                break

        # Find first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1