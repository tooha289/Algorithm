from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = defaultdict(list)
        for index, value in enumerate(nums):
            nums_dict[value].append(index)

        for k, v in nums_dict.items():
            diff = target-k
            if diff in nums_dict and diff != k:
                return [v[0], nums_dict[diff][0]]
            if diff in nums_dict and len(nums_dict[diff]) > 1:
                return nums_dict[diff][0:2]


s = Solution()
print(s.twoSum([3,3], 6))