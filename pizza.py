#!/usr/bin/env python3

# Created by Devin Jhu
# Created on March 2022
# The pizza calculator

import constants


def main():
    # this calculates your pizza cost

    # input
    diameter = int(input("Enter the diameter of pizza (inch): "))

    # process
    sub_total = constants.labor + constants.rent + (diameter * constants.cost_per_ince)
    total = sub_total + (sub_total * constants.HST)

    # output
    print("")
    print("The cost for a {0} inch pizza is ${1:,.2f}".format(diameter, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
