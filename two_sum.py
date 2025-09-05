# Probelm: Two Sum (LeetCode #1)
# Link: https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        # Make an empty dictionary (like a notebook)
        # It will map numbers we've seen -> their index (position in the list)
       seen = {}
       
       # Loop through the list, one number at a time
       # i = index (0, 1, 2...)
       # num = the actual number at that index
       for i, num in enumerate(nums):
           
        # Figure out what number we need to reach the target 
        complement = target - num
        
        #Step 1: Check if we already saw that partner earlier
        if complement in seen:
            # If yes -> reutrn the two positions
            return [seen[complement], i]
            
        #Step 2: Otherwise, write this number in the notebook 
        # so future numbers can pair with it
        seen[num] = i