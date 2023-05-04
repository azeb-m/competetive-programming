class Solution:
    def isValid(self, s: str) -> bool:
        mystack=[]
        dict={
            '[':']',
            '{':'}',
            '(':')'
        }
        opens=['[','{','(']
        i=0
        while i<len(s):
            if s[i] in opens:
                mystack.append(s[i])
            else :
                if mystack !=[]:
                    if dict[mystack.pop()] != s[i]:
                        return False
                else:
                    return False
            i=i+1
        if mystack==[]:
            return True
        else:
            return False
