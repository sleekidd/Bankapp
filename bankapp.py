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

#     def deposit(self, amount, comment="no comment", source=False):

#         transaction_label = "credit"

#         if source:
#             transaction_type = "transfer"
#             source = source.name
#         else:
#             transaction_type = "deposit"
#             source = self.name

#         self.balance += amount  # ADD DEPOSIT VALUE TO BALANCE\
#         self.store_history(transaction_type, transaction_label,
#                            amount, self.name, comment, source)

#         print(
#             f"Well done {self.name}, Your deposit of ₦{amount} was successful. Your new balance is ₦{self.balance}.")

#     def withdrawal(self, amount, comment="no comment", collector=False):

#         transaction_label = "dedit"

#         if collector:
#             transaction_type = "transfer"
#             collector = collector.name
#         else:
#             transaction_type = "withdrawal"
#             collector = self.name

#         self.balance -= amount  # ADD DEPOSIT VALUE TO BALANCE\
#         self.store_history(transaction_type, transaction_label,
#                            amount, self.name, comment, collector)

#         print(
#             f"Hello {self.name}, Your withdrawal of ₦{amount} was successful. Your new balance is ₦{self.balance}.")

#     def transfer(self, amount, recipient, comment=""):

#         self.withdrawal(amount, comment, recipient)
#         recipient.deposit(amount, comment, self)

#         # self.balance -= amount
#         # recipient.balance += amount
#         # self.store_history("transfer", amount, comment, recipient.name)

#         print(
#             f"Congratulations {self.name}, Your transfer of ₦{amount} to {recipient.name} was successful. Your new balance is ₦{self.balance}.")

#     def store_history(self, transaction_type, transaction_label,
#                       amount, source, comment, receiver="same"):
#         file = open("financial_statement.csv", "a")
#         file.write(
#             f"{transaction_type}, {transaction_label}, {amount}, {source}, {receiver}, {comment}\n")
#         print(transaction_type, amount, comment, receiver)


# tobi = Account("Tobi", 23, "tobi@tobiallen.com", "08025291194")
# tobi.deposit(20000)
# tobi.withdrawal(10000)
# ayo = Account("Ayo", 29, "ayo@tobiallen.com", "08023456789")
# tobi.transfer(2000, ayo, "Testing")


import random


class User():

    def __init__(self, name, age, email, phone):

        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.is_logged_in = False

        # self.create_user()
        # self.login()

    def create_user(self):

        self.name = input("Please enter your name: ")
        self.age = input("Please enter your age: ")
        self.email = input("Please enter your email: ")
        self.phone = input("Please enter your phone: ")
        password = input("Please enter your password: ")
        balance = 0

        users_file_name = "users.csv"
        users_file = open(users_file_name, "a")

        users_file.write(
            f"{self.name},{password},{self.age},{self.email},{self.phone},{balance}\n")
        users_file.close()

    def login(self):

        input_name = input("Please enter your name: ")
        input_password = input("Please enter your password: ")

        users_file_name = "users.csv"
        users_file = open(users_file_name, "r")

        for line in users_file.readlines():
            # print(line.split(","))
            name, saved_password, age, email, phone, balance = line.split(",")
            # print(saved_password, input_password)

            if name == input_name:

                if saved_password == input_password:
                    self.is_logged_in = True

                    self.name = name
                    self.age = age
                    self.email = email
                    self.phone = phone
                    self.balance = float(balance)

                    print(f"successfully logged in {self.name}")

                    # return

                    break

                else:
                    print(f"Sorry {input_password} is a wrong password!!")
                    self.login()

        else:
            print(f"Sorry the username {input_name} does not exist")
            self.create_user()


class Account(User):

    # balance = 0
    # account_no = ""

    def __init__(self, name="nil", age=0, email="nil", phone="nil"):

        # INITIALIZE ATTRIBUTES FROM PARFENT CLASS
        super().__init__(name, age, email, phone)

        self.balance = 0
        self.account_no = self.generate_acct_no()

    def generate_acct_no(self):

        account_num = random.randint(3000000000, 3000009999)
        return str(account_num)

    def deposit(self, amount, comment="no comment", source=False):

        transaction_label = "credit"

        if source:
            transaction_type = "transfer"
            source = source.name
        else:
            transaction_type = "deposit"
            source = self.name

        self.balance += amount  # ADD DEPOSIT VALUE TO BALANCE\
        self.write_balance_value(self.balance)
        self.store_history(transaction_type, transaction_label,
                           amount, self.name, comment, source)

        print(
            f"Well done {self.name}, Your deposit of ₦{amount} was successful. Your new balance is ₦{self.balance}.")

    def write_balance_value(self, amount):

        user_file = open("users.csv", "r")

        data = user_file.read()

        user_file.close()

        user_file = open("users.csv", "w")

        new_data = ""

        for line in data.splitlines():
            name, password, age, email, phone, balance = line.split(",")

            if self.name == name:

                balance = amount

            new_data += f"{name},{password},{age},{email},{phone},{balance}\n"

        user_file.write(new_data)

    def withdrawal(self, amount, comment="no comment", collector=False):

        transaction_label = "debit"

        if collector:
            transaction_type = "transfer"
            collector = collector.name
        else:
            transaction_type = "withdrawal"
            collector = self.name

        self.balance -= amount  # ADD DEPOSIT VALUE TO BALANCE\
        self.write_balance_value(self.balance)
        self.store_history(transaction_type, transaction_label,
                           amount, self.name, comment, collector)

        print(
            f"Hello {self.name}, Your withdrawal of ₦{amount} was successful. Your new balance is ₦{self.balance}.")

    def transfer(self, amount, recipient, comment=""):

        self.withdrawal(amount, comment, recipient)
        recipient.deposit(amount, comment, self)

        # self.balance -= amount
        # recipient.balance += amount
        # self.store_history("transfer", amount, comment, recipient.name)

        print(
            f"Congratulations {self.name}, Your transfer of ₦{amount} to {recipient.name} was successful. Your new balance is ₦{self.balance}.")

    def store_history(self, transaction_type, transaction_label,
                      amount, source, comment, receiver="same"):
        file = open("financial_statement.csv", "a")
        file.write(
            f"{transaction_type}, {transaction_label}, {amount}, {source}, {receiver}, {comment}\n")
        print(transaction_type, amount, comment, receiver)

    def begin(self):

        existing_user = input(
            "Please are you an existing or new customer? (y/n): ")

        if existing_user == "y":

            self.login()

        else:
            self.create_user()


account = Account()
account.begin()
account.deposit(30000)
# account.withdrawal(20000)
# tobi.deposit(20000)
# tobi.withdrawal(10000)
# ayo = Account("Ayo", 29, "ayo@tobiallen.com", "08023456789")
# tobi.transfer(2000, ayo, "Testing")
