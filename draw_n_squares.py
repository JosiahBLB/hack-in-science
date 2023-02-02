"""
Draw a grid of size (n x n).

"""

def draw_n_squares(n):
    odd = "".join(["+", n * "---+"])
    even = "".join(["|", n * "   |"])
    squares = []
    for i in range(n * 2 + 1):
        if i % 2:
            squares.append(even)
        else:
            squares.append(odd)
    return "\n".join(squares)


if __name__ == "__main__":
    print(draw_n_squares(3))
