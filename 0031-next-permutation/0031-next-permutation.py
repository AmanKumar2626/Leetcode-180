class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        for i in range(len(nums)-1, 0,-1):
            if(nums[i] > nums[i-1]):
                for j in range(len(nums) -1, i-1,-1):
                    if(nums[j] > nums[i-1]):
                        nums[i-1], nums[j] =  nums[j], nums[i-1]
                        nums[i:] = reversed(nums[i:])
                        return
        return nums.reverse()           
            
        

        