limit = 1000
threecheck = 3
fivecheck = 5
sum = 0

while(threecheck < 1000):
    sum = sum + threecheck
    threecheck = threecheck + 3

while(fivecheck < 1000):
    sum = sum + fivecheck
    fivecheck = fivecheck + 5
    if(fivecheck % 3 == 0):
        fivecheck = fivecheck + 5
        
print(sum)