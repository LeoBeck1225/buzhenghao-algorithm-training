"""005. 无重复字符的最长子串（#3）

思路见 thought.md：滑动窗口 + last 字典记录每个字符上次出现的下标；
右指针右扩，遇到重复就把左指针跳到 last[c] + 1（仅当 last[c] >= l）。
时间 O(n)，空间 O(min(n, 字符集大小))。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        a = 0
        last = {}
        for r, c in enumerate(s):
            if c in last and last[c] >= l:
                l = last[c] + 1
            last[c] = r
            a = max(a, r - l + 1)
        return a


if __name__ == "__main__":
    cases = [
        ("", 0),
        ("a", 1),
        ("aa", 1),
        ("abba", 2),
        ("abcabcbb", 3),
        ("pwwkew", 3),
        ("dvdf", 3),
        ("bbbbb", 1),
    ]

    ok = 0
    for s, want in cases:
        got = Solution().lengthOfLongestSubstring(s)
        passed = got == want
        ok += passed
        flag = "PASS" if passed else "FAIL"
        print(f"[{flag}] {s!r:<14} -> {got} (want {want})")
    print(f"\n{ok}/{len(cases)} passed")
