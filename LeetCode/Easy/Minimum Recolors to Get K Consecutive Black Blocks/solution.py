class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        for i in range(k):
            if blocks[i]=='W':
                count+=1
        min_count = count

        for i in range(k,len(blocks)):
            if blocks[i]=='W':
                count+=1
            if blocks[i-k]=='W':
                count-=1
            min_count=min(count,min_count)
        return min_count