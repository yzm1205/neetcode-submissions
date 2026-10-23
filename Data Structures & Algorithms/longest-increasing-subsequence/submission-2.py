class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        stack = [nums[0]]
            # optimizing further. Since stack is sorted list we can use binary search

        
        for i in range(1, len(nums)):
            low = 0
            high= len(stack)
            while low < high:
                mid = (low + high)//2
                if nums[i] > stack[mid]:
                    low = mid+1
                else:
                    high = mid 

            if low == len(stack):
                stack.append(nums[i])
            elif low < len(stack):
                stack[low] = nums[i]
        return len(stack)
                



        # for i in range(1, len(nums)):
        #     for j in range(len(stack)):
        #         if nums[i] <= stack[j]:
        #             print(f"replacing-{stack[j]} with {nums[i]}")
        #             stack[j] = nums[i]
        #             break
        #         elif j == len(stack)-1:
        #             stack.append(nums[i])
        #             print(f"appending-{stack=}")
        #             break
        #         else:
        #             continue
        # return len(stack)