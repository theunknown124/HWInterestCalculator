#!/usr/bin/env python3

from decimal import Decimal
from decimal import ROUND_HALF_UP
from decimal import ROUND_HALF_DOWN
import locale as lc

def getLoanAmount():
    userLoanAmount = float(input("Enter loan amount: "))
    return userLoanAmount

def get_interest_rate():
    userInterestRate = float(input("Enter interest rate: "))
    print()
    return userInterestRate

def main():
    lc.setlocale(lc.LC_ALL, "us")
    print("Interest Calculator")
    print()

    choice = "y"
    while choice.lower() == "y":
        # get loan amount and interest rate from the user
        loanAmount = userLoanAmount = float(input("Enter loan amount: "))
        interestRate = userInterestRate = float(input("Enter interest rate: "))

        # quantize the entries
        loan_amount = Decimal(loanAmount).quantize(Decimal("0.00"))
        interest_rate = Decimal(interestRate).quantize(Decimal("1.000"))


        # calculate and quantize the interest amount
        interestAmount = loan_amount * (interest_rate / 100)
        interestAmount = Decimal(interestAmount).quantize(Decimal("0.00"))

        # format and display the results
        line = "{:20} {:>10}"
        #print("\nLoan amount:  {:10,.2f}".format((loan_amount,grouping=True)))
        print(line.format("\nLoan amount:",lc.currency(loan_amount, grouping=True)))
        print(line.format("Interest rate:","{}%".format(interest_rate)))
        #print("Interest amount  {:10,.2f}".format(lc.currency(interestAmount, grouping=True)))
        print(line.format("Interest amount:",lc.currency(interestAmount, grouping=True)))

        choice = input("\nContinue? (y/n): ")
        print()

    print("Bye!")

if __name__ == "__main__":
    main()
