from src import Calculator as cal
from decimal import *

class FileParser:
    def LoadFile(self, file):
        try:
            file_handler = open(file,'r')
        except FileNotFoundError as e:
            print("Invalid File Name: {0}".format(e.args[1]))   #Incase the file name is invalid
            return

        items = []      #List of items

        for num, line in enumerate(file_handler, 1):        #Iterating through each line in the file
            currLine = line.split()
            print(currLine)
            if not currLine[0].isdigit():
                print("Invalid receipt format detected at line {0}. Ignoring line".format(num))
                continue
            item = {'Quantity' : currLine[0]}
            #Each item will be a dictionary containing 3 values - Quantity, Name and Price

            itemname = ""
            for i in range(1,len(currLine)):                #Iterating through the remainder of the string after the quantity
                s = currLine[i]
                if s.isalpha():
                    if s == "at":
                        item['Name'] = itemname.strip()     #Adding the name to the dictionary when you reach an 'at' while removing trailing or leading whitespaces
                    else:
                        itemname += s + " "                 #Adding a whitespace to the end of the string so the spaces are maintained in the name sequence
                else:
                    try:
                        price = Decimal(s)
                        item['Price'] = price
                    except ValueError as e:                 #Checking if there are any alien characters after 'at'
                        print("Invalid characters detected in line {0}. Skipping".format(num))
                        break

            if len(item) == 3:                              #Only add the item to the list if it is a valid entry
                items.append(item)

        print(items)
        c = cal.Calculator()
        rawReceipt = c.GenerateReceipt(items)               #Calculates the taxes
        self.SaveFile(rawReceipt)                           #Saves result to another file

    def LoadExemptItems(self, file):
        #Uses a text file to build the list of tax exempt items that can be modified on the fly
        try:
            file_handler = open(file,'r')
        except FileNotFoundError as e:
            print("Invalid File Name: {0}".format(e.args[1]))
            return

        exemptList = []

        for num, line in enumerate(file_handler, 1):
            line = line.rstrip('\n')
            exemptList.append(line)
            # else:
            #     print("Invalid characters detected in line {0} for exempt file. Skipping".format(num))
            #     continue

        return exemptList

    def SaveFile(self, raw):
        #Saves the receipt as a text file
        f = open("receipt.txt", "w")
        receipt = raw[0]
        for item in receipt:
            f.write(item + "\n")
        f.write("Sales Tax: "+str(raw[1])+"\n")
        f.write("Total: "+str(raw[2]))


if __name__ == '__main__':
    f = FileParser()
    f.LoadFile('input2.txt')