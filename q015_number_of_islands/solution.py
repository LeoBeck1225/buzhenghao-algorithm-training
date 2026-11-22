"""015. 岛屿数量（#200）

思路见 thought.md：外层扫描，遇到未访问的 '1' 就 count+1，
再用 BFS 把整座岛淹成 '0'（四连通）。
时间 O(m×n)，空间 O(m×n)。
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
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1":
                    continue

                count += 1
                grid[i][j] = "0"
                q = deque([(i, j)])

                while q:
                    x, y = q.popleft()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                            grid[nx][ny] = "0"
                            q.append((nx, ny))

        return count


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
        print(f"[{flag}] {str(g)[:58]:<60} -> {got} (want {want})")
    print(f"\n{ok}/{len(cases)} passed")

    print("\n=== 压测 ===")
    big = [["1"] * 300 for _ in range(300)]
    t = time.time()
    r1 = Solution().numIslands(big)
    t1 = (time.time() - t) * 1000

    chess = [[("1" if (i + j) % 2 == 0 else "0") for j in range(300)] for i in range(300)]
    t = time.time()
    r2 = Solution().numIslands(chess)
    t2 = (time.time() - t) * 1000

    print(f"300x300 全 '1'   -> {r1} 座岛，{t1:.0f} ms")
    print(f"300x300 棋盘格   -> {r2} 座岛，{t2:.0f} ms")
