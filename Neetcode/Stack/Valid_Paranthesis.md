# Valid Paranthesis

2nd Review: November 8, 2025
Date Solved: November 3, 2025
Difficulty: Easy
Review: 0
Status: Solved
Topic/Pattern: Stack

### Link → https://neetcode.io/problems/valid-parentheses

## Problem

- You are given a string `s` containing only the characters:
    
    `(`, `)`, `{`, `}`, `[`, `]`
    
- Determine if the string is **valid**.
- A string is considered valid if:
    1. Every opening bracket has a matching closing bracket **of the same type**
    2. Brackets are **closed in the correct order**

---

### Example

| Input | Output | Reason |
| --- | --- | --- |
| `"()"` | `True` | simple match |
| `"()[]{}"` | `True` | all matching and ordered |
| `"(]"` | `False` | `(` does not match `]` |
| `"([)]"` | `False` | order is wrong |
| `"{[]}"` | `True` | properly nested |

---

## Approaches

### 1. Brute Force — Replace Pairs Repeatedly

```python
def isValid(s):
    prev = None
    while prev != s:
        prev = s
        s = s.replace("()", "").replace("{}", "").replace("[]", "")
    return s == ""
d

```

- **Time:** O(n²) — because replace happens repeatedly
    - .replace = O(n)
    - While loo[ = O(n)
- **Space:** O(n) — as strings are copied
- **Notes:** Works but too slow & not clean for interviews

---

### 2. Optimal — Stack (Recommended)

```python
def isValid(s):
    stack = []
    bracs = {')':'(', ']':'[', '}':'{'}

    for ch in s:
        if ch in bracs.values():
            stack.append(ch)
        else:
            if not stack or stack[-1] != bracss[ch]:
                return False
            stack.pop()

    return len(stack) == 0

```

- **Time:** **O(n)** — each character processed once
- **Space:** O(n) — stack may hold opening brackets
- **Notes:** Clean, efficient, standard stack problem

---

## Summary

| Approach | Time | Space | Notes |
| --- | --- | --- | --- |
| Replace repeatedly | O(n²) | O(n) | Slow and hacky |
| **Stack** | **O(n)** | O(n) | Best & most used |

---

## Edge Cases

| Input | Output | Reason |
| --- | --- | --- |
| `""` | `True` | empty string is valid |
| `")("` | `False` | closing appears first |
| `"((("` | `False` | unclosed brackets |
| `"{}[]"` | `True` | independent correct pairs |

---

## Tip

- Whenever brackets must be matched in **order**, think **Stack**.
- Push opening brackets → pop when matching closing bracket appears.
- Final answer is valid **only if stack ends empty**.