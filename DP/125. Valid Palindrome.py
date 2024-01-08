class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        l=""
        for i in s:
            if 97<=ord(i) and ord(i)<=122:
                l+=i
            elif 48<=ord(i) and ord(i)<=57:
                l+=i
        print(l)
        for i in range(len(l)):
            if l[i]!=l[-(i+1)]:
                return False
        return True
        # for i in range(int((len(s)-1)/2)):
        #     print(s[i],s[-(i+1)])
print(Solution().isPalindrome("0P"))