class Solution:
    def isValid(self, s: str) -> bool:
        for i in s:
            for j in range(len(s)-1,0,-1):
                if i==s[j]:
                    return True
                    break
                else:
                    return False
o=Solution()
s="()"
o.isValid(s)