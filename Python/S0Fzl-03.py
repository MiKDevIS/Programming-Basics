def main():
    a = -1
    while a > 20 or a < 0:
        print("Note that grades must be between 20 and 0.")
        a = float(input("Please enter your grade: "))
    if a >= 10:
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    main()
