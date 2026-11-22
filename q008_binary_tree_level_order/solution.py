"""008. 二叉树的层序遍历（#102）

思路见 thought.md：BFS + 队列，每轮先记录队列长度作为本层节点数。
时间 O(n)，空间 O(n)（最宽一层）。
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res


def build_tree(vals):
    """把 LeetCode 的层序数组（None 表示缺失）转成树。"""
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
        ([1], [[1]]),
        ([1, 2], [[1], [2]]),
        ([1, None, 2], [[1], [2]]),
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1, 2, None, 3], [[1], [2], [3]]),
        ([1, None, 2, None, 3], [[1], [2], [3]]),
    ]

    ok = 0
    for vals, want in cases:
        got = Solution().levelOrder(build_tree(vals))
        passed = got == want
        ok += passed
        flag = "PASS" if passed else "FAIL"
        print(f"[{flag}] {str(vals):<36} -> {got}")
    print(f"\n{ok}/{len(cases)} passed")
