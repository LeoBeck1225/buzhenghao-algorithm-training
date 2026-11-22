"""006. 找到字符串中所有字母异位词（#438）

思路见 thought.md：固定长度窗口 + 差异计数 d（窗口计数与 p 计数不相等的字符种类数）。
时间 O(n)，空间 O(1)（两个长度 26 的计数数组）。
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []

        need = [0] * 26
        for ch in p:
            need[ord(ch) - 97] += 1

        win = [0] * 26
        for ch in s[:m]:
            win[ord(ch) - 97] += 1

        # d = 计数不相等的字符种类数
        d = sum(1 for c in range(26) if win[c] != need[c])

        res = []
        if d == 0:
            res.append(0)

        for i in range(1, n - m + 1):
            out = ord(s[i - 1]) - 97
            if win[out] == need[out]:
                d += 1                  # 移出前相等，移出后就不等了
            win[out] -= 1
            if win[out] == need[out]:
                d -= 1                  # 移出后反而相等

            inn = ord(s[i + m - 1]) - 97
            if win[inn] == need[inn]:
                d += 1
            win[inn] += 1
            if win[inn] == need[inn]:
                d -= 1

            if d == 0:
                res.append(i)

        return res


if __name__ == "__main__":
    cases = [
        ("", "a", []),
        ("a", "ab", []),
        ("a", "a", [0]),
        ("ab", "a", [0]),
        ("ab", "ba", [0]),
        ("abd", "b", [1]),
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
        ("aaaa", "aa", [0, 1, 2]),
        ("aaaaaaaaaa", "aaaa", [0, 1, 2, 3, 4, 5, 6]),
        ("baa", "aa", [1]),
    ]

    ok = 0
    for s, p, want in cases:
        got = Solution().findAnagrams(s, p)
        passed = got == want
        ok += passed
        flag = "PASS" if passed else "FAIL"
        print(f"[{flag}] s={s!r:<14} p={p!r:<7} -> {got} (want {want})")
    print(f"\n{ok}/{len(cases)} passed")
