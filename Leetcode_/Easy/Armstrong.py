# Link : https://leetcode.com/problems/armstrong-number/description/

# ### SOLUTION

# - Description : The addition of all the digit of the number were each one is multiplied by itself same number of times as the number of digit in the number.

# Examples :   
#  153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# 370 = 3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370
# 371 = 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371
# 1634 = 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
    
# Method :

def Armstrong_number(num):
    len_num = len(str(num))
    print (len_num)
    result = 0
    while num > 0:
        last_digit = num % 10
        result = result + (last_digit**len_num)
        num = num // 10
    print(result)


# - Time complexity → 0(log10(num))
#     - The number of times the while loop will run is depend on how the num is being reduced.
#     - Hence in the ques it happens by a factor of 10.
# - Space complexity → O(1)

# Mistake : *result = result + (last_digit**len_num)*