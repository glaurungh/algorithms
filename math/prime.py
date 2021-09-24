def is_prime(n):
    """
    Returns True if number is prime
    """
    if n%2 == 0 : return False
    i = 3
    while i <= n**0.5:
        if n%i == 0 : return False
        i += 1
    return True
