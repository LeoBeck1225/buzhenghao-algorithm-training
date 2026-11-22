"""014. 最长递增子序列（#300）

思路见 thought.md：dp[i] = 以 nums[i] 结尾的 LIS 长度，答案 max(dp)。
两版：O(n²) 的朴素 DP、O(n log n) 的 tails + 二分。
"""

import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """O(n²)：dp[i] = 以 i 结尾的最长递增子序列长度。"""
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLISBinary(self, nums: List[int]) -> int:
        """O(n log n)：tails[k] = 长度 k+1 的递增子序列的最小结尾。"""
        tails = []
        for x in nums:
            pos = bisect.bisect_left(tails, x)   # 严格递增 → left
            if pos == len(tails):
                tails.append(x)
            else:
                tails[pos] = x
        return len(tails)


def brute(nums):
    """暴力：枚举所有子序列判断递增（n 很小才用）。"""
    n = len(nums)
    best = 0
    for mask in range(1 << n):
        seq = [nums[i] for i in range(n) if mask >> i & 1]
        if all(seq[k] < seq[k + 1] for k in range(len(seq) - 1)):
            best = max(best, len(seq))
    return best


if __name__ == "__main__":
    cases = [
        ([], 0),
        ([1], 1),
        ([2, 2], 1),
        ([7, 7, 7, 7], 1),
        ([1, 2, 3, 4, 5], 5),
        ([5, 4, 3, 2, 1], 1),
        ([3, 1, 2], 2),
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([1, 2, 3, 0], 3),          # dp[-1] 陷阱：最长不在末尾
        ([0], 1),
    ]

    ok_a = ok_b = 0
    for nums, want in cases:
        a = Solution().lengthOfLIS(list(nums))
        b = Solution().lengthOfLISBinary(list(nums))
        ok_a += a == want
        ok_b += b == want
        print(f"[DP {'PASS' if a == want else 'FAIL'}] "
              f"[二分 {'PASS' if b == want else 'FAIL'}] {str(nums):<30} -> {a} / {b} (want {want})")
    print(f"\nDP {ok_a}/{len(cases)}   二分 {ok_b}/{len(cases)}")

    print("\n=== 随机对拍（n<=10，200 组）===")
    import random
    random.seed(5)
    bad = 0
    for _ in range(200):
        nums = [random.randint(-5, 10) for _ in range(random.randint(0, 10))]
        ref = brute(nums)
        a = Solution().lengthOfLIS(list(nums))
        b = Solution().lengthOfLISBinary(list(nums))
        if a != ref or b != ref:
            bad += 1
            print(f"  FAIL {nums} dp={a} bin={b} ref={ref}")
    print(f"对拍通过 {200 - bad}/200")
