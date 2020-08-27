# GENERATING ACCOUNT NUMBER


# import random


# class User():

#     def __init__(self, name, age, email, phone):

#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone


# class Account(User):

#     # balance = 0
#     # account_no = ""

#     def __init__(self, name, age, email, phone):

#         # INITIALIZE ATTRIBUTES FROM PARFENT CLASS
#         super().__init__(name, age, email, phone)

#         self.balance = 0
#         self.account_no = self.generate_acct_no()

#     def generate_acct_no(self):

#         account_num = random.randint(3000000000, 3000009999)
#         return str(account_num)


# x = Account("Tobi", 23, "tobi@tobiallen.com", "08025291194")
# print(x.account_no)

######################

# DEPOSIT

# import random


# class User():

#     def __init__(self, name, age, email, phone):

#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone


# class Account(User):

#     # balance = 0
#     # account_no = ""

#     def __init__(self, name, age, email, phone):

#         # INITIALIZE ATTRIBUTES FROM PARFENT CLASS
#         super().__init__(name, age, email, phone)

#         self.balance = 0
#         self.account_no = self.generate_acct_no()

#     def generate_acct_no(self):

#         account_num = random.randint(3000000000, 3000009999)
#         return str(account_num)

#     def deposit(self, amount):

#         self.balance += amount  # ADD DEPOSIT VALUE TO BALANCE\

#         print(
#             f"Well done {self.name}, Your deposit of ₦{amount} was successful. Your new balance is ₦{self.balance}.")


# x = Account("Tobi", 23, "tobi@tobiallen.com", "08025291194")
# print(x.account_no)
# x.deposit(20000)


# WITHDRAWAL

# import random


# class User():

#     def __init__(self, name, age, email, phone):

#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone


# class Account(User):

#     # balance = 0
#     # account_no = ""

#     def __init__(self, name, age, email, phone):

#         # INITIALIZE ATTRIBUTES FROM PARFENT CLASS
#         super().__init__(name, age, email, phone)

#         self.balance = 0
#         self.account_no = self.generate_acct_no()

#     def generate_acct_no(self):

#         account_num = random.randint(3000000000, 3000009999)
#         return str(account_num)

#     def deposit(self, amount):

#         self.balance += amount  # ADD DEPOSIT VALUE TO BALANCE\

#         print(
#             f"Well done {self.name}, Your deposit of ₦{amount} was successful. Your new balance is ₦{self.balance}.")

#     def withdrawal(self, amount):

#         self.balance -= amount  # ADD DEPOSIT VALUE TO BALANCE\

#         print(
#             f"Hello {self.name}, Your withdrawal of ₦{amount} was successful. Your new balance is ₦{self.balance}.")


# x = Account("Tobi", 23, "tobi@tobiallen.com", "08025291194")
# print(x.account_no)
# x.deposit(20000)
# x.withdrawal(10000)


# TRANSACTION HISTORY

import random


class User():

    def __init__(self, name, age, email, phone):

        self.name = name
        self.age = age
        self.email = email
        self.phone = phone


class Account(User):

    # balance = 0
    # account_no = ""

    def __init__(self, name, age, email, phone):

        # INITIALIZE ATTRIBUTES FROM PARFENT CLASS
        super().__init__(name, age, email, phone)

        self.balance = 0
        self.account_no = self.generate_acct_no()

    def generate_acct_no(self):

        account_num = random.randint(3000000000, 3000009999)
        return str(account_num)

    def deposit(self, amount, comment=""):

        self.balance += amount  # ADD DEPOSIT VALUE TO BALANCE\
        self.store_history("credit", amount, comment)

        print(
            f"Well done {self.name}, Your deposit of ₦{amount} was successful. Your new balance is ₦{self.balance}.")

    def withdrawal(self, amount, comment=""):

        self.balance -= amount  # ADD DEPOSIT VALUE TO BALANCE\
        self.store_history("debit", amount, comment)

        print(
            f"Hello {self.name}, Your withdrawal of ₦{amount} was successful. Your new balance is ₦{self.balance}.")

    def transfer(self, amount, recipient, comment=""):

        self.balance -= amount
        recipient.balance += amount
        self.store_history("transfer", amount, comment, recipient.name)

        print(
            f"Congratulations {self.name}, Your transfer of ₦{amount} to {recipient.name} was successful. Your new balance is ₦{self.balance}.")

    def store_history(self, type, amount, comment, receiver="same as sender"):
        file = open("financial_statement.csv", "a")
        file.write(f"{type},{self.name},{amount},{comment},{receiver}\n")
        print(type, amount, comment, receiver)


tobi = Account("Tobi", 23, "tobi@tobiallen.com", "08025291194")
tobi.deposit(20000)
tobi.withdrawal(10000)
ayo = Account("Ayo", 29, "ayo@tobiallen.com", "08023456789")
tobi.transfer(2000, ayo, "Testing")
