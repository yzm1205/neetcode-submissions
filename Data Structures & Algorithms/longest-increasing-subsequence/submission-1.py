class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        stack = [nums[0]]

        for i in range(1, len(nums)):
            for j in range(len(stack)):
                if nums[i] <= stack[j]:
                    print(f"replacing-{stack[j]} with {nums[i]}")
                    stack[j] = nums[i]
                    break
                elif j == len(stack)-1:
                    stack.append(nums[i])
                    print(f"appending-{stack=}")
                    break
                else:
                    continue
                
        # print(f"{stack=}") 
        return len(stack)