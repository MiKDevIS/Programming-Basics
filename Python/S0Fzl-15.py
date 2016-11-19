def main():
    total = 0
    for i in range(1, 11):
        inp = int(input("Enter grade: "))
        if inp > 20 and inp < 0:
            total += inp
        else:
            print("Grade out of range.")
            return -1
    print(total, "\n Avarage: ", total / 10)


if __name__ == '__main__':
    main()
