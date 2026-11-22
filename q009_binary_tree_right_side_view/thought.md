# 009. 二叉树的右视图（#199）

- LeetCode: https://leetcode.cn/problems/binary-tree-right-side-view/
- 分类: 二叉树
- 开始时间: 2026-11-22 11:10
- 用时: 约 25 分钟

## 我的第一想法（未使用 AI，原文保留）

1. 使用层序遍历，最后右节点替换掉左节点
2. 或者是使用DFS？递归右子树再递归左子树？

## 复杂度

- 时间：O(n)
- 空间：O(n)

## 边界情况

- [] → []
- [1] → [1]
- [1, 2] → [1, 2]
- [1, null, 2] → [1, 2]
- [1, 2, 3, null, 5, null, 4] → [1, 3, 4]
- [1, 2, 3, 4] → [1, 3, 4]
- [1, 2, 3] → [1, 3]
- [1, 2, null, 3] → [1, 2, 3]（全是左链，右视图就是整条链）

## 卡住的地方 / 想向 AI 验证的点

- 能用DFS吗？我觉得这个思维更加直观

## 经 AI 提示后的补充（这部分不是原话，单独记录）

### ① BFS 的表述修正

不是"最后右节点替换掉左节点"，而是「**层序遍历，每层只取最后一个节点**」：

```
while q:
    size = len(q)
    for i in range(size):
        node = q.popleft()
        if i == size - 1: res.append(node.val)   # 本层最后一个
        if node.left:  q.append(node.left)
        if node.right: q.append(node.right)
```

### ② DFS 可以，而且更短

先右后左递归，**每层第一次到达时记录**：

```
def dfs(node, depth):
    if not node: return
    if depth == len(res):        # 这层还没记过 → 当前就是最右
        res.append(node.val)
    dfs(node.right, depth + 1)   # 先右
    dfs(node.left,  depth + 1)   # 后左
```

**为什么对**：先遍历右子树，所以每一层第一个被访问到的节点必然是该层最右节点；
`depth == len(res)` 表示"这一层还没被记录过"。

### ③ 两种解法对比

| | BFS（层序） | DFS（先右后左） |
|---|---|---|
| 核心 | 每层取 `level[-1]` | 每层首次到达时记录 |
| 时间 | O(n) | O(n) |
| 空间 | **O(w)**（最宽一层） | **O(h)**（递归栈，树高） |
| 代码量 | 略多（要分层） | 更短 |
| 风险 | 无 | 极深的树可能超递归深度（可 `setrecursionlimit` 或改迭代） |

### ④ 复杂度修正

原稿写的是 O(n)/O(n)，更准确是：
- BFS：时间 O(n)，空间 **O(w)**
- DFS：时间 O(n)，空间 **O(h)**（最坏退化成链时 h = n）

### ⑤ 提交结果

两种解法都提交通过（217/217）：
- BFS：**0 ms，击败 100%**，12.11 MB（击败 98.7%）
- DFS：1 ms，击败 10.7%，19.27 MB
