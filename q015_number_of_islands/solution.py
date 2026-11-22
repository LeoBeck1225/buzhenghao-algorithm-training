"""015. 岛屿数量（#200）

思路见 thought.md：外层扫描，发现未访问的 '1' 就 count+1，
再用 BFS 把这座岛全部“淹”成 '0'（四连通）。
时间 O(m×n)，空间 O(m×n)（队列最坏情况）。
"""

import time
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0

        def flood(si: int, sj: int) -> None:
            """从 (si, sj) 出发，把整座岛淹成 '0'。"""
            grid[si][sj] = "0"                 # 起点先淹（入队前）
            q = deque([(si, sj)])
            while q:
                i, j = q.popleft()
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                        grid[ni][nj] = "0"     # 入队前就淹，避免重复入队
                        q.append((ni, nj))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1                 # 发现新岛，立即计数
                    flood(i, j)

        return count


def to_grid(rows):
    return [[str(x) for x in row] for row in rows]


if __name__ == "__main__":
    cases = [
        ([], 0),
        ([["0"]], 0),
        ([["1"]], 1),
        ([["1", "1"], ["1", "1"]], 1),
        ([["1", "0", "1"]], 2),
        ([["1", "1", "1"], ["0", "0", "0"], ["1", "1", "1"]], 2),
        ([["1", "1", "0"], ["0", "1", "0"], ["0", "0", "1"]], 2),
        ([["1", "0", "1", "1"], ["1", "1", "0", "1"],
          ["0", "0", "1", "0"], ["1", "1", "0", "0"]], 4),
    ]

    ok = 0
    for g, want in cases:
        got = Solution().numIslands([row[:] for row in g])
        passed = got == want
        ok += passed
        flag = "PASS" if passed else "FAIL"
        print(f"[{flag}] {str(g)[:60]:<62} -> {got} (want {want})")
    print(f"\n{ok}/{len(cases)} passed")

    print("\n=== 300x300 全 '1' 压测 ===")
    big = [["1"] * 300 for _ in range(300)]
    t = time.time()
    r = Solution().numIslands(big)
    print(f"结果 {r}，耗时 {(time.time() - t) * 1000:.0f} ms")

    print("\n=== 300x300 棋盘格（最坏情况：每个格子都是独立岛）===")
    chess = [[("1" if (i + j) % 2 == 0 else "0") for j in range(300)] for i in range(300)]
    t = time.time()
    r = Solution().numIslands(chess)
    print(f"结果 {r}，耗时 {(time.time() - t) * 1000:.0f} ms")
