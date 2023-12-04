from collections import defaultdict

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = set()
        nums_dict = defaultdict(int)
        for index, value in enumerate(nums):
            nums_dict[value] +=1

        sorted_nums = sorted(nums)
        
        for fi, first in enumerate(sorted_nums):
            for second in sorted_nums[fi+1:]:
                target = -(first+second)

                nums_dict[first] -= 1
                nums_dict[second] -= 1
                if first+second > 0:
                    nums_dict[first] += 1
                    nums_dict[second] += 1    
                    break

                if target in nums_dict and nums_dict[target]>0:
                    answer.add(tuple(sorted([first, second, target])))
                
                nums_dict[first] += 1
                nums_dict[second] += 1            

        return [list(value) for value in answer]
s = Solution()
print(s.threeSum([-1,-2,-3,4,1,3,0,3,-2,1,-2,2,-1,1,-5,4,-3]))