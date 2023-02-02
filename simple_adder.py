from sys import argv

def adder(x, y):
    try:
        return print(x + y)
    except:
        return print("usage: python3 solution.py OP1 OP2")
        
if __name__ == "__main__":
    adder(argv[1], argv[2])