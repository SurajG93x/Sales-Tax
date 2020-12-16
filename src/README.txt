################################################################################################READ-ME################################################################################################

IMPORTANT: This program is written in Python 3.6+

SALES TAX CALCULATOR:
This program takes in a text file that represents a shopping cart and calculates the taxes depending on the nature of the item.
It prints out the results to an output file called receipt.txt

PROGRAM STRUCTURE:
The program consists of 3 different python files classified by functionality.
main.py is the point of start that takes in a file name (along with the extension) and calls the corresponding methods to calculate the taxes
FileParser.py, as the name suggests, parses a file, builds the lists and passes it on to the Calculator for calculations and then gets the result and builds the receipts.
Calculator.py receives lists from the parser and runs the calculations(taxes) on them and returns the result as a list.

ASSUMPTIONS:
1. The names of items do not contain any digits or special characters. (Can be changed by using regex)
2. The input file for the shopping cart follows a specific pattern - <Quantity> <Name of the item(s)> at <Price>
3. Any line in the file that does not follow the said pattern is skipped.
4. If all the lines of the input file are invalid, the program returns a "No items in cart" on the CL and exits.
5. The file exempt.txt has a list of all the items (books, foods and medicine) that are tax exempt.
6. Any item that is not a part of this list will NOT be counted towards tax exemption regardless of the nature of the item.
7. Taxes are calculated at the following rates depending on the nature of the item:
    a. A tax exempt local item has a tax rate of 0%.
    b. A non-tax exempt local item has a tax rate of 10%.
    c. An imported tax exempt item has an import duty at the rate of 5%.
    d. An imported non-tax exempt item has a tax rate of 10% and an import duty of 5% bringing a total of 15%.
        This can be changed later depending on how the import duty is calculated. The 5% can be added on top of the 10% sales tax or before.
        But for maintaining simplicity for this mini-project, I chose to directly add the overall percentage.
8. The exempt.txt file has 2 entries per item. One of them is a single and the other being multiple. This is due to the one-on-one mapping on the names directly with this list.

EXPLANATION:

I.main.py:
As mentioned, this class acts the main executable for this project.
This is the point of contact that takes in user input in the form of the name of the text file. The input must include the name of the file as well as the extension.
For example, the name of the file "input1.txt" will be input1.txt instead of just 'input1'.
This can be changed later on to just name the file if we want a more scalable solution by adding the extension to it depending on the nature of the file.

II.Parsing Files
This class has three methods-
    LoadFile() method takes in the file directly received from main.py and parses ir constructing a list of items.
Each line as assumed to have a specific format <quantity> <name of the product/item> 'at' <price>.
This builds a list of dictionaries having the following keys per item - quantity(string/int), name(string) and price(decimal).
I used Decimals for dealing with money representations since it has in built methods that adds a trailing zero if there is a single point, rounds up any float values to 2 points and other features.
If by any chance the dictionary has more or less than three values, the entry is not added to the final list of items.
    LoadExemptItems() takes another text file that contains a list of tax exempt items and generates a list of items that are/will be tax exempt.
Each item will have 2 entries, one for a single item and another for multiple. This is because the calculator does a direct check to see if the item is a part of this list.
Having a list for this has many advantages in terms of scalability.
For example, this can be attached on a DB later to directly append the names of the products terms as one of three sales tax exempt categories.
ML can also be implemented later on to directly deal with multiple iterations of the same object.
    SaveFile() receives a list of 3 items - a list of receipt strings, the total price and the total sales tax.
This will then generate the receipt in the format-
<quantity> <name if item>: <price with taxes>
.
.
n items
Total Tax: <total tax>
Total: <total price with taxes included>

III. Calculating taxes
    The method GenerateReceipt() needs 2 lists - one that is received from fileparser's loadfile method. And another list of of items that are tax exempt.
It then goes through each element in the item list and does 2 operations on it. Firstly, it checks if there is a word "imported" in the name to see if it needs an Import duty attached to it.
Next, it removes this word from the name temporarily and checks if the item qualifies for tax exemption by checking it against the list of exempt items.
Depending on the output of these 2 checks, the method SalesTax() is called on the price of each item which also takes a parameter for tax rate.
It calculates the tax for each item and returns it. The method GenerateReceipt() then creates three variables.
First, it generates the string of each line in the receipt per item and appends them all to a list. Next it creates a total of the sales tax.
And finally, it generates another total of the overall price. It appends all of these to a list (where the first element is another list) and sends it back to the parser.
I chose to create a list here since it made sense to just return one list for this project.
In terms of scalability, this can later be expanded upon to iteratively call two separate functions to keep track of the running total and sales total.

UPDATE: A new class for generating itemList has been created.
Functionality from the LoadFile() method have been relocated to this class and split into two methods - GenerateItemList and CheckInputAuthenticity

UPDATE 2: Another class for receipts has been created. It only has one method - GenerateReceipt

UPDATE 3: Made SaveFile optional

##################################################################################################END##################################################################################################