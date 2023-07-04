import random


def generate_large_prime(n):
    """Generates a large prime number of n bits"""
    while True:
        num = random.getrandbits(n)
        if is_prime(num):
            print(num)
            return num

def is_prime(n, k=5):
    """Tests if a number is prime using the Miller-Rabin algorithm"""
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    # Write n-1 as 2^r*d
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Test the primality k times
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True



if __name__ == '__main__':
    n = 4096
    large_prime = generate_large_prime(n)
