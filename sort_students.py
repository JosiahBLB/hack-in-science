def sort_by_mark(my_class):
    my_class.sort(reverse=True, key=lambda x: x[0])
    return my_class

def sort_by_name(my_class):
    my_class.sort(key=lambda x: x[1])
    return my_class


if __name__ == "__main__":
    my_class = [(25, "Shannon"), (50, "Alan"), (75, "Ada")]

    print(sort_by_mark(my_class))
    print(sort_by_name(my_class))