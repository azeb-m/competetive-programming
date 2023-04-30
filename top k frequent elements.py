from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=[]
        for x in dict(sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)):
            if k > len(result):
                result.append(x)
            else:
                break
        return result
