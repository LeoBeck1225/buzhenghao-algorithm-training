"""010. 验证二叉搜索树（#98）

思路见 thought.md：中序（LDR）严格递增。
两种实现：
  1) 中序 + prev：边走边比较，空间 O(h)
  2) 上下界递归：每个节点必须落在祖先给的 (low, high) 内，空间 O(h)
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """中序 + prev 变量。"""
        prev = float("-inf")

        def dfs(node: Optional[TreeNode]) -> bool:
            nonlocal prev
            if not node:
                return True
            if not dfs(node.left):
                return False
            if node.val <= prev:          # 必须严格递增
                return False
            prev = node.val
            return dfs(node.right)

        return dfs(root)

    def isValidBSTByBounds(self, root: Optional[TreeNode]) -> bool:
        """上下界递归。"""
        def check(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (check(node.left, low, node.val)
                    and check(node.right, node.val, high))

        return check(root, float("-inf"), float("inf"))


def build_tree(vals):
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
        ([], True),
        ([1], True),
        ([2, 1, 3], True),
        ([5, 4, 6, None, None, 3, 7], False),
        ([5, 1, 4, None, None, 3, 6], False),
        ([1, 1], False),
        ([1, None, 1], False),
        ([10, 5, 15, None, None, 6, 20], False),   # 专治“只比较父子”的陷阱
        ([2147483647], True),                      # int 上界
    ]

    ok_a = ok_b = 0
    for vals, want in cases:
        a = Solution().isValidBST(build_tree(vals))
        b = Solution().isValidBSTByBounds(build_tree(vals))
        ok_a += a == want
        ok_b += b == want
        print(f"[中序 {'PASS' if a == want else 'FAIL'}] "
              f"[上下界 {'PASS' if b == want else 'FAIL'}] {str(vals):<36} -> {a} (want {want})")
    print(f"\n中序 {ok_a}/{len(cases)}   上下界 {ok_b}/{len(cases)}")
