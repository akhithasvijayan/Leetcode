class Solution:
    def shipWithinDays(self, weights, days):

        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            current_weight = 0
            required_days = 1

            for weight in weights:
                if current_weight + weight > mid:
                    required_days += 1
                    current_weight = 0

                current_weight += weight

            if required_days <= days:
                right = mid - 1
            else:
                left = mid + 1

        return left