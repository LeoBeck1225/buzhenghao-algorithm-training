"""013. 零钱兑换（#322）

思路见 thought.md：完全背包 DP。
dp[i] = 凑出金额 i 的最少硬币数；dp[i] = 1 + min(dp[i-c])，c ∈ coins 且 c <= i。
不可达保持 inf，最后返回 -1。时间 O(amount × n)，空间 O(amount)。
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")
        dp = [0] + [INF] * amount

        for i in range(1, amount + 1):
            for c in coins:
                if c <= i and dp[i - c] + 1 < dp[i]:
                    dp[i] = dp[i - c] + 1

        return -1 if dp[amount] == INF else dp[amount]


def bfs_ref(coins, amount):
    """BFS 求最少枚数，用于对拍。"""
    if amount == 0:
        return 0
    seen = {0}
    frontier = [0]
    steps = 0
    while frontier:
        steps += 1
        nxt = []
        for cur in frontier:
            for c in coins:
                v = cur + c
                if v == amount:
                    return steps
                if v < amount and v not in seen:
                    seen.add(v)
                    nxt.append(v)
        frontier = nxt
    return -1


if __name__ == "__main__":
    cases = [
        (([], 0), 0),
        (([1], 0), 0),
        (([], 1), -1),
        (([1], 2), 2),
        (([2], 3), -1),
        (([1, 2, 5], 11), 3),
        (([2, 5, 10, 1], 27), 4),
        (([1, 3, 4], 6), 2),
        (([186, 419, 83, 408], 6249), 20),
        (([5], 5), 1),
        (([3, 7], 5), -1),
    ]

    ok = 0
    for (coins, amount), want in cases:
        got = Solution().coinChange(list(coins), amount)
        passed = got == want
        ok += passed
        flag = "PASS" if passed else "FAIL"
        print(f"[{flag}] coins={str(coins):<24} amount={amount:<6} -> {got} (want {want})")
    print(f"\n{ok}/{len(cases)} passed")

    print("\n=== 随机对拍（amount<=60，200 组）===")
    import random
    random.seed(3)
    bad = 0
    for _ in range(200):
        coins = random.sample(range(1, 20), random.randint(1, 4))
        amount = random.randint(0, 60)
        a = Solution().coinChange(coins, amount)
        b = bfs_ref(coins, amount)
        if a != b:
            bad += 1
            print(f"  FAIL coins={coins} amount={amount} dp={a} bfs={b}")
    print(f"对拍通过 {200 - bad}/200")
