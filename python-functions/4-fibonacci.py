#!/user/bin/pyhton3
def fibonacci_sequence(n):
    val = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
         while len(val) < n:
             cal = val[-1] + val[-2]
             val.append(cal)
    return val
