"""016. 课程表（#207）

思路见 thought.md：判环。
  1) Kahn：入度 + 队列，最后看 processed == n
  2) DFS 三色标记：0 未访问 / 1 访问中 / 2 已完成，遇到 1 即有环
时间 O(V+E)，空间 O(V+E)。
"""

import sys
import time
from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """Kahn：入度 + 队列。"""
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        seen = 0

        while q:
            u = q.popleft()
            seen += 1
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return seen == numCourses

    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """DFS 三色标记。"""
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses

        def dfs(u: int) -> bool:
            state[u] = 1
            for v in graph[u]:
                if state[v] == 1:
                    return False
                if state[v] == 0 and not dfs(v):
                    return False
            state[u] = 2
            return True

        return all(dfs(i) for i in range(numCourses) if state[i] == 0)


if __name__ == "__main__":
    cases = [
        (1, [], True),
        (2, [], True),
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (3, [[0, 1], [1, 2]], True),
        (3, [[0, 1], [1, 2], [2, 0]], False),
        (2000, [[i, i - 1] for i in range(1, 2000)], True),
        (3, [[1, 0], [1, 2], [0, 1]], False),
    ]

    print("=== Kahn ===")
    ok = 0
    for n, pre, want in cases:
        got = Solution().canFinish(n, [p[:] for p in pre])
        ok += got == want
        print(f"[{'PASS' if got == want else 'FAIL'}] n={n:<5} edges={len(pre):<5} -> {got} (want {want})")
    print(f"Kahn {ok}/{len(cases)}")

    print("\n=== DFS（当前递归上限 %d）===" % sys.getrecursionlimit())
    ok = 0
    for n, pre, want in cases:
        try:
            got = Solution().canFinishDFS(n, [p[:] for p in pre])
            good = got == want
        except RecursionError:
            got = "RecursionError"
            good = False
        ok += good
        print(f"[{'PASS' if good else 'FAIL'}] n={n:<5} edges={len(pre):<5} -> {got} (want {want})")
    print(f"DFS {ok}/{len(cases)}")

    print("\n=== 压测：2000 节点、5000 条边 ===")
    import random
    random.seed(9)
    n = 2000
    pre = []
    for _ in range(5000):
        a = random.randrange(n)
        b = random.randrange(n)
        if a != b:
            pre.append([a, b])
    t = time.time()
    r = Solution().canFinish(n, pre)
    print(f"Kahn: {r}, {(time.time() - t) * 1000:.0f} ms")
