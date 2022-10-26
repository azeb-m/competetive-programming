class Solution {
public:
    string sortSentence(string s) {
        vector<string>list;
        vector<string>list2;
        string str="";
        string result1="";
        string result2="";
        string resultf="";
        for(int i=0;i<s.size();i++)
        {
            if(s[i]!=' ')
            {
                str+=s[i];
            }
            else 
            {
                list.push_back(str);
                str="";
            }
        }
        list.push_back(str);
     for(int i=0;i<list.size()-1;i++)
         for(int j=i+1;j<list.size();j++)
             if(list[j].back()<list[i].back())
             {
                 string temp=list[i];
                 list[i]=list[j];
                 list[j]=temp;
             }
        int i=0;
        while(i<list.size())
        {  
            result1.append(list[i]);
            i++;
        
        }
        for(int i=0;i<result1.size()-1;i++)
        {
            if(result1[i]!='1'&&result1[i]!='2'&&result1[i]!='3'&&result1[i]!='4'&&result1[i]!='5'&&result1[i]!='6'&&result1[i]!='7'&&result1[i]!='8'&&result1[i]!='9')
            {
               result2+=result1[i];
            }
            
            else 
            {
                result2+=' ';
                list2.push_back(result2);
                    result2="";
            }
        } list2.push_back(result2);
        int j=0;
        while(j<list2.size())
        {  
            resultf.append(list2[j]);
            j++;
        
        }
       
        return resultf;
    }
};
