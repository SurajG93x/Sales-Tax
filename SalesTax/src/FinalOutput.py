class Controller:
    def PrintReceipt(self, receipt):
        if len(receipt) == 3:  # output the receipt on the interface
            for item in receipt[0]:
                print(item)
            print("Sales Tax: " + str(receipt[1]))
            print("Total: " + str(receipt[2]))
        else:
            print("Error creating receipt")
            return
