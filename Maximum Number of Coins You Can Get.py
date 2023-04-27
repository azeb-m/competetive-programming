class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        result=0
        last=len(piles)-1
        i=1
        while(i<last):
        
            result+=piles[i]
            i=i+2
            last-=1
        
        return result
