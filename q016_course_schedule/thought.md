# 016. 207. 课程表

- LeetCode: https://leetcode.cn/problems/course-schedule/
- 分类: 图/拓扑排序
- 开始时间: ____-__-__ __:__
- 用时: ____ 分钟

## 我的第一想法（未使用 AI）

1. 为每一种课构建一个链表，如果该课程已在之前的链表里面存在就接着前面的来，最后发现有第一个课程在以自己为开头的链表里再度出现，则判定失败
2. 

## 复杂度

- 时间：O( v+e)
- 空间：O( v+e)

## 边界情况

- 
- numCourses = 1, prerequisites = [] → true
- numCourses = 2, prerequisites = [] → true
- numCourses = 2, prerequisites = [[1, 0]] → true
- numCourses = 2, prerequisites = [[1, 0], [0, 1]] → false
- numCourses = 3, prerequisites = [[0, 1], [1, 2]] → true
- numCourses = 3, prerequisites = [[0, 1], [1, 2], [2, 0]] → false
- numCourses = 2000, 长链 [[1,0],[2,1],...,[1999,1998]] → true

## 卡住的地方 / 想向 AI 验证的点

- 怎样能省一点复杂度？
