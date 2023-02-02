from itertools import chain

def perfect_shuffle(deck):
    if len(deck) == 0:
        return deck
    divisor = len(deck)//2
    first_half  = deck[0:divisor] 
    second_half = deck[divisor:-1]
    deck = []
    for n, m in zip(first_half, second_half):
        deck.append(n).append(m)
    return deck

# Not my solution
def perfect_shuffle_copied(deck: list):
    deck = list(chain(*zip(deck[len(deck)//2:],deck[:len(deck)//2])))
    return deck

# Perfect shuffle 6 times returns deck to original state:
my_list1 = [1, 2, 3, 4, 5, 6]
for _ in range(6):
    my_list1 = perfect_shuffle_copied(my_list)
    print(my_list)