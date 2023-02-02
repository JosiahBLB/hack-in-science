"""
My first http request

"""

import requests


if __name__ == "__main__":
    try:
        r = requests.get("https://api.github.com/users/python")
        print(r.text)
    except requests.exceptions.ConnectionError:
        print("No internet connectivity.")
