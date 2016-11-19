def main():
    for i in range(100, 1000):
        if (i % 2 != 0) and (int(i / 10) % 2 == 0) and (int(i / 100) % 5 == 0):
            print(i)


if __name__ == '__main__':
    main()
