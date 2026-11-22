"""004. 盛最多水的容器（#11）

思路见 thought.md：双指针从两端向中间收，每次移动较短的一边。
时间 O(n)，空间 O(1)。
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        best = 0
        while i < j:
            best = max(best, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return best


if __name__ == "__main__":
    cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([1, 1, 1, 1], 3),
        ([0, 1, 0], 0),
        ([2, 3, 4, 5, 18, 17, 6], 17),
        ([1, 2, 4, 3], 4),
        ([2, 3, 10, 5, 7, 8, 9], 36),
    ]

    ok = 0
    for h, want in cases:
        got = Solution().maxArea(list(h))
        passed = got == want
        ok += passed
        flag = "PASS" if passed else "FAIL"
        print(f"[{flag}] {str(h):<28} -> {got} (want {want})")
    print(f"\n{ok}/{len(cases)} passed")
