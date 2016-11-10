def main():
    a = int(input("Please enter 1st number: "))
    b = int(input("Please enter 2nd number: "))
    tmp = a
    a = b
    b = tmp
    print(a, b, sep='\n')


if __name__ == '__main__':
    main()
