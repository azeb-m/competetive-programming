class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[]
        nums.sort()
        l=0
        r=len(nums)-1
        while len(res) != len(nums):
            res.append(nums[l])
            l=l+1
            if l<=r:
                res.append(nums[r])
                r=r-1
        return res
