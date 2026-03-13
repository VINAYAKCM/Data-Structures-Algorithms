def nTo1(n):
    if n == 0:
        return
    
    print(n)
    nTo1(n-1)

print(nTo1(5))