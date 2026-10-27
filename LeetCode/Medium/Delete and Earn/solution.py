
class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        points = [0] * (max(nums) + 1)

        for num in nums:
            points[num] += num

        prev2 = 0
        prev1 = 0

        for i in range(len(points)):
            current = max(prev1, prev2 + points[i])
            prev2 = prev1
            prev1 = current

        return prev1
