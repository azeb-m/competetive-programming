class Solution {
public:
    vector<string> fizzBuzz(int n) {
      vector<string> collector;
        for(int i=1;i<=n;i++)
        {
            if((i%3==0)&&(i%5==0))
                collector.push_back("FizzBuzz");
           else if(i%3==0)
                collector.push_back("Fizz");
           else if(i%5==0)
                collector.push_back("Buzz");
            else collector.push_back(to_string(i));
        }
        for(auto x:collector)
            cout<<x<<",";
        return collector;
        
    }
};
