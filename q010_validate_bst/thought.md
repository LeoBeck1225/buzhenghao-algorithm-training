# 010. 98. 验证二叉搜索树

- LeetCode: https://leetcode.cn/problems/validate-binary-search-tree/
- 分类: 二叉树
- 开始时间: ____-__-__ __:__
- 用时: ____ 分钟

## 我的第一想法（未使用 AI）

1. 采用LDR的顺序遍历判断，得到严格递增序列即可
2. 

## 复杂度

- 时间：O(n)
- 空间：O(h)

## 边界情况

- 
- [] → true
- [1] → true
- [2, 1, 3] → true
- [5, 4, 6, null, null, 3, 7] → false
- [5, 1, 4, null, null, 3, 6] → false
- [1, 1] → false
- [1, null, 1] → false

## 卡住的地方 / 想向 AI 验证的点

- DLR为何判断不了？
哪一种情况更省？
为何只比较父子节点是错的？