def main():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    Max = a
    Min = b
    if a < b:
        Max = b
        Min = a
    if Max % Min == 0:
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    main()
