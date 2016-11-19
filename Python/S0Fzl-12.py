def main():
    n = int(input("Enter an integer: "))
    if n >= 0:
        for i in range(1, n + 1):
            print(i)
    else:
        print("Integer must be positive.")


if __name__ == '__main__':
    main()
