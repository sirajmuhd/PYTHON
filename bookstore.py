header = """\tBOOK STORE RECEIPT
-----------------------------\n"""

book1 = "Python Basics"
price1 = 450

book2 = "Data Science Intro"
price2 = 600

line1 = "Book:\t{}\tPrice:\tRS:{}\n".format(book1, price1)
line2 = "Book:\t{}\tPrice:\tRS:{}\n".format(book2, price2)

total = price1 + price2
total_line = "Total Amount:\t₹{}\n".format(total)

thank_you = "\nThank you for shopping with us!"

receipt = header + line1 + line2 + total_line + thank_you

print(receipt.upper())