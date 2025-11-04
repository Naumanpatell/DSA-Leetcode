# MinStack

2nd Review: November 8, 2025
Date Solved: November 3, 2025
Difficulty: Medium
Review: 0
Status: Solved
Topic/Pattern: Stack

## Link→ [https://neetcode.io/problems/minimum-stack?list=neetcode150](https://neetcode.io/problems/minimum-stack?list=neetcode150)

### **Problem**

Design a stack that, in addition to the normal stack operations (`push`, `pop`, `top`), can also return the **minimum element** in **O(1)** time.

You must support:

| Function | Meaning |
| --- | --- |
| `push(val)` | Insert value into stack |
| `pop()` | Remove top element |
| `top()` | Return top element |
| `getMin()` | Return **current minimum** |

---

## **Example**

```
Input:
push(1)
push(2)
push(0)
getMin() → 0
pop()
top() → 2
getMin() → 1

```

---

## **Brute Force Approach (BAD)**

- Use a normal stack.
- Every time someone calls `getMin()`, **scan the entire stack** to find the smallest value.

```python
# getMin -> O(n)
min_val = min(stack)

```

### **Complexity**

| Operation | Time |
| --- | --- |
| push | O(1) |
| pop | O(1) |
| top | O(1) |
| getMin | ❌ O(n) |

**Not acceptable.**

---

## **Optimal Approach — Maintain a Second Stack**

We use **two stacks**:

| Stack | Stores |
| --- | --- |
| `stack` | All values normally |
| `min_stack` | The minimum **at each point in time** |

**Key Idea**

Whenever we push a value:

- Push it into main stack
- Push `min(value, current_min)` into `min_stack`

So top of `min_stack` is always the **current minimum**.

---

### **Code (Interview-Safe, No Imports)**

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        # Push the new min between val and previous min
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

```

---

## **Why This Works**

Example `push` sequence:

```
push(3)     stack: [3]        min_stack: [3]
push(5)     stack: [3,5]      min_stack: [3,3]
push(1)     stack: [3,5,1]    min_stack: [3,3,1]
push(2)     stack: [3,5,1,2]  min_stack: [3,3,1,1]

```

`getMin()` → **last element of min_stack** → `1`

If we pop the 2:

```
stack:     [3,5,1]
min_stack: [3,3,1]

```

Min remains correct.

---

## **Complexity**

| Operation | Time | Space |
| --- | --- | --- |
| push | O(1) | O(n) |
| pop | O(1) | O(n) |
| top | O(1) | O(n) |
| getMin | **O(1)** | O(n) |

---

## **Tip**

- Always keep `min_stack` in **sync** with `stack`.
- Never compare values by looking back into stack — always rely on `min_stack`.