class Solution {
public:
    void sortColors(vector<int>& nums) {
        for(int i=0;i<nums.size()-1;i++)
        {   int min_i=i;
         for(int j=i+1;j<nums.size();j++)
             if(nums[min_i]>nums[j])
                 min_i=j;
         if(min_i!=i)
         {
             int temp=nums[min_i];
             nums[min_i]=nums[i];
             nums[i]=temp;
         }
        }
        for(int k:nums)
            cout<<k;
    }
};
