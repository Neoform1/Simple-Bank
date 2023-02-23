# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function

class BankAccount:
    def __init__(self, id, first_name, last_name, email):
        self.balance = 0
        self.id = input("Enter your id: ")
        self.first_name = input("Enter your first name: ")
        self.last_name = input("Enter your last name: ")
        self.email = input("Enter your email: ")
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def getName(self):
        return self.first_name





    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)
        if amount <= 0:
            raise Exception('The amount must be positive.')




    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")

    def display(self):
        print("\n Net Available Balance=", self.balance)


# Driver code


# creating an object of class
s = BankAccount(1, first_name="Artyom", last_name="Z", email="mail@mail.com")

# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()
