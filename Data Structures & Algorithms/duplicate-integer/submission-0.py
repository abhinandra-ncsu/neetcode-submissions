class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        new_dict = {}
        for num in nums:
            if num in new_dict.keys():
                new_dict[num] += 1
            else:
                new_dict[num] = 1
        

        for key, value in new_dict.items():
            if value != 1:
                return True
        return False
            