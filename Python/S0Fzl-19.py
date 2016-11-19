def main():
    inp = int(input("Enter an integer: "))
    for i in range(1, inp + 1):
        if inp % i == 0:
            print(i)


if __name__ == '__main__':
    main()
