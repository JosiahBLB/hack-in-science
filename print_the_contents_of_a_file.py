"""
Print the contents of a file

"""

if __name__ == "__main__":
    with open("words.txt", "r") as file:
        print(file.read())
