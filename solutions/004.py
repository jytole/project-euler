import math

def isPalindrome(input):
    inputString = str(input)
    # Base case: 1-digit number
    if(len(inputString) <= 1):
        return True
    middle = math.ceil(len(inputString) / 2)
    for i in range(middle):
        # Compare ith digit with ith digit from end
        if inputString[i] != inputString[-i-1]:
            return False
    return True

maxPalindrome = -1    
for j in range(900):
    for k in range(900):
        tmp = (j + 100) * (k + 100)
        if(isPalindrome(tmp)):
            if(tmp > maxPalindrome):
                maxPalindrome = tmp
print(maxPalindrome)