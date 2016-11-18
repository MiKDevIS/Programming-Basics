def main():
    a = float(input("Please enter your grade: "))
    if a <= 20 and a > 0:
        if a >= 10:
            print("Pass")
        else:
            print("Fail")
    else:
        print("Grade out of range.")


if __name__ == "__main__":
    main()
