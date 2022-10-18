# Numerical methods for prime numbers.

from random import randint

# Fermat primality test
def fermat_test(n):
  for _ in range(100):
    a = randint(2,n-2)
    if pow(a,n-1,n) != 1:
      return False
  return True

def milTst(d, n):
    # Pick a random number in [2..n-2]
    a = 2 + randint(1, n - 4);
    # Compute a^d % n
    x = pow(a, d, n);
    if (x == 1 or x == n - 1):
        return True;
    # Keep squaring x while one of the following doesn't happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
    return False;

# It returns false if n is composite and returns true if n is probably prime. k is an input parameter that determines accuracy level. Higher value of k indicates more accuracy.
def miller_test(n, k):
    # Corner cases
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;

    # Find r such that n = 2^d * r + 1 for some r >= 1
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
    # Iterate given number of 'k' times
    for i in range(k):
        if (milTst(d, n) == False):
            return False;
    return True;

#k = 4;
#n = 20
#if (isPrime(n,k)):
#    print(n)
#else:
#    print("no")
