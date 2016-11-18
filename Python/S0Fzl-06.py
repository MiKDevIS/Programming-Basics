def main():
    length = int(input("Please enter length of the rectangle: "))
    width = int(input("Please enter width of rectangle: "))
    p = 2 * (length + width)
    s = length * width
    print("Surface: ", s)
    print("Perimeter: ", p)


if __name__ == "__main__":
    main()
