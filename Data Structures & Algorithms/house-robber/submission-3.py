class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])

        # memo = [[-1]*(len(nums)+2) for _ in range(len(nums)+2)]
        memo=[-1]*(len(nums)+3)
        def trav(n):
            if n==len(nums):
                return 0
            if memo[n] != -1:
                return memo[n]
            memo[n]= nums[n] + max(trav(n+2),trav(n+3)) if n+3 <= len(nums) else nums[n]
            return memo[n]

        return max(trav(0),trav(1))

        