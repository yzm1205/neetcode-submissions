class Solution:
    def countSubstrings(self, s: str) -> int:

        if len(s) == 1:
            return 1
        total = 0
        def check(l,r):
            temp_count = 0
            while l>=0 and r <len(s) and s[l] == s[r]:
                l -=1
                r +=1
                temp_count +=1
                # print(f"{s[l-1:r]=}")
            return temp_count

        for i in range(len(s)):
            # print(f"{i,s[i]=}")
            odd = check(i,i)
            # print(f"{odd=}")
            even = check(i,i+1)
            # print(f"{even=}")
            total += odd + even
        return total


        