def isPowerOfFour( n: int) -> bool:
    print(n)
    if (n <= 0):
        return False
    if (n == 1):
        return True
    if (n % 4 == 0):
        return isPowerOfFour(n // 4)

print(isPowerOfFour(18))