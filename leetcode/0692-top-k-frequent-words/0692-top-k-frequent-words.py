class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordmap=Counter(words)
        minheap=[(-freq ,word) for word , freq in wordmap.items()]
        heapq.heapify(minheap)
        res=[]
        while k >0:
            freq , word = heapq.heappop(minheap)
            res.append(word)
            k -=1
        return res    
