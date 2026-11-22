"""012. 打家劫舍（#198）

思路见 thought.md：dp[i] = 前 i 间的最大值 = max(dp[i-1], dp[i-2] + nums[i])。
两个版本：滚动变量（空间 O(1)）、DP 数组（空间 O(n)）。
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """滚动变量版：时间 O(n)，空间 O(1)。"""
        prev2 = 0
        prev1 = 0
        for x in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + x)
        return prev1

    def robDpArray(self, nums: List[int]) -> int:
        """DP 数组版：dp[i] = 前 i 间的最大。时间 O(n)，空间 O(n)。"""
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[n]


def brute(nums):
    """暴力枚举所有不取相邻的子集，仅用于对拍。"""
    n = len(nums)
    best = 0
    for mask in range(1 << n):
        if mask & (mask << 1):
            continue
        best = max(best, sum(nums[i] for i in range(n) if mask >> i & 1))
    return best


if __name__ == "__main__":
    cases = [
        ([], 0),
        ([5], 5),
        ([0], 0),
        ([1, 2], 2),
        ([2, 1], 2),
        ([1, 3, 1], 3),
        ([2, 1, 1, 2], 4),
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([5, 5, 5, 5], 10),
    ]

    ok_a = ok_b = 0
    for nums, want in cases:
        a = Solution().rob(list(nums))
        b = Solution().robDpArray(list(nums))
        ok_a += a == want
        ok_b += b == want
        print(f"[滚动 {'PASS' if a == want else 'FAIL'}] "
              f"[数组 {'PASS' if b == want else 'FAIL'}] {str(nums):<22} -> {a} (want {want})")
    print(f"\n滚动 {ok_a}/{len(cases)}   数组 {ok_b}/{len(cases)}")

    print("\n=== 随机对拍（长度<=12，200 组）===")
    import random
    random.seed(11)
    bad = 0
    for _ in range(200):
        nums = [random.randint(0, 20) for _ in range(random.randint(0, 12))]
        ref = brute(nums)
        a = Solution().rob(list(nums))
        b = Solution().robDpArray(list(nums))
        if a != ref or b != ref:
            bad += 1
            print(f"  FAIL {nums} 滚动={a} 数组={b} ref={ref}")
    print(f"对拍通过 {200 - bad}/200")
