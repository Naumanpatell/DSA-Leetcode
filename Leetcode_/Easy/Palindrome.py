###Link : https://leetcode.com/problems/palindrome-number/description/

### Using Mathematics

### Store the last digit of the number → then multiply the number by 10 → then add the new last digit to it.

def isPalindrome(num):
	result = 0 
	while num > 0:
		last_digit = num % 10
		result = (result*10) + last_digit
		num = num //10
	return result
if isPalindrome:
	print("your number is a palindrome")
else:
	print("Not a palindrome")

# - Time complexity → 0(log10(num))
#     - The number of times the while loop will run is depend on how the num is being reduced.
#     - Hence in the ques it happens by a factor of 10.
# - Space complexity → O(1)