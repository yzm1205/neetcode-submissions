class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix_prod = [1]*n
        prefix_prod = [1]* n

        prefix = 1
        for i in range(1,n):
            prefix *= nums[i-1]
            prefix_prod[i] = prefix
        
        suffix = 1
        for j in range(n-2,-1,-1):
            # print(f"{nums[j]=}")
            suffix *= nums[j+1]
            suffix_prod[j] = suffix

        # print(f"{prefix_prod=}")
        # print(f"{suffix_prod=}")

        prod = []
        for i in range(n):
            prod.append(prefix_prod[i] * suffix_prod[i])
        
        return prod


        