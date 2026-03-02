# from temperature import to_celsius, to_fahrenheit
from temperature import *

def main():
    f = 212
    c = to_celsius(f)
    print(f"{f} degrees fahrenheit is  {c} degrees celsius")
    c = 0
    f = to_fahrenheit(c)
    print(f"{c} degrees celsius is {f} degrees fahrenheit")

if(__name__ == "__main__"):
    main()