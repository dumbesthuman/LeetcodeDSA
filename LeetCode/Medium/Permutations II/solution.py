from collections import Counter
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        counts = Counter(nums)
        n = len(nums)
        path: list[int] = []
        ans: list[list[int]] = []

        def backtrack() -> None:
            if len(path) == n:
                ans.append(path.copy())
                return

            for num, freq in counts.items():
                if freq > 0:
                    counts[num] -= 1
                    path.append(num)
                    backtrack()
                    path.pop()
                    counts[num] += 1

        backtrack()
        return ans