# link => https://leetcode.com/problems/longest-consecutive-sequence/


class Solution:
    # using disjoint set concept
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0

        nums = set(nums)
        repr_ = {x: x for x in nums}
        rank = {x: 1 for x in nums}

        for x in nums:
            if x-1 in repr_:
                i = x
                while repr_[i] != i:
                    i = repr_[i]
                repr_[x-1] = i
                rank[i] += rank[x-1]

        return max(rank.values())
    '''
    # using set and intelligent sequence building
    def longestConsecutive(self, nums) -> int:

        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
    '''


print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
