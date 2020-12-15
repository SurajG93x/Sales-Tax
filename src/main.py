from src import FileParser

def main():
    #Takes in one file - The shopping cart
    file = input("Enter file name of the cart if the file in the same directory or the entire path :")
    dh = FileParser.FileParser()
    dh.LoadFile(file)


if __name__ == "__main__":
    main()