def battery_charge(level):
    return print("[{}]\n{}%".format(("❚" * (round(level / 10))).ljust(10, " "), level))

if __name__ == "__main__":
    battery_charge(50)
