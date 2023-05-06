class Solution:
    def reverseParentheses(self, s: str) -> str:
        mystack=[]
        st=''
        dict={'(':')'}
        for x in s:
            if x != dict['(']:
                mystack.append(x)
            else:  
                temp=[]
                y=mystack.pop()
                while y !='(':
                    temp.append(y)
                    y=mystack.pop()
                for z in temp:
                    mystack.append(z)
        for i in mystack:
            st += i
        return st
