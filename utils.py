def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

<<<<<<< HEAD
<<<<<<< Updated upstream
=======
=======
>>>>>>> dev5
def is_power_of_five(n):
    while n % 5 == 0 and n != 0:
        n //= 5
    return n == 1

<<<<<<< HEAD
def is_power_of_two(n):
    return (n & (n - 1)) == 0 and n != 0

>>>>>>> Stashed changes
=======
>>>>>>> dev5
