class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force
        sub_string=""
        l = len(s)
        if l==1:
            return s

        for i in range(l-1):
            for j in range(i+1,l+1):
                temp = s[i:j]
                if temp == temp[::-1]:
                    sub_string = temp if len(sub_string) < len(temp) else sub_string
        return sub_string
        