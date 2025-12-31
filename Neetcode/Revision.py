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
#<------------------------------ 29 December 2025-------------------------------->#
def containsduplicates(nums):   
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
def ValidAnagram(s,t):
    if len(s) == len(t):
        return False
    count_s = {}
    count_t = {}
    for char in s:
        count_s[char] = count_s.get(char,0) + 1
    for char in t:
        count_t[char] = count_t.get(char,0) + 1
    return count_s == count_t
def groupanagram(strs):
    anagram = {}
    for word in strs:
        s_count = [0]*26
        for char in word:
            s_count[ord(char) - ord("a")] += 1
        key = tuple(s_count)
        if key not in anagram:
            anagram[key] = []
        anagram[key].append(word)
    return list(anagram.values())
def palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    #return s == s[::-1] space complexity is O(n)
    i,j = 0,len(s)-1
    while i<j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True
def containerwithmsotwater(height):
    max_area = 0
    i,j = 0, len(height)-1
    while i<j:
        height = min(height[i], height[j])
        width = j-i
        area = height*width
        max_area = max(max_area,area)
        if height[i]>height[j]:
            j-=1
        else:
            i+=1
    return max_area
#<------------------------------ 31 December 2025-------------------------------->#
def threeSum(nums):
    Output = []
    nums = nums.sort()
    for n in range(len(nums)):
        if n > 0 and nums[n] == nums[n+1]:
            pass
        i,j = i+1,len(nums)-1
        while i < j:
            sum = nums[i]+nums[j]+nums[n]
            if sum == 0:
                Output.append([nums[i],nums[j],nums[n]])
                i+=1
                j-=1
                while i<j and nums[j] == nums[j+1]:
                    j-=1
                while i<j and  nums[i] == nums[i-1]:
                    i+=1
            elif sum > 0:
                j-=1
            else:
                i+=1
    return Output
def besttimetobutandsell(prices):
    max_profit = 0 
    min_price = float('inf')
    for price in prices:
        if price < min_price:
            price = min_price
        else:
            profit = price - min_price
            max_profit = max(max_profit,profit)
    return max_profit
def LSSwithoutrepeatingchar(s):
    seen = set()
    i = 0
    longest = 0 
    for j in range(len(s)-1):
        while s[j] in seen:
            seen.remove(s[j])
            i += 1
        seen.add(s[j])
        longest = max(longest,j-i+1)
    return longest
def stringpermutation(s1,s2):
    if len(s1) > len(s2):
        return False
    counts1 = [0]*26
    counts2 = [0]*26
    for char in counts1:
        counts1[ord(char) - ord('a')] += 1
    for char in counts2:
        counts2[ord(char) - ord('a')] += 1

    for j in range(len(s2) - len(s1)):
        if counts1 == counts2
            return True
        counts2[ord(s2[j]) - ord('a')] -= 1
        counts2[ord(s2[j + len(s1)]) - ord('a')] += 1
    return counts1 == counts2
