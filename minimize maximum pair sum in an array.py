class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxi=nums[0]+ nums[len(nums)-1]
        i=1
        j=len(nums)-2
        while i<=len(nums)/2:
            if maxi < nums[i]+nums[j]:
                maxi=nums[i]+nums[j]
            i=i+1
            j=j-1
        return maxi
