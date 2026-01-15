# LSS Without Repeating Characters

2nd Review: November 4, 2025
Date Solved: October 30, 2025
Difficulty: Medium
Review: 0
Status: Solved
Topic/Pattern: Sliding Window

### Link → https://neetcode.io/problems/longest-substring-without-repeating-characters

## Problem

- Given a string `s`, find the **length of the longest substring** without repeating characters.
- A substring must be **continuous**.

---

### Example

| Input | Output | Reason |
| --- | --- | --- |
| `"abcabcbb"` | `3` | `"abc"` is longest before repeating `a` |
| `"bbbbb"` | `1` | only `"b"` |
| `"pwwkew"` | `3` | `"wke"` is longest continuous unique substring |
| `""` | `0` | empty string |

---

## Approaches

### 1. Brute Force — Check All Substrings

```python
def lengthOfLongestSubstring(s):
    longest = 0

    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            longest = max(longest, j - i + 1)

    return longest
```

- **Time:** O(n²) — tries all substrings
- **Space:** O(n) — set to track characters
- **Notes:** Works but slow when `n` is large

---

### 2. Optimal — Sliding Window + Set (Recommended)

```python
def lengthOfLongestSubstring(s):
    charSet = set()
    left = 0
    longest = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1

        charSet.add(s[right])
        longest = max(longest, right - left + 1)

    return longest
```

- **Time:** O(n) — each char added/removed at most once
    - There are 2 loops but that does not make the complexity to n^2 because the points does not comeback to the previous so the elemets are iterated only once.
- **Space:** O(n) — storing current substring characters
- **Notes:** Efficient & clean; classic sliding window pattern

---

## Summary

| Approach | Time | Space | Notes |
| --- | --- | --- | --- |
| Brute Force | O(n²) | O(n) | Too slow for large inputs |
| Sliding Window | **O(n)** | O(n) | Best solution, used in interviews |

---

## Edge Cases

| Input | Output | Reason |
| --- | --- | --- |
| `""` | `0` | No characters |
| `"a"` | `1` | Single character |
| `"aaaaa"` | `1` | All repeats |
| `"abcd"` | `4` | All unique |

---

## Tip

- Whenever you must **find or maximize a substring with a restriction**, think **Sliding Window**.
- Use two pointers and a **set** to maintain unique characters.