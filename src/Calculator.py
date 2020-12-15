from src import FileParser
from decimal import *

class Calculator:
    def SalesTax(self, price, taxRate):
        tax = round(Decimal(price) * Decimal(taxRate / 100), 2)         #Decimal class in python is useful for dealing with floats representing money
        return tax

    def GenerateReceipt(self, items):
        #Main method that generates receipts
        exepmt = FileParser.FileParser().LoadExemptItems('exempt.txt')  #Creating an exempt list for the items that do not have a local sales tax

        if not items:
            print("No items in cart")
            return

        salesTax = 0                                                    #Total tax
        total = 0                                                       #Total Price
        res = []                                                        #List of results (receipt entries)

        for item in items:
            try:
                qty = item['Quantity']
                name = item['Name']
                price = item['Price']
                tax = 0

            except KeyError as e:
                print("Invalid Key: {0}".format(e.args))
                continue

            # Checking if an item is imported or not and initializing rate of tax
            # Passing in the tax rate depending on the type of item and whether it is imported or not
            if 'imported' in name:
                loc = name.replace('imported ', '')
                if loc in exepmt:
                    print("Sales tax of {0} @ 5%".format(name))
                    tax = self.SalesTax(price, 5)
                else:
                    print("Sales tax of {0} @ 15%".format(name))
                    tax = self.SalesTax(price, 15)
            else:
                if name in exepmt:
                    print("Sales tax of {0} @ 0%".format(name))
                else:
                    print("Sales tax of {0} @ 10%".format(name))
                    tax = self.SalesTax(price, 10)

            retailprice = round(Decimal(price) + Decimal(tax), 2)
            salesTax += tax
            total += retailprice

            res.append("{0} {1}: {2}".format(qty, name, retailprice))   # Gererating the receipt

        salesTax = Decimal(salesTax)                                    # Changing a binary floating point to float with 2 decimals
        print(res)
        print("Sales Tax: " + str(salesTax))
        print("Total: " + str(total))

        return [res, salesTax,total]                                    # Returning the result as a list where the first element is another list of the items, sales tax and total price


if __name__ == '__main__':
    f = Calculator()
    f.GenerateReceipt([{'Quantity': '1', 'Name': 'music CD', 'Price': 14.99},
                       {'Quantity': '1', 'Name': 'chocolate bar', 'Price': 0.85}])
