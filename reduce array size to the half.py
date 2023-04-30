from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        count_dict = Counter(arr)
        size=len(arr)/2
        sum=0
        cout=0
        for x in reversed(sorted(count_dict.values())):
            sum=sum+x
            cout=cout+1
            if sum>= size:
                break
        return cout
