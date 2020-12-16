from src import FileParser as FP
from src import ItemListGenerator as gen
from src import Receipt as rec
from src import FinalOutput as fot
import time


def main():
    # Takes in one file - The shopping cart
    fp = FP.FileParser()

    file = input("Enter file name of the cart if the file in the same directory or the entire path :")
    openFile = fp.LoadFile(file)

    time.sleep(1)
    listGen = gen.ListGenerator()
    itemList = listGen.GenerateItemList(openFile)  # Gets list of items

    exemptitems = fp.LoadExemptItemList(
        'exempt.txt')  # Creating an exempt list for the items that do not have a local sales tax

    if not exemptitems:
        print("No exemption list detected")  # If no list is found, no items are considered tax exempt

    receiptGen = rec.Receipt(itemList, exemptitems)
    receipt = receiptGen.GenerateReceipt()

    ctrl = fot.Controller()
    ctrl.PrintReceipt(receipt)

    save = input("Do you want to save the receipt(Y/N)?:")  # Save the receipt as a txt file if needed
    if save.upper() == "Y":
        fileName = input("Enter file name:")
        if fileName:
            fp.SaveFile(receipt, fileName)


if __name__ == "__main__":
    main()
