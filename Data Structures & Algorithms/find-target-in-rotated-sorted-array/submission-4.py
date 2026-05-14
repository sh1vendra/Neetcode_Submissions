class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l<=r: #
            m = (l+r)//2
            if target == nums[m]:
                return m
            #we are in L array and wanna go to R array
            if nums[m] >= nums[l]:#
                if target > nums[m] or target < nums[l]:
                    #simple bs logic or sorted array logic
                    l = m+1
                else: 
                    r = m-1
            #We are in R array and wanna go to L array
            else:
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else:
                    l = m+1
        return -1 

