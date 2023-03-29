class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
      nums.sort()  
      count=0
      def binary_search(arr, low, high, x):
 
    
         if high >= low:
 
             mid = (high + low) // 2
 
        
             if arr[mid] == x:
                 return mid
 
        
       
             elif arr[mid] > x:
                 return binary_search(arr, low, mid - 1, x)
 
       
             else:
                 return binary_search(arr, mid + 1, high, x)
 
         else:
        
             return -1
      result=binary_search(nums, 0, len(nums)-1, k-nums[0])
         
      while len(nums)>1:
             result=binary_search(nums, 0, len(nums)-1, k-nums[0])
             if result != -1 and result != 0:
                nums.pop(result)
                nums.pop(0)
                count=count+1
             elif result != -1:
                temp=nums[0]
                nums.pop(0)
                result=binary_search(nums, 0, len(nums)-1, k-temp)
                if result != -1:
                   nums.pop(result)
                   count=count+1 
                else:
                   continue      
             else:
                nums.pop(0)
                    
      return count
