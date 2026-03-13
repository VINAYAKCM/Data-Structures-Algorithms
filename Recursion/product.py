def ProdOfDigits(n):
    if n%10 == n:
        return n

    return n % 10 * ProdOfDigits(n//10)
    #last digit → n % 10
    #remove last digit → n // 10

print(ProdOfDigits(1342))