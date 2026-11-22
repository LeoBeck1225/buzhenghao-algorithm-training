"""020. 搜索旋转排序数组（#33）

思路见 thought.md：一次二分，每轮判断哪半有序，再看 target 是否落在有序半区。
时间 O(log n)，空间 O(1)。
"""

import random
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:                 # 左半有序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:                                        # 右半有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == "__main__":
    cases = [
        ([], 0, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([3, 1], 1, 1),
        ([5, 1, 3], 5, 0),
        ([5, 1, 3], 3, 2),
        ([1, 3], 3, 1),
    ]

    ok = 0
    for nums, target, want in cases:
        got = Solution().search(list(nums), target)
        passed = got == want
        ok += passed
        print(f"[{'PASS' if passed else 'FAIL'}] {str(nums):<24} target={target:<4} -> {got} (want {want})")
    print(f"\n{ok}/{len(cases)} passed")

    print("\n=== 随机对拍（n<=12，500 组）===")
    random.seed(33)
    bad = 0
    for _ in range(500):
        n = random.randint(0, 12)
        base = sorted(random.sample(range(0, 50), n))
        k = random.randint(0, n - 1) if n else 0
        nums = base[k:] + base[:k]
        target = random.choice(base + [random.randint(0, 60)] * 2) if base else random.randint(0, 60)
        got = Solution().search(list(nums), target)
        ref = nums.index(target) if target in nums else -1
        if got != ref:
            bad += 1
            print(f"  FAIL nums={nums} target={target} got={got} ref={ref}")
    print(f"对拍通过 {500 - bad}/500")
