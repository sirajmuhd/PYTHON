# Base class
class Account:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

   
    def __add__(self, other):
        return self._balance + other._balance



class SavingsAccount(Account):

    def calculate_interest(self):
        return self._balance * 0.05



class CurrentAccount(Account):

    def calculate_interest(self):
        return self._balance * 0.02



sav1 = SavingsAccount("Ravi", 10000)

cur1 = CurrentAccount("Anjali", 15000)



print("Savings Account")
print("Name:", sav1._name)
print("Balance:", sav1._balance)
print("Interest:", sav1.calculate_interest())



print("\nCurrent Account")
print("Name:", cur1._name)
print("Balance:", cur1._balance)
print("Interest:", cur1.calculate_interest())



total = sav1 + cur1

print("Total Balance:", total)