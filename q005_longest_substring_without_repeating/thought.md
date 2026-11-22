# 005. 无重复字符的最长子串（#3）

- LeetCode: https://leetcode.cn/problems/longest-substring-without-repeating-characters/
- 分类: 滑动窗口
- 开始时间: 2026-11-22 00:30
- 用时: 约 15 分钟

## 我的第一想法（未使用 AI）

1. (这一题之前已经练习过了)使用双指针，字典last记录每个字符出现一次之后的下标，r不断右扩，重复就把l往右缩，l跳到last[c]+1，last[c]小于left说明旧位置已经再窗口外，不用重复
2. 

## 复杂度

- 时间：O(n)——右指针只前进 n 次，left 只增不减
- 空间：O(min(n, 字符集大小))——`last` 字典最多存字符集大小个键

## 边界情况

- "" → 0
- "a" → 1
- "aa" → 1
- "abba" → 2
- "abcabcbb" → 3
- "pwwkew" → 3
- "dvdf" → 3
- "bbbbb" → 1

## 卡住的地方 / 想向 AI 验证的点

- （暂无）
