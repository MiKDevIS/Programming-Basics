def main():
    inp = int(input("Enter a number: "))
    if (inp / 1000) > 1:
        print(inp, "has more than 3 digits.")
    elif (inp / 100) > 1:
        print(inp, "has more than 2 digits.")
    elif (inp / 10) > 1:
        print(inp, "has more than 1 digits.")
    elif inp < 10:
        print(inp, "has 1 digit.")


if __name__ == '__main__':
    main()
