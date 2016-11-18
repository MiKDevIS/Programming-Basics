def main():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = int(input("Enter 3rd number: "))
    tmp = b
    b = a
    tmp1 = c
    c = tmp
    a = tmp1
    print(a, b, c, sep=' ')


if __name__ == '__main__':
    main()
