import time

def primeFactors(input):
    factors = [input]
    allPrime = False
    nth = 1
    currentFactor = nthprime(nth)
    
    # Quick loop to attempt to make the problem more manageable
    
    # Limit this run to 10 iterations, so this isn't an infinite loop
    
    testn = 0
    while(factors[0] > 100000 and testn < 10):
        tmp = primesLEQ(100000)
        for i in range(len(factors)):
            factor = factors[i]
            for val in tmp:
                if factor % val == 0 and factor / val > 1:
                    factors[i] = factor / val
                    factors.append(val)
        testn = testn + 1
    
    while(not allPrime):
        # check if each factor is divisible by prime (and greater than 1)
        for i in range(len(factors)):
            factor = factors[i]
            if(factor % currentFactor == 0 and factor / currentFactor > 1):
                factors[i] = factor / currentFactor
                factors.append(currentFactor)
        # Test if all of the factors are prime at the end of each loop
        
        print(factors)
        
        allPrime = True
        for testNum in factors:
            if(not isPrime(testNum)):
                allPrime = False
                
        nth = nth + 1
        currentFactor = nthprime(nth)
                
    return factors

def largestPrimeFactor(input):
    factors = primeFactors(input)
    max = 1
    for factor in factors:
        if factor > max:
            max = factor
    return max
    
def nthprime(n):
    # Handle base cases
    if(n == 1):
        return 2
    if(n < 1):
        return 0
    
    primes = [2]
    
    # Start counting primes
    i = 2
    while(n > 1):
        i = i + 1
        isPrime = True
        for prime in primes:
            if(i % prime == 0):
                isPrime = False
        if(isPrime):
            primes.append(i)
            n = n - 1
    return i

def primesLEQ(n):
    # Handle base cases
    if(n <= 1):
        return 0
    
    primes = [2]
    
    # Start counting primes
    i = 2
    while(i <= n):
        i = i + 1
        threshold = i / 2
        isPrime = True
        for prime in primes:
            if(prime < threshold):
                if(i % prime == 0):
                    isPrime = False
                    break
        if(isPrime):
            print("added", i)
            primes.append(i)
            
    return primes

def isPrime(n):
    if(n % 2 == 0):
        return False
    testList = primesLEQ(n / 2)
    for prime in testList:
        if(n % prime == 0):
            return False
        
    return True