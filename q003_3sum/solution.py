"""003. 三数之和（#15）

思路见 thought.md：排序 + 固定 i + 双指针，记录后两边同时跳过重复值。
时间 O(n²)，空间 O(1)（不计返回结果）。
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            if nums[i] > 0:
                break                      # 已排序，后面不可能凑出 0
            if i > 0 and nums[i] == nums[i - 1]:
                continue                   # 跳过重复的 i
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return res


def _norm(triples):
    return sorted(tuple(sorted(t)) for t in triples)


if __name__ == "__main__":
    cases = [
        ([], []),
        ([0], []),
        ([0, 0], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([1, 2, 3], []),
        ([-3, -2, -1], []),
        ([-1, -1, -1, 2, 2], [[-1, -1, 2]]),
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([1, -1, 0], [[-1, 0, 1]]),
        ([100000, -100000, 0], [[-100000, 0, 100000]]),
        ([0] * 3000, [[0, 0, 0]]),
    ]

    ok = 0
    for nums, want in cases:
        got = Solution().threeSum(list(nums))
        passed = _norm(got) == _norm(want)
        ok += passed
        flag = "PASS" if passed else "FAIL"
        label = f"{nums[:6]}{'...' if len(nums) > 6 else ''}"
        print(f"[{flag}] {label:<28} -> {got}")
    print(f"\n{ok}/{len(cases)} passed")
