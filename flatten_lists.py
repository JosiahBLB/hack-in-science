"""
Flatten a nested list.

"""

def flatten(nested_list):
    flattened_list = []
    for item in nested_list:
        if type(item) == list:
            flattened_list += flatten(item)
        else:
            flattened_list.append(item)
    return flattened_list


if __name__ == "__main__":
    myList = [1, 2, [3, [4, 3, 5]]]
    print(flatten(myList))
