def main():
    a = int(input("Please enter 1st number: "))
    b = int(input("Please enter 2nd number: "))
    a = a + b
    b = a - b
    a = a - b
    print(a, b, sep='\n')


if __name__ == '__main__':
    main()
