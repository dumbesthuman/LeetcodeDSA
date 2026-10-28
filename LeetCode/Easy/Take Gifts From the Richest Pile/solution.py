import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        for i in range(k):
            max = -heapq.heappop(gifts)
            add = isqrt(max)
            heapq.heappush(gifts,-add)
        return -sum(gifts)