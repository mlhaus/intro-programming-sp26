import temperature as temp

def main():
    f = 212
    c = temp.to_celsius(f)
    print(f"{f} degrees fahrenheit is  {c} degrees celsius")
    c = 0
    f = temp.to_fahrenheit(c)
    print(f"{c} degrees celsius is {f} degrees fahrenheit")

if(__name__ == "__main__"):
    main()