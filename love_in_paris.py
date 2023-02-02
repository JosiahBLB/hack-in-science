def love_meet(bob, alice):
    bob = set(bob)
    alice = set(alice)
    visited = bob.intersection(alice)
    return set(visited)

if __name__ == "__main__":
    love_meet()