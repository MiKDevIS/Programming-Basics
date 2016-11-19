def main():
    n = int(input("Enter an integer: "))
    if n >= 0:
        for i in range(n + 1, 1, -1):
            if i % 2 == 0:
                print(i)
    else:
        print("Integer must be positive.")


if __name__ == '__main__':
    main()
