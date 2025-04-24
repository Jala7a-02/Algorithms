# Recurssion
print(0)
print(1)
count = 2 
def fib(a,b) :
    global count
    if count <= 13 :
        new = a + b
        print(new)
        a = b 
        b = new
        count += 1
        fib(a,b)
    else :
        return
# Find the Nth number
def F(n) :
    if n <= 1 :
        return n
    return F(n-1) + F(n-2)
print(F(19))