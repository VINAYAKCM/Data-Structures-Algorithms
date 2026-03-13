def nTo1(n):
    if n == 0:
        return
    
    nTo1(n-1)
    print(n)
    
print(nTo1(5))
