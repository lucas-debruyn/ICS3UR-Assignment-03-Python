#!/usr/bin/env python3

# Created by: Lucas DeBruyn
# Created on: Oct 2022
# This program calculates the cost of croissants

import constants


def main():
    # this function calculates the cost of croissants

    # input
    amount = int(input("Enter the amount of croissants you would " + "like (amount): "))

    sub_total = amount * (constants.COST_PER_CROISSANTS)

    # process
    if amount >= constants.MAGIC_NUMBER:
        tax_total = sub_total * (constants.HST)
        total = sub_total + tax_total

    if amount < constants.MAGIC_NUMBER:
        total = sub_total

    # output
    print("The cost for {0} croissants is ${1:,.2f}".format(amount, total))

    print("\nDone.")


if __name__ == "__main__":
    main()
