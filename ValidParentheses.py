class Solution:
    def checkValidString(self, s: str) -> bool:
        lc=0
        rc=0
        for i in s:
            if i=='(' or i=='*':
                lc+=1
            else:
                lc-=1
            if lc<0:
                return False
        if lc==0:
            return True
        for i in range(len(s)-1,-1,-1):
            if s[i]==")" or s[i]=='*':
                rc+=1
            else:
                rc-=1
            if rc<0:
                return False
        return True
