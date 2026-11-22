"""019. 合并区间（#56）

思路见 thought.md：按左端点排序，维护当前合并区间，与后一个区间的左端点比较。
时间 O(n log n)，空间 O(n)。
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for l, r in intervals[1:]:
            if l <= merged[-1][1]:                  # 相接也算重叠
                merged[-1][1] = max(merged[-1][1], r)
            else:
                merged.append([l, r])
        return merged


def naive(intervals):
    """O(n²) 暴力合并，用于对拍。"""
    res = [list(x) for x in intervals]
    changed = True
    while changed:
        changed = False
        n = len(res)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = res[i], res[j]
                if not (a[1] < b[0] or b[1] < a[0]):     # 有交集或相接
                    res[i] = [min(a[0], b[0]), max(a[1], b[1])]
                    res.pop(j)
                    changed = True
                    break
            if changed:
                break
    return sorted(res)


if __name__ == "__main__":
    cases = [
        ([], []),
        ([[1, 3]], [[1, 3]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [2, 3]], [[1, 4]]),
        ([[1, 4], [0, 4]], [[0, 4]]),
        ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[2, 3], [1, 4]], [[1, 4]]),
    ]

    ok = 0
    for iv, want in cases:
        got = Solution().merge([x[:] for x in iv])
        passed = got == want
        ok += passed
        print(f"[{'PASS' if passed else 'FAIL'}] {str(iv):<46} -> {got}")
    print(f"\n{ok}/{len(cases)} passed")

    print("\n=== 随机对拍（n<=8，200 组）===")
    import random
    random.seed(21)
    bad = 0
    for _ in range(200):
        n = random.randint(0, 8)
        iv = []
        for _ in range(n):
            a = random.randint(0, 10)
            b = a + random.randint(0, 5)
            iv.append([a, b])
        got = Solution().merge([x[:] for x in iv])
        ref = naive(iv)
        if got != ref:
            bad += 1
            print(f"  FAIL {iv} got={got} ref={ref}")
    print(f"对拍通过 {200 - bad}/200")
