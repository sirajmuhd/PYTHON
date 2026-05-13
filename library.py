import re

try:
    
    title = input("Enter book title: ")

    
    if not re.fullmatch(r"[A-Za-z ]+", title):
        raise ValueError("Book title must contain only alphabets and spaces.")

    
    year = input("Enter publication year: ")

    
    if not re.fullmatch(r"(19|20)\d{2}", year):
        raise ValueError("Publication year must be a 4-digit number starting with 19 or 20.")

    
    print("\nBook Details Accepted")
    print("Title:", title)
    print("Publication Year:", year)

except ValueError as e:
    print("\nError:", e)

finally:
    print("\nProgram finished.")