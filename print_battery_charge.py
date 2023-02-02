def battery_charge(level):
    return print("[{}]\n{}%".format(("❚"*(round(level/10))).ljust(10, " "), level))

battery_charge(50)