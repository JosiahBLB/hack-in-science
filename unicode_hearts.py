import unicodedata as ucd

if __name__ == "__main__":
    for i in range(50,230000):
        num = str(chr(i))
        name = ucd.name(num,'')
        if "heart" in name.lower():
            print(ucd.lookup(name), end='')