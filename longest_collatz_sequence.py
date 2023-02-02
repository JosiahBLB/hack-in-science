def collatz_length(n, steps=0):
    while n != 1:
        n = n // 2 if n % 2 == 0 else n * 3 + 1
        steps += 1
    return int(steps)
