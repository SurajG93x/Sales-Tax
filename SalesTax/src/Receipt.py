from decimal import *
from src import Calculator as cal
import unittest


class Receipt:
    def __init__(self, items, exemptions):  # Constructor
        self.items = items
        self.exemptions = exemptions

    def GenerateReceipt(self):
        # Main method that generates receipts
        items = self.items
        exemptions = self.exemptions

        if not items:
            print("No items in cart")
            return

        salesTax = 0  # Total tax
        total = 0  # Total Price
        res = []  # List of results (receipt entries)

        for item in items:
            try:
                qty = item['Quantity']
                name = item['Name']
                price = item['Price']
                tax = 0

            except KeyError as e:
                print("Invalid Key: {0}".format(e.args))
                continue

            calc = cal.TaxCalculator()

            # Checking if an item is imported or not and initializing rate of tax
            # Passing in the tax rate depending on the type of item and whether it is imported or not
            if exemptions:
                if 'imported' in name:
                    loc = name.replace('imported ', '')
                    taxRate = 5 if loc in exemptions else 15
                else:
                    taxRate = 0 if name in exemptions else 10
            else:
                if 'imported' in name:
                    taxRate = 15
                else:
                    taxRate = 10

            # print("Tax rate of item {0} is {1}".format(name,taxRate))
            tax = calc.SalesTax(price, taxRate)
            retailprice = round(Decimal(price) + Decimal(tax), 2)
            salesTax += tax
            total += retailprice

            res.append("{0} {1}: {2}".format(qty, name, retailprice))  # Gererating the receipt

        salesTax = Decimal(salesTax)  # Changing a binary floating point to float with 2 decimals
        # print(res)
        # print("Sales Tax: " + str(salesTax))
        # print("Total: " + str(total))

        return [res, salesTax,
                total]  # Returning the result as a list where the first element is another list of the items, sales tax and total price


if __name__ == '__main__':  # Unit test
    items = [{'Quantity': '1', 'Name': 'book', 'Price': '12.49'},
             {'Quantity': '1', 'Name': 'music CD', 'Price': '14.99'},
             {'Quantity': '1', 'Name': 'chocolate bar', 'Price': '0.85'}]
    exemptions = ['book', 'books', 'boxes of chocolates', 'box of chocolates', 'chocolate bar', 'chocolate bars']
    f = Receipt(items, exemptions)
    print(f.GenerateReceipt())
