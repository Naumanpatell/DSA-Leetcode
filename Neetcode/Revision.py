from collections import defaultdict  
#<------------------------------30 october 2025-------------------------------->#
#--1. Contain_duplicates--
#Sorting method
def sort_duplicates(nums):
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            return True
        else:
            return False
#set method
def contain_duplicates(nums):
    seen = set()
    for num in range(len(nums)):
        if num in seen:
            return True
        set.add(num)
    return False
#--2. Valid_Aangram--
#sorting method
def sort_anagrams(s,t):
    sorted(s)==sorted(t)
#Hashing method
def Valid_anagram(s,t):
    if len(s) != len(t):
        return False
    counts = {}
    countt= {}
    for char in s:
        counts[char] = counts.get(char,0) + 1
    for char in t:
        countt[char] = countt.get(char,0) + 1
    return counts == countt
#--3. TwoSum--
#Brute Force
def TwoSum_Brute(nums,target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
#Hashmap
def TwoSum(nums,target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff],i]
        seen[num] = i
#--4. GroupAnagram--
#sortingmethod
def sorting_Group_anagram(strs):
    anagram = defaultdict(list)
    for word in strs:
        sorted_word = sorted(word)
        key = ''.join(sorted_word)
        anagram[key].append(word)
    return list(anagram.values())      
#hashmaps
def Group_anagarm(strs):
    anagram = {}
    for word in strs:
        count = [0]*26
        for char in word:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)
        if key not in anagram:
            anagram[key] = []
        anagram[key].append(word)
    return list(anagram.values())
#--5. Palindrome(sentence)--
#directmethod
def palindrome(s):
    s = ''.join(char for char in s if char.isalnum())
    # s == s[::-1]
    i, j = 0,len(s)-1
    while i <= j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
        return True
#--6. Container with Most Water--
#bruteforce
def most_water_brute(heights):
    max_area = 0
    for i in range(len(heights)):
        for j in range(i+1, len(heights)):
            width = j-i
            length = min(heights[i], heights[j])
            area = width*length
            max_area = max(max_area, area)
    return max_area
#TwoPointer
def most_water(heights):
    max_area = 0
    i, j = 0, len(heights)
    while i < j:
        length = min(heights[i], heights[j])
        width = j-i
        area = length * width
        max_area = max(max_area, area)
        if heights[i] > heights[j]:
            j -= 1
        else:
            i += 1
    return max_area
#