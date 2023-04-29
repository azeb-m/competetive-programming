class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        i=0
        result=[]
        max=len(arr)
        j=0
        temp=[]
        while(j < len(arr)-1):
           i=0
           #flag=0
           while(i < len(arr)):
              if(arr[i]==max):
                  result.append(i+1)
                  result.append(len(arr)-j)
                  max=max-1
                  temp=arr[0:i+1]
                  temp.reverse()
                  temp=temp + arr[i+1:len(arr)-j]
                  temp.reverse()
                  arr=temp +arr[len(arr)-j:]
                  
                  
                  j=j+1

                  #flag=1
                  break
              i=i+1
           #if flag==0:
              #j=j+1
        return result
