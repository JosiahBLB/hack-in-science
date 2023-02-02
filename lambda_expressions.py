"""
Using lambda expressions to find the multiples of 3, 5 and 15 within the range of 100

"""


def filtered(items, func):
    return filter(func, items)


if __name__ == "__main__":
    # Multiples of three
    print(
        str(list(filtered((x for x in range(101)), lambda x: x % 3 == 0))).strip("[]")
    )
    # Multiples of five
    print(
        str(list(filtered((x for x in range(101)), lambda x: x % 5 == 0))).strip("[]")
    )
    # Multiples of 15
    print(
        str(list(filtered((x for x in range(101)), lambda x: x % 15 == 0))).strip("[]")
    )
