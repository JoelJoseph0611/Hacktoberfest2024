def is_prime(n):
    # Check if number is less than 2 (0 and 1 are not prime)
    if n < 2:
        return False
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
number = 29
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
