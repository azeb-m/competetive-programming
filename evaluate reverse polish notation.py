class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack=[]
        operator=["+","-","*","/"]
        for x in tokens:
            if x in operator:
                y=int(mystack.pop())
                z=int(mystack.pop())
                if x == '+':
                    r= y + z
                elif x == '-':
                    r= z - y
                elif x== '/':
                    r= (z / y)
                    if r < 0:
                        r=ceil(r)
                    else:
                        r=floor(r)
                else:
                    r= y * z
                mystack.append(r)
            else:
                mystack.append(int(x))
        return mystack.pop()
