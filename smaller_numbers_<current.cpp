class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        int count;
        vector<int> list;
        for(int i=0;i<nums.size();i++)
        { count=0;
            for(int j=i+1;j<nums.size();j++)
                if(nums[j]<nums[i])
                    count++;
         for(int k=i-1;k>=0;k--)
             if(nums[k]<nums[i])
                    count++;
         list.push_back(count);
        }
        return list;
    }
};
