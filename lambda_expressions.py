def filtered(items, func):
    return filter(func, items)

if __name__ == "__main__":
    print(str(list(filtered((x for x in range(101)), lambda x: x%3 == 0))).strip("[]"))
    print(str(list(filtered((x for x in range(101)), lambda x: x%5 == 0))).strip("[]"))
    print(str(list(filtered((x for x in range(101)), lambda x: x%15 == 0))).strip("[]"))