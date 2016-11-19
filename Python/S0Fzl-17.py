def main():
    inp = int(input("Enter an integer: "))
    result = 1
    if inp == 0 or inp == 1:
        print(1)
    else:
        for i in range(1, inp + 1):
            result *= i
        print(result)


if __name__ == '__main__':
    main()
