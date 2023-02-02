import re

with open('words.txt', 'r') as file:
    print(len(re.findall(re.compile(r'[e]'), file.read())))