def main():
    n = int(input("Enter an integer: "))
    for i in range(n + 1, 1, -1):
        if i % 2 == 0:
            print(i)


if __name__ == '__main__':
    main()
