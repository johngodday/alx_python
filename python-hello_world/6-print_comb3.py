for x in range(10):
    for y in range(x + 1, 10):
        print("{:02d}".format(x * 10 + y), end=", " if x < 9 or y < 9 else "\n")