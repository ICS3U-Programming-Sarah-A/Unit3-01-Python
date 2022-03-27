#!/usr/bin/env python3

# Created by: Sarah
# Created on: Mar 25, 2022
# This program calculates total from subtotal and tax


import constants


def main():
    # this function calculates total from subtotal and tax

    # get subtotal from the user
    sub_total = float(input("Enter the subtotal: $"))

    # calculate tax and sutotal
    tax = sub_total * constants.HST
    total = sub_total + tax

    # display results, tax and subtotal
    print("")
    print("The HST is ${0:,.2f}, and the total cost is: ${1:,.2f}"
          .format(tax, total))


if __name__ == "__main__":
    main()
