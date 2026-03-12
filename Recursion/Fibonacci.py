def Fibo(n):
    #Base Condition
    if n < 2:
        return n
    
    #Calulate nth Fibonacci number
    return Fibo(n-1)+Fibo(n-2)

print(Fibo(7))