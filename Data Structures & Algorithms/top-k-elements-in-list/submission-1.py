from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        # return sorted(count, key = count.get, reverse = True)[:k]
        
        h = []
        # min heap
        for i,v in count.items():
            heapq.heappush(h,(v,i))
            if len(h)>k:
                heapq.heappop(h)
            
        return [i[1] for i in h]
                





        

    
        