# 006. 438. 找到字符串中所有字母异位词

- LeetCode: https://leetcode.cn/problems/find-all-anagrams-in-a-string/
- 分类: 滑动窗口
- 开始时间: ____-__-__ __:__
- 用时: ____ 分钟

## 我的第一想法（未使用 AI）

1. 这个和第一题有些相似啊。
2. 

## 复杂度

- 时间：O( n)
- 空间：O(1)

## 边界情况

- 
- s = "", p = "a" → []
- s = "a", p = "ab" → []
- s = "a", p = "a" → [0]
- s = "ab", p = "a" → [0, 1]
- s = "ab", p = "ba" → [0]
- s = "abd", p = "b" → [1]
- s = "cbaebabacd", p = "abc" → [0, 6]
- s = "abab", p = "ab" → [0, 1, 2]
- s = "aaaa", p = "aa" → [0, 1, 2]

## 卡住的地方 / 想向 AI 验证的点

- 
