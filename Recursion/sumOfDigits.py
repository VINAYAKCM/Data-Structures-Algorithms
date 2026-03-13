def sumOfDigits(n):
    if n == 0:
        return 0

    return n % 10 + sumOfDigits(n//10)
    #last digit → n % 10
    #remove last digit → n // 10

print(sumOfDigits(1342))