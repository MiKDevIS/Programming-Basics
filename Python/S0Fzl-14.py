def main():
    a = int(input("Enter lower bound: "))
    b = int(input("Enter upper bound: "))
    for i in range(a, b):
        if i % 2 != 0:
            print(i)


if __name__ == '__main__':
    main()
