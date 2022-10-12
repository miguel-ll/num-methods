from random import randint

# Fermat primality test
def fermat_test(n):
  for _ in range(100):
    a = randint(2,n-2)
    if pow(a,n-1,n) != 1:
      return False
  return True
