# 001. 字母异位词分组（#49）

- LeetCode: https://leetcode.cn/problems/group-anagrams/
- 分类: 哈希
- 开始时间: 2026-11-21 21:20
- 用时: 约 20 分钟

## 我的第一想法（未使用 AI）

1. 采用字典，key采用ASCLL码，value按输入的字符储存，输入完成好统一比较key，输出相同的value
2. ASCLL码为按字母顺序。"eat" → 排序 → "aet"，"tea" → 排序 → "aet"，"ate" → 排序 → "aet"

## 复杂度

- 时间：O(k log k)，k为长度
- 空间：O(1)

## 边界情况

- ["abc", "bca", "cab"] → 应该输出一组，[""] 和 [""] → 空串之间不算异位词

## 卡住的地方

- key 和 value 谁放"特征值"没想清楚，一开始写成了 key 用原词
