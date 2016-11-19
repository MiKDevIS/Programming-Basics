def main():
    a = input("Enter a number: ")
    result = 0
    for i in range(len(a)):
        result += int(a[i])
    print(result)


if __name__ == '__main__':
    main()
