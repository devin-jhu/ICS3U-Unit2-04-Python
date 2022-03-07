#!/usr/bin/env python3

# Created by Devin Jhu
# Created on March 2022
# The area and perimeter calculator


def main():
    # this function calculates the area and perimeter of a rectangle

    # input
    width = int(input("Enter width of rectangle(mm): "))
    height = int(input("Enter height of rectangle(mm): "))

    # process
    area_of_rectangle = width * height
    perimeter_of_rectangle = 2 * (width + height)

    # output
    print("")
    print("Area is {0} mm².".format(area_of_rectangle))
    print("Perimeter is {0} mm.".format(perimeter_of_rectangle))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
