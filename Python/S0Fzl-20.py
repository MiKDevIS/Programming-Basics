def main():
    inp = int(input("Enter an integer: "))
    result = 0
    for i in range(1, inp + 1):
        if inp % i == 0:
            result += i
    print(result)


if __name__ == '__main__':
    main()
