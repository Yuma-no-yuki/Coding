class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        l=""
        for i in s:
            if 97<=ord(i) and ord(i)<=122:
                l+=i
            elif 48<=ord(i) and ord(i)<=57:
                l+=i
        for i in range(len(l)):
            if l[i]!=l[-(i+1)]:
                return False
        return True
