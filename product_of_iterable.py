from functools import reduce

def mul(numbers):
    return reduce((lambda x, y: x*y), numbers)