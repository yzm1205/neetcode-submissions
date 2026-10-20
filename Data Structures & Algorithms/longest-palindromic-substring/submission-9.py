class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub_string = ""
        l = len(s)
        if l==1:
            return s
        # if len(set(s)) == 1:
        #     return s
        
        def check(lft,rht):
            while lft>=0 and rht<len(s) and s[lft] == s[rht]:
                lft -=1
                rht +=1
            
            return s[lft+1:rht]
        
        for i in range(len(s)):
            #odd len palindrome
            odd = check(i,i)
            even = check(i,i+1) # due to two center
            sub_string = max(sub_string, odd, even,key=len)


        return sub_string
        
        # start = 0
        # if s[0] == s[1]:
        #     start +=1
        #     sub_string = s[:2]

        # for i in range(start,l):
        #     left=1
        #     right=1
        #     temp=s[i]
        #     while i+right<=l-1:
        #         # when substring palindrome is ODD
        #         if i-left>=0 and s[i-left] == s[i+right]: 
        #             temp = s[i-left] + temp + s[i+right]
        #             sub_string = temp if len(sub_string) < len(temp) else sub_string
        #             left+=1
        #             right+=1
        #         # when substring palindrome is EVEN
        #         elif temp == s[i+right]:
        #             temp += s[i+right]
        #             print(temp,right)
        #             right+=1
        #             sub_string = temp if len(sub_string) < len(temp) else sub_string
                    
        #         else:
        #             sub_string = temp if len(sub_string) < len(temp) else sub_string
        #             break
        # return sub_string

        # # brute force
        # sub_string=""
        # l = len(s)
        # if l==1:
        #     return s
        # for i in range(l-1):
        #     for j in range(i+1,l+1):
        #         temp = s[i:j]
        #         if temp == temp[::-1]:
        #             sub_string = temp if len(sub_string) < len(temp) else sub_string
        # return sub_string
        