# 算法训练作业 · AI 辅助编程

> 20 道 Medium 算法题。每题**先独立写思路**，再借助 Coding Agent 完成，
> 保留完整的 AI 交互记录与测试结果。

- 姓名：卜郑豪
- GitHub：[@LeoBeck1225](https://github.com/LeoBeck1225)
- 开始日期：2026-11-21

## 题目清单

| # | 题目 | 分类 | 难度 | LeetCode | 状态 |
|---|------|------|------|----------|------|
| 001 | 49. 字母异位词分组 | 哈希 | Medium | [链接](https://leetcode.cn/problems/group-anagrams/) | ✅ AC（18 ms / 击败 22.5%） |
| 002 | 128. 最长连续序列 | 哈希 | Medium | [链接](https://leetcode.cn/problems/longest-consecutive-sequence/) | ✅ AC（48 ms / 击败 67.1%） |
| 003 | 15. 三数之和 | 双指针 | Medium | [链接](https://leetcode.cn/problems/3sum/) | ✅ AC（501 ms / 击败 74.8%） |
| 004 | 11. 盛最多水的容器 | 双指针 | Medium | [链接](https://leetcode.cn/problems/container-with-most-water/) | ✅ AC（115 ms / 击败 53.4%） |
| 005 | 3. 无重复字符的最长子串 | 滑动窗口 | Medium | [链接](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) | ✅ AC（266 ms / 击败 92.8%） |
| 006 | 438. 找到字符串中所有字母异位词 | 滑动窗口 | Medium | [链接](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) | ✅ AC（43 ms / 击败 54.4%） |
| 007 | 19. 删除链表的倒数第 N 个结点 | 链表 | Medium | [链接](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/) | ✅ AC（0 ms / 击败 100%） |
| 008 | 102. 二叉树的层序遍历 | 二叉树 | Medium | [链接](https://leetcode.cn/problems/binary-tree-level-order-traversal/) | ✅ AC（0 ms / 击败 100%） |
| 009 | 199. 二叉树的右视图 | 二叉树 | Medium | [链接](https://leetcode.cn/problems/binary-tree-right-side-view/) | ✅ AC（0 ms / 击败 100%） |
| 010 | 98. 验证二叉搜索树 | 二叉树 | Medium | [链接](https://leetcode.cn/problems/validate-binary-search-tree/) | ⬜ 未开始 |
| 011 | 5. 最长回文子串 | 动态规划 | Medium | [链接](https://leetcode.cn/problems/longest-palindromic-substring/) | ⬜ 未开始 |
| 012 | 198. 打家劫舍 | 动态规划 | Medium | [链接](https://leetcode.cn/problems/house-robber/) | ⬜ 未开始 |
| 013 | 322. 零钱兑换 | 动态规划 | Medium | [链接](https://leetcode.cn/problems/coin-change/) | ⬜ 未开始 |
| 014 | 300. 最长递增子序列 | 动态规划 | Medium | [链接](https://leetcode.cn/problems/longest-increasing-subsequence/) | ⬜ 未开始 |
| 015 | 200. 岛屿数量 | 图/DFS | Medium | [链接](https://leetcode.cn/problems/number-of-islands/) | ⬜ 未开始 |
| 016 | 207. 课程表 | 图/拓扑排序 | Medium | [链接](https://leetcode.cn/problems/course-schedule/) | ⬜ 未开始 |
| 017 | 208. 实现 Trie (前缀树) | 设计 | Medium | [链接](https://leetcode.cn/problems/implement-trie-prefix-tree/) | ⬜ 未开始 |
| 018 | 146. LRU 缓存 | 设计 | Medium | [链接](https://leetcode.cn/problems/lru-cache/) | ⬜ 未开始 |
| 019 | 56. 合并区间 | 排序 | Medium | [链接](https://leetcode.cn/problems/merge-intervals/) | ⬜ 未开始 |
| 020 | 33. 搜索旋转排序数组 | 二分 | Medium | [链接](https://leetcode.cn/problems/search-in-rotated-sorted-array/) | ⬜ 未开始 |

## 仓库结构

```
.
├── README.md            # 总览与进度
├── 对话/                # 与 AI 的完整对话记录（按日期追加）
│   ├── 对话1.md         # 2026-11-21
│   └── 对话2.md         # 2026-11-22
└── qXXX_slug/           # 每道题
    ├── thought.md       # 先写的解题思路（提交时间早于代码）
    ├── ai_chat.md       # 该题的 AI 交互摘要（索引）
    ├── solution.py      # 可独立运行的实现 + 自测
    └── result.png       # LeetCode AC 截图
```

> `对话/` 为**完整往返记录**（用户原文 + AI 回复）；
> `ai_chat.md` 是同一对话的**结构化摘要**，便于按题检索。

## 目录约定

```
qXXX_slug/
├── thought.md    # 先写：独立思考的思路（提交时间早于代码）
├── ai_chat.md    # AI 交互链接 + 提示词 + 输出摘要
├── solution.py   # 最终代码（可独立运行）
└── result.png    # LeetCode AC 截图（可选，建议放）
```

## 每题提交流程

1. 读题 → 写 `thought.md` → `git commit -m "qXXX: 独立思路"`
2. 带思路与 AI 讨论（要提示 / 要审查，不要整段代码）→ 记录到 `ai_chat.md`
3. 自己实现 `solution.py` → 本地测试 → LeetCode AC → 截图
4. `git commit -m "qXXX: 实现完成，AC 通过"`

## 进度

- 已完成：9 / 20
