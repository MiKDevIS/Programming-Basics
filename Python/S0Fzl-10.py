def main():
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    result = 0
    if (day > 0 and day < 31) and (month < 13 and month > 0):
        if month < 7:
            result += (month - 1) * 31
        elif month > 6 and month < 13:
            result += (6 * 31) + (month - 7) * 30
        result += day
        print(result)
    else:
        print("Day or month out of range.")


if __name__ == '__main__':
    main()
