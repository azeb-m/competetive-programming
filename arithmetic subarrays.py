class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result=[]
        
        for i in range(len(l)):
            query=nums[l[i]:r[i]+1]
            flag=1
            query=sorted(query)
            dif=query[1]-query[0]
            for j in range(len(query)-1):
                if query[j+1] != query[j]+dif:
                    result.append(0)
                    flag=0
                    break
                    
                    
                    
            if flag==1:
               result.append(1)
        return result
