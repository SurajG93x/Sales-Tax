from decimal import *
import io


class ListGenerator:
    def GenerateItemList(self, file_handler):  # Checking if file is of the expected type
        if not isinstance(file_handler, io.IOBase):
            print("Invalid file type")
            exit()
        items = []  # List of items

        for num, line in enumerate(file_handler, 1):  # Iterating through each line in the file
            currLine = line.split()
            # print(currLine)
            item = self.CheckInputAuthenticity(currLine, num)

            if item and len(item) == 3:  # Only add the item to the list if it is a valid entry
                items.append(item)
            else:
                print("Invalid item entry")

        # print(items)
        return items

    def CheckInputAuthenticity(self, line, lineNum):
        if not line[0].isdigit():
            print("Invalid receipt format detected at line {0}. Ignoring line".format(lineNum))
            return
        item = {'Quantity': line[0]}
        # Each item will be a dictionary containing 3 values - Quantity, Name and Price

        itemname = ""
        endofname = False
        for i in range(1, len(line)):  # Iterating through the remainder of the string after the quantity
            s = line[i]
            if s.isalpha():
                if s == "at":
                    item[
                        'Name'] = itemname.strip()  # Adding the name to the dictionary when you reach an 'at' while removing trailing or leading whitespaces
                    endofname = True
                elif not endofname:
                    itemname += s + " "  # Adding a whitespace to the end of the string so the spaces are maintained in the name sequence
                else:
                    print("Invalid format at line {0}".format(lineNum))
                    break
            else:
                if len(s.rsplit('.')[-1]) <= 2:
                    try:
                        s = float(s)
                        price = Decimal(s)
                        item['Price'] = price
                    except ValueError:  # Checking if there are any alien characters after 'at'
                        print("Invalid characters detected in line {0}. Skipping".format(lineNum))
                        break
                else:
                    print("Invalid price for {0}".format(itemname))

        return item


if __name__ == '__main__':  # Failing test (expected to fail)
    f = ListGenerator()
    # f.GenerateItemList('file')

    f.CheckInputAuthenticity(['x,y', 'sppe'], 2)  # Input line type test
