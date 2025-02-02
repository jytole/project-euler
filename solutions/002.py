fib1 = 1
fib2 = 2
fib3 = 3

limit = 4000000

sum = 2

while(fib3 < limit):
    if(fib3 % 2 == 0):
        sum = sum + fib3
    fib1 = fib2
    fib2 = fib3
    fib3 = fib1 + fib2
    
print(sum)