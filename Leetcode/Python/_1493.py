class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        max_len, i = 0, 0

        for j in range(len(nums)):
            if nums[j] == 0:
                k -= 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
            max_len = max(max_len, j - i)

        return max_len
