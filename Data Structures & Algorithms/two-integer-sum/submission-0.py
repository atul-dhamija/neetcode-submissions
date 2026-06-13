class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in nums[i+1:]:

                return [i, nums.index(compliment, i+1)]
        
        





# target = 7
# nums = [3,4,5,6]
# compliment_nums = [target - i for i in nums]
# # [4, 3, 2, 1]
# output_lst = []

# for i in nums:
#     if i in compliment_nums:
#         output_lst.append(compliment_nums.index(i))
        
# output_lst.sort()
# print(output_lst)
    