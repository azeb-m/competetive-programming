class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        vector<int>list;
        for(int i=0;i<nums.size()-1;i++)
        {
            int min_index=i;
            for(int j=i+1;j<nums.size();j++)
              if(nums[min_index]>nums[j])
                  min_index=j;
            if(min_index !=i)
            {
                int temp=nums[i];
                nums[i]=nums[min_index];
                nums[min_index]=temp;
            }
        }
        for(int k=0;k<nums.size();k++)
        {
            if(nums[k]==target)
                list.push_back(k);
                
        }
        return list;
    }
};
