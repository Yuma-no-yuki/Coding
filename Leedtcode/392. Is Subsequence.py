class Solution(object):
    def isSubsequence(self, s, t):
        for i in t:
            if s == "":
                return True
            elif i==s[0]:
                s=s[1:]
        if s == "":
            return True
        else:
            return False
