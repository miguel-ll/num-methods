from decimal import *
import random

# Check whether a number can be represented by sum of two squares using Fermat Theorem.
def sum2sq(n):
    i = 2;
    while (i * i <= n):
        count = 0;
        if (n % i == 0):
            # Count all the prime factors.
            while (n % i == 0):
                count += 1;
                n = int(n / i);
            # If any prime factor of the form (4k+3)(4k+3) occurs an odd number of times.
            if (i % 4 == 3 and count % 2 != 0):
                return False;
        i += 1;
    # If n itself is a x prime number and can be expressed in the form of 4k + 3 we return false.
    return n % 4 != 3;

# Legendre's three-square theorem. That gives a condition for a number n to be expressible as the sum of three squares: if n != 4^a(8b+7).
def sum3sq(n):
    while n > 0 and n % 4 == 0:
        n = n//4
    return n % 8 != 7

def pdi_function(number, base: int = 10, p: int = 2):
    """Perfect digital invariant function."""
    total = 0
    while number > 0:
        total += pow(number % base, p)
        number = number // base
    return total

# A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit. For instance, 13 is a happy number because 1^2 + 3^2 = 10 and 1^2 + 0^2 = 1.
# A happy base is a number base b where every number is b-happy. The only happy bases less than 5*10^8 are base 2 and base 4.
# Unsolved problem: Are base 2 and base 4 the only bases that are happy?

def is_happy(number: int) -> bool:
    """Determine if the specified number is a happy number."""
    seen_numbers = set()
    while number > 1 and number not in seen_numbers:
        seen_numbers.add(number)
        number = pdi_function(number)
    return number == 1

# William Shanks bot. After which digit will the reciprocal of a prime number repeat?
def shanks(num):
    if num == 7:
    	print("6")
    	return
    getcontext().prec = num+9
    new_num = str(Decimal(1)/Decimal(num))
    new_num = new_num[new_num.find('.'):]
    new_num = new_num[1:]
    firstfour = new_num[:9]
    rest = new_num[9:]
    print(rest.find(firstfour)+9)
    
def approx_pi(INTERVAL):
    circle_points = 0
    square_points = 0

    for _ in range(INTERVAL):
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)

        # Distance between (x, y) from the origin
        origin_dist = rand_x**2 + rand_y**2

        # Checking if (x, y) lies inside the circle
        if origin_dist <= 1:
            circle_points += 1
        square_points += 1

        # pi= 4*(no. of points generated inside the circle)/ (no. of points generated inside the square)
        pi = 4 * circle_points / square_points
    return pi
