""" 
Count the number of occurances of 'e' within a text document. 

"""

import re


def count_e_occurances(file):
    with open(file, "r") as file:
        return print(len(re.findall(re.compile(r"[e]"), file.read())))


if __name__ == "__main__":
    count_e_occurances("words.txt")
