"""009. 二叉树的右视图（#199）

思路见 thought.md：两种解法
  1) BFS：层序遍历，每层取最后一个节点           时间 O(n)，空间 O(w)
  2) DFS：先右后左，每层第一次到达时记录         时间 O(n)，空间 O(h)
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """BFS：逐层取最后一个。"""
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

    def rightSideViewDFS(self, root: Optional[TreeNode]) -> List[int]:
        """DFS：先右后左，每层第一次到达时记录。"""
        res = []

        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):      # 这一层还没记录过 → 当前节点就是最右
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res


def build_tree(vals):
    """层序数组（None 表示缺失）→ 树。"""
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals):
            v = vals[i]
            i += 1
            if v is not None:
                node.left = TreeNode(v)
                q.append(node.left)
        if i < len(vals):
            v = vals[i]
            i += 1
            if v is not None:
                node.right = TreeNode(v)
                q.append(node.right)
    return root


if __name__ == "__main__":
    cases = [
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, None, 2], [1, 2]),
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, 2, 3, 4], [1, 3, 4]),
        ([1, 2, 3], [1, 3]),
        ([1, 2, None, 3], [1, 2, 3]),
    ]

    ok_bfs = ok_dfs = 0
    for vals, want in cases:
        a = Solution().rightSideView(build_tree(vals))
        b = Solution().rightSideViewDFS(build_tree(vals))
        ok_bfs += a == want
        ok_dfs += b == want
        flag_a = "PASS" if a == want else "FAIL"
        flag_b = "PASS" if b == want else "FAIL"
        print(f"[BFS {flag_a}] [DFS {flag_b}] {str(vals):<30} -> {a} (want {want})")

    print(f"\nBFS {ok_bfs}/{len(cases)}  DFS {ok_dfs}/{len(cases)}")
