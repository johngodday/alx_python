#!/user/bin/python3
def is_prime(n):
    if n % 1 == 0 and n % n == 0:
        return True
    else:
        return False

print(is_prime(17))