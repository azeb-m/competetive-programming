class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        numm=[]
        i=0
        while len(numm)!=len(nums):
            numm.append(int(nums[i]))
            i=i+1
        numm.sort()
        return str(numm[len(nums)-k])
