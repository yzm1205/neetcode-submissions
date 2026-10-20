class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        total_max = max(nums)
        max_product = 1
        min_product = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                max_product = 1
                min_product = 1
                continue

            temp_max = max_product
            max_product= max(nums[i], max_product*nums[i],min_product*nums[i])
            min_product = min(nums[i], min_product*nums[i], temp_max*nums[i])
            total_max = max(max_product, total_max)
        return total_max

        