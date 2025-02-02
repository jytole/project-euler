def smallestDivByUpTo(n):
    if(n <= 0):
        return -1
    result = 0
    loop = True
    while(loop):
        result = result + n
        loop = False
        for test in range(n):
            if(result % (test + 1) != 0):
                loop = True
                break
    return result
    
print(smallestDivByUpTo(20))