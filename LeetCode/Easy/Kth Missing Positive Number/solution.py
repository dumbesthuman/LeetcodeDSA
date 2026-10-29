class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        num =1
        while True:
            if num not in arr:
                k-=1
            if k==0:
                return num
            num+=1