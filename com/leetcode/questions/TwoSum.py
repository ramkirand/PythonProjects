from typing import List
class TwoSum:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedarr = sorted(nums)
        current = 0
        last = len(nums) - 1
        whiler = True
        res = [0, 0]
        while whiler:
            if sortedarr[current] + sortedarr[last] > target:
                last -= 1
            elif sortedarr[current] + sortedarr[last] < target:
                current += 1
            else:
                whiler = False
        # get original index
        res[0] = nums.index(sortedarr[current])
        # in case of same number existing
        nums[res[0]] += 9
        res[1] = nums.index(sortedarr[last])
        return res