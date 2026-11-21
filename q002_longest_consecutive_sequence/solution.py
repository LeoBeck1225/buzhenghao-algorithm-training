"""002. 最长连续序列（#128）

思路见 thought.md：集合去重 + 只从"没有前驱"的数当作起点向后延伸。
时间 O(n)，空间 O(n)。
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for x in s:
            if x - 1 in s:
                continue          # 不是起点，跳过，保证每个数只被数一次
            y = x
            while y + 1 in s:
                y += 1
            best = max(best, y - x + 1)
        return best


if __name__ == "__main__":
    cases = [
        ([], 0),
        ([1, 1, 1], 1),
        ([0, -1, 1], 3),
        ([100, 4, 200, 1, 3, 2], 4),
        ([5, 6, 7, 8], 4),
        ([1, 3, 5], 1),
    ]

    ok = 0
    for nums, want in cases:
        got = Solution().longestConsecutive(nums)
        passed = got == want
        ok += passed
        flag = "PASS" if passed else "FAIL"
        print(f"[{flag}] {str(nums):<22} -> {got} (want {want})")
    print(f"\n{ok}/{len(cases)} passed")
