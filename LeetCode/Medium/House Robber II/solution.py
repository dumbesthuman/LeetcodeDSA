class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n==1:
            return nums[0]
        
        def robb(houses):
            m = len(houses)
            dp = [0] * m

            dp[0] = houses[0]
            if m ==1:
                return houses[0]
            dp[1]= max(houses[0],houses[1])
            
            
            for i in range(2,m):
                dp[i]= max(dp[i-1],dp[i-2]+houses[i])
            return dp[m-1]
            
        return max(robb(nums[:-1]),robb(nums[1:]))