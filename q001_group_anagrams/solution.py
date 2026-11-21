"""001. 字母异位词分组（#49）

思路见 thought.md：把"字母构成"编码成可哈希的 key，一次遍历分组。
实现时把 key 从"排序后的字符串"换成了"26 长度计数元组"：
  - 排序 key：O(k log k) / 词
  - 计数 key：O(k) / 词，整体从 O(n·k log k) 降到 O(n·k)
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            cnt = [0] * 26
            for ch in word:
                cnt[ord(ch) - ord("a")] += 1
            groups[tuple(cnt)].append(word)

        return list(groups.values())


def _normalize(groups):
    """把结果整理成可比较的形式：组内排序、组间按首元素排序。"""
    return sorted((sorted(g) for g in groups), key=lambda g: g[0] if g else "")


if __name__ == "__main__":
    cases = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["aab", "abb"], [["aab"], ["abb"]]),
        (["abc", "bca", "cab"], [["abc", "bca", "cab"]]),
        (["a", "a", "a"], [["a", "a", "a"]]),
    ]

    ok = 0
    for strs, want in cases:
        got = Solution().groupAnagrams(strs)
        passed = _normalize(got) == _normalize(want)
        ok += passed
        flag = "PASS" if passed else "FAIL"
        print(f"[{flag}] {strs} -> {got}")
    print(f"\n{ok}/{len(cases)} passed")
