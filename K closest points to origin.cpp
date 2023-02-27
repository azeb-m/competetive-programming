class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<vector<double>>point;
        for(int m=0;m<points.size();m++)
        {   vector<double>tempo;
            tempo.push_back(points[m][0]);
            tempo.push_back(points[m][1]);
            point.push_back(tempo);
        }
        for(int i=0;i<point.size();i++)
        {
            point[i].push_back(sqrt(pow(point[i][0],2)+pow(point[i][1],2)));
        }
            for(int j=0;j<point.size()-1;j++)
            {
                int min=j;
                for(int k=j+1;k<point.size();k++)
                {
                    if(point[k][2]<point[min][2])
                    {
                     min=k;
                    }
                }
                if(min!=j)
                {
                    vector<double> temp;
                    temp.push_back(point[min][0]);
                    temp.push_back(point[min][1]);
                    temp.push_back(point[min][2]);
                    
                    point[min][0]=point[j][0];
                    point[min][1]=point[j][1];
                    point[min][2]=point[j][2];
                    
                    point[j][0]=temp[0];
                    point[j][1]=temp[1];
                    point[j][2]=temp[2];
                    
                }
            }
        vector<vector<int>>result;
        int n=0;
        while(n<k)
        {
            vector<int>tempo;
            tempo.push_back(point[n][0]);
            tempo.push_back(point[n][1]);
            result.push_back(tempo);
           
            n++;
        
        }
        return result;
        
        
    }
};
