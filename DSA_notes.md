# DSA

## Time and Space Complexity

### Time complexity

- Time taken for the code to run? → ❌
    - WHY??…. because different devices have different capabilities and a code can take different amount of time to run on different devices.
- Rate of Increase in time with respect to the input size.
- Rules to calculate Time complexities
    - Always calculate TC in terms of Worst case.
    - Avoid the constant values
    - Avoid lower bounds.
    
    ```python
    for i in range (1,n):  ----> 1 (ops1 --> checks if i is in the range)
    	print("Nauman")    ----> 1 (ops2 --> prints)
    	i+=1               ----> 1 (ops3 --> adds i)
    ```
    
    - as the loop goes (n-1) times total ops → 3(n-1)
    - **Big O notation**
        - describes the **worst-case time or space complexity** of an algorithm as the input size grows.
        - It shows how quickly the runtime or memory usage increases relative to the input size **n**, helping compare the efficiency of different algorithms.
        - For example, **O(n²)** that on Doubling the input you quadruple the amount of Time taken.
    - For the Above example → O(3(n-1)) → O(3n-3) → O(3n) → O(n) → Hence can say that the time grows in linearly with the input size.
- Examples

![image.png](image.png)

### Time Limit Exceeded Error

- Time limit → 10^8 operations can be done in 1 sec
    
    ![image.png](image%201.png)
    
- e.g. Lets suppose we Sort a list with O(N^2).
    - The upper limit of the constraints is 10^5.
    - hence WORST CASE → ((10^5)^2) = 10^10
    - only 10^8 operations can be done in 1 sec Hence, to work onto 10^10 operation it will take 100sec.
    - Which is too much we need to reduce the Time complexity from N^2 to N, NLog(N) or Log(N).

### Complexities of Basic operations

- For Lists
    
    ![image.png](image%202.png)
    
- For Sets →
    
    ![image.png](e7dee655-0799-49b3-9998-a4194d746b1b.png)
    
- For Dictionaries →
    
    ![image.png](image%203.png)
    

### Space Complexity

- The memory space that the code takes.
    - Space → Auxiliary space + Input space
        - Auxiliary space → The extra space used to solve the problem.
        - Input space → The space used to store the input.
            
            ```python
            x=5
            y=10
            z=15
            total = x+y+z
            print(total)
            ```
            
        - Here → x,y,z are the input variables.
            - Total is a Auxiliary variable
            - WHY??
                - because we are making the variable to help us solve the question.

## QSCs

(Question Solving Concept)s

### Extraction of digits

- e.g. We need to extracts all the digits of the n = 5673.
- Hint → get the reminder → print it → replace n with whole digits.
    
    ```python
    n = 5673
    while n > 0:
    	last_digit = n % 10
    	print(last_digit)
    	n = n // 10
    ```
    

### Counting of digits

- e.g. We need to count the digits of n = 5673

Method - 1 

- Hint → Use the same logic as Extraction of digits
    
    ```python
    n = 5673
    count = 0
    while num > 0:
    	count += 1
    	n = n // 10
    ```
    
    - Time complexity → Because we are dividing by 10 Hence,
        
        ![image.png](image%204.png)
        
        - If it were to be divided by 2,5 of any other number that number will be in the base of time complexities
        - Obviously because if the number increases the number of time operation happen will reduce hence the time complexity will decrease

Method  - 2

- Hint → Using LOG function
    
    ```python
    from math import *
    def countdigit(num):
    	return int(log10(num)+1)
    ```
    

### Store Frequencies in a Dictionary

- Count the occurrences of the number in a List using a Dictionary

Method - 1 

- Basic method
    
    ```python
    nums = [5,6,5,8,7,6,8,9,7,4]
    freq_map = {}
    for i in range(0,len(nums):
    	if nums[i] in freq_map:
    			freq_map[nums[i]] += 1
    	else:
    			freq_map[nums[i]] = 1
    print(freq_map)
    print(freq_map[6]) -> #gives the number of 6 in the nums and dict
    ```
    

Method -2 

- .get method
    
    ```python
    nums = [5,6,5,8,7,6,8,9,7,4]
    hash_map = {}
    for i in range(0,len(nums):
    	hash_map[nums[i]] = hash_map.get(nums[i],0) + 1
    ```
    
    Explanation → *hash_map.get[nums[i],0]  →* counts the current frequency of the ith element from the list in the hash_map.
    
    - Time complexity → O(n) → depends on the number of items in the list linearly.
    - Space Complexity → O(n) → because we are taking a dict that can have the length of n.

## Hasing

- Restoring Values into some Data Structure like List, Dictionary, Sets and then fetching it.

### Problem

---

1. Count the number of times a number in the list M appears in the list N.
    - N = [5,4,5,6,5,5,1,2,3,9,7,]
    - M = [54,8,4,2,6,3,2,1,4,55,6]
- ***Brute Force method*** → iterate through all the elements of the M to find the number of time the First element of N appears and do it for all the elements of N.
    - Problem → TC → 10^2
        - Constraint on N and M → 10^8
        - So the total operation become (10^8)^2 = 10^16
        - So TLEE will occur.
- ***Hashing method (LISTS)*** → we make a list of length 11 hence it has indexes from 0 to 10 and all the positions have 0 initially. Then every time you find the element in the N list we would just want to add a 1 in the same index on the hash_list we created.
    - THIS METHOD ONLY WORKS BECAUSE WE HAVE A CONSTRAINTS → NUMBERS IN N ARE BETWEEN 1 AND 10.
    
    ```python
    N = [5,4,5,6,5,5,8,2,3,9,7]
    M = [8,4,2,6,3,2,1,4,55,6]
    
    hash_list = [0]*11
    for i in N:
    	hash_list[i] += 1
    for j in M:
    	if j<1 and j>10:
    		print("0")
    	else:
    		Value = hash_list[j]
    		print(Value)
    
    Mistake: hash_list[N[i]] Wrong
    				If you are using range then only you need to do this. If you are using the (In List) operation then you did not use it then we use hash_list[i] just the index.
    ```
    
    - Time Complexity → O(N)
    - Space Complexity → O(11) → O(1)
- ***Hashing Method (DICT)*** →  As we find the new number in the in the N lists we add that number to the dictionary as a key and with a value of 1 as you find the same number again you just increase the value by 1.
    - THIS ALSO WORKS MORE FOR NUMBERS OF ELEMENTS IN LISTS.
    
    ```python
    N = [5,4,5,6,5,5,8,2,3,9,7]
    M = [8,4,2,6,3,2,1,4,55,6]
    
    hash_map = {}
    for i in range(0,len(N)):
    	hash_map[N[i]] = hash_map.get(N[i],0) + 1
    for j in range(len(M):
    	Value = hash_map.get(M[j])
    	If value is None:
    			print("0")
    	else:
    			print(Value)
    ```
    

---

1. Character Hashing → ASCII value
    - S = “azyxyyzaaaa”
    - q = [”d” , “a”, “y”, “x”]
    
    ```python
    Method of Using - 97
    
    S = “azyxyyzaaaa”
    q = [”d”, “a”, “y”, “x”]
    
    hash_list = [0]*26
    for char in range(0,len(S)):
    		ASCII_value = ord(char)
    		Value = ASCII_value - 97
    		hash_list[Value] += 1
    for ch in q:
    		ASCII_val = ord(ch)
    		Val = ASCII_val - 97
    		print(hash_list[Val])
    ```
    
    ```python
    Method of using only by ord func.
    
    S = “azyxyyzaaaa”
    q = [”d”, “a”, “y”, “x”]
    
    hash_list = [0]*26
    for char in S:
    		value = ord(char) - ord("a")
    		hash_list[value] += 1
    for ch in q:
    		val = ord(ch) - ord("a")
    		print(hash_list[val])
    ```
    

## Recursion

- Infinite Recursion: If there is not bound it will go until infinity and give a STACKOVER FLOW error.
    - Python is smart what it does is goes only 987 and them assumes it is going to be infinite.( you can always change this)
- Head Recursion: When the action is one before and the fucntion is called again later on.
    
    ```python
    def func():
    	if count == 4:
    			return
    	print("Nauman")
    	count+=1
    	func()
    ```
    
- Tail Recursion: When the function is called before the action.
    
    ```python
    def func():
    	if count == 4:
    			return
    	count+=1
    	func()
    	print("Nauman")
    	
    ```
    
- Recursion Tree:
    
    ![image.png](image%205.png)
    
    - Time Complexity → O(N+1) → O(N)
        - If there are N inputs or N outcomes The number of the time the function is called is always N+1.
    - Space Complexity → O(N)

### Recursion Using Parameters

- e.g. Print “15” 4 times using Recursion.
    
    ```python
    def func(x, n):
        if n == 0:   # base case
            return
        print(x)      # do work
        func(x, n-1)  # recursive call
    ```
    

![image.png](image%206.png)

- e.g. Print 1 to N using Recursion

```python
def func(i,N)
		while i>N:
			return
		print(i)
		func(i+1,N)
```

![image.png](image%207.png)

- e.g. Print sun of First Natural numbers.
    
    ```python
    def sunc(sum,i,N):
    	while i>N:
    			print(sum)
    			return
    	sunc(sum+i,i+1,N)
    ```
    

![image.png](image%208.png)

### Functional Recursion

- Create a flow
- Create the base Condition.
- e.g. Print sun of First Natural numbers.

```python
def func(N):
		if N==1:
			return 1
		return N + func(N-1)
```

![image.png](image%209.png)

- Factorial of a Number
    
    ```python
    def factorial(num):
    		if n==0 or n==1 
    			return 1
    		return num*(factorail(num-1)
    ```
    

![image.png](image%2010.png)

- Reverse a list with the help of Recursion
    
    ```python
    def func(nums,left,right):
    		if left > right:
    				return
    		arr[left], arr[right] == arr[right], arr[left]
    		return func(nums,left+1,right-1)
    ```
    
- PALINDROME using Recursions
    
    ```python
    def palindrome(s,left,right):
    		if left > right:
    				return True
    		if s[left] != s[right]
    				return False
    		return palindrome(s,left+1,right-1)
    				
    ```
    
- Fibonacci Series
    
    ```python
    def FBS(num):
    		if num == 0 or num == 1:
    				return num
    		return FBS(num-2) + FBS(num-1)
    ```
    

## Sorting Algorithms

### Selection Sort

```python
nums = [2,1,4,5,3,5]

def selectionsort(nums):
		for i in range(len(nums)):
				min_idx = i
				for j in range(i+1, len(nums)):
						if nums[j] < nums[min_idx]:
								min_idx = j
				 nums[i],nums[min_idx] = nums[min_idx].nums[i]
						
Time compleity -> The list will go n,n-1,n-2,...,0 times.
									hence TC = O(N^2)
Space complexity -> o(1)						
```

## Bubble sort

```python
nums = [2,1,4,5,3,5]

def bubblesort(nums):
		for i in range(len(nums)):
			is_swap = False              # to reduce the TC for best case when the list is sorted
				for j in range(0,len(nums)-i-1)
						if nums[j] > nums[j+1]:
								 nums[j],nums[j+1] =nums[j+1], nums[j]
								 is_swap = True
				if is_swap == False:
						return
								
								 
Time complexity -> Worst Case -> same as selection Sort -> O(N^2)
			 
```

## Insertion Sort

```python
nums = [2,1,4,5,3,5]

def Insertionsort(nums):
		for i in range(len(nums)):
				 nums[i] = key
				 j = i - 1
				 while j >= 0 and nums[j] > key:
							nums[j+1] = nums[j]
							j-=1
				arr[j+1] = key
				
Time complexity -> Worst Case -> Same as bubble and selection sort -> O(N^2)

```

## Stack

- A **Stack** is a data structure used to store and manage data in a specific order.

### LIFO: Last In, First Out

- The element that is inserted **last** is removed **first**.
- Example: A stack of plates. The plate placed on the top last will be the first to be removed.

### Operations on Stack

| Operation | Description | Python Equivalent |
| --- | --- | --- |
| push(x) | Insert element into stack | `append(x)` |
| pop() | Remove the top element | `pop()` |
| peek() or top() | View the top element without removing it | `stack[-1]` |
| isEmpty() | Check if the stack is empty | `len(stack) == 0` |

### Stack in Python Using List

```python
stack = []  # creating an empty stack

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

# Pop element
removed = stack.pop()

# Peek at top element
top = stack[-1]

# Check if empty
empty = (len(stack) == 0)

print("Removed element:", removed)
print("Current top element:", top)
print("Is stack empty?", empty)ddd
```

### Stack Using Class

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0
```

### Why Stack Is Useful

- Stacks are used in many applications such as:
    - Reversing data
    - Checking balanced parentheses
    - Function call execution (call stack)
    - Undo / Redo operations in editors
    - Expression evaluationd
    
- Check Balanced Parentheses

```python
# Given a string containing brackets, determine if the brackets are properly balanced.

def isBalanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in pairs.values():
            stack.append(char) # Push opening brackets into stack.
        elif char in pairs.keys():
            if not stack or stack.pop() != pairs[char]: #When a closing bracket is found, check if it matches the top of stack.
                return False
    return len(stack) == 0

print(isBalanced("{[()]}"))  # True
print(isBalanced("([)]"))    # False
```

---

- Reverse a String Using Stack

```python
def reverseString(s):
    stack = []
    for char in s:
        stack.append(char) #Push every character into the stack.

    reversed_s = ""
    while stack:
        reversed_s += stack.pop() #Pop characters one-by-one to build the reversed string.
    return reversed_s

print(reverseString("hello"))  # olleh

```

---

- Minimum Element in a Stack (Efficient Approach)
    - Use an additional stack to track minimum values.

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self):
        value = self.stack.pop()
        if value == self.minStack[-1]:
            self.minStack.pop()

    def getMin(self):
        return self.minStack[-1]
```