from decimal import *
import unittest

class TaxCalculator:
    def SalesTax(self, price, taxRate):
        tax = round(Decimal(price) * Decimal(taxRate / 100), 2)         #Decimal class in python is useful for dealing with floats representing money
        return tax


class SimplisticTest(unittest.TestCase):                                #Unit tests for calculating sales taxes
    def testNotEqual(self):
        tc = TaxCalculator()
        self.failUnlessEqual(tc.SalesTax(50,15), 7.50)

    def testNotEqual2(self):
        tc = TaxCalculator()
        self.failUnlessEqual(tc.SalesTax(75.50, 15), 11.32)

if __name__ == '__main__':                                              #test
    unittest.main()
