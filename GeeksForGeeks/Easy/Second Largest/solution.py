class Solution:
    def getSecondLargest(self, arr):
        # code here
    
        
        arr = sorted(set(arr))

        if len(arr) < 2:
            return -1

        return arr[-2]