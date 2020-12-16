class FileParser:
    def LoadFile(self, file):
        try:
            file_handler = open(file,'r')
            return file_handler
        except FileNotFoundError as e:
            print("Invalid File Name: {0}".format(e.args[1]))   #Incase the file name is invalid
            exit()

    def LoadExemptItemList(self, file):
        #Uses a text file to build the list of tax exempt items that can be modified on the fly
        try:
            file_handler = open(file,'r')
        except FileNotFoundError as e:
            print("Invalid File Name: {0}".format(e.args[1]))
            print("Using default exemption list")
            file_handler = open('exempt.txt', 'r')

        exemptList = []

        for num, line in enumerate(file_handler, 1):
            line = line.rstrip('\n')
            exemptList.append(line)
            # else:
            #     print("Invalid characters detected in line {0} for exempt file. Skipping".format(num))
            #     continue

        return exemptList

    def SaveFile(self, raw, name="receipt.txt"):
        #Saves the receipt as a text file
        if not name.endswith('.txt'):
            name += '.txt'
        f = open(name, "w")

        receipt = raw[0]
        for item in receipt:
            f.write(item + "\n")
        f.write("Sales Tax: "+str(raw[1])+"\n")
        f.write("Total: "+str(raw[2]))


if __name__ == '__main__':  # Unit test
    f = FileParser()
    f.LoadFile('input2.txt')
