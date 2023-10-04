#!/usr/bin/python3

def prime (n):
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime

""" Prime Game """
def isWinner(x, nums):
    if x is None or nums is None or x == 0 or nums ==0:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = isPrime(nums[i])
        if len(prime) %2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    return None
