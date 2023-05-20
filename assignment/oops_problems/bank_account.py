# Create a class called "BankAccount" with attributes account number, account holder name, and balance.
# Implement methods for deposit, withdraw, and transfer between accounts.

# pseudocode
"""
class Account:
    __init__()
        acc_holder_name
        acc_holder_number
        balance

    withdraw(amount)

    deposit(amount)


class Bank:
    __init__()
        collection_of_account

    transfer(sender_acc_no, receiver_acc_no, amount)
        sender_obj = get sender from collection_of_account
        receiver_obj = get receiver from collection_of_account
        sender_obj.withdraw(amount)
        receiver_obj.withdraw(amount)

"""


class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.dict = {self.account_number: {"account_holder_name": self.account_holder_name, "account_number": self.account_number,
                          "balance": self.balance}}

    def deposit(self, amount):
        self.balance += amount
        self.dict.update({self.account_number: {"account_holder_name": self.account_holder_name, "account_number": self.account_number,
                          "balance": self.balance}})
        return self.dict

    def withdraw(self, amount):
        self.balance -= amount
        self.dict.update({self.account_number: {"account_holder_name": self.account_holder_name, "account_number": self.account_number,
                                                "balance": self.balance}})
        return self.dict

    def display(self):
        # print(self.dict)
        return self.dict


class Bank:
    def create_account(self):
        account_number = int(input("Enter Account Number"))
        account_holder_name = input("Enter Account Holder Name")
        balance = int(input("Enter Creating Balance"))
        obj = BankAccount(account_number, account_holder_name, balance)
        return obj

    def deposit(self):
        obj = self.create_account()
        amount = int(input("Enter amount"))
        print(obj.deposit(amount))


    def withdraw(self):
        obj = self.create_account()
        amount = int(input("Enter amount"))
        obj.withdraw(amount)

    # def transfer(self, amount, account1, account2):
    #     pass

    # def display_data(self):
    #     obj = self.create_account()
    #     obj.display()






    # def transfer_balance(self):
    #     # amount
    #     print(self.dict.get(self.id))
    # bank = BankAccount()


    # def display_data(self):
    #     print(self.dict)

        # print(
        #     " account_holder_name \taccount_number \tbalance ")
        # for key, value in self.dict.items():
        #     print(key, value)
            # print("\t{}\t\t\t\t{}\t\t\t\t{}".format(value.account_holder_name, value.account_number,
            #                                                     value.balance))


if __name__ == '__main__':
    # bank_acc = BankAccount(123456789, "milan", 2000)
    # print(bank_acc.deposit(2000))
    # print()
    # print(bank_acc.withdraw(500))
    # print()

    # bank_acc = BankAccount(21354645, "raj", 0)
    # print(bank_acc.deposit(2000))
    print()

    # print(bank_acc.transfer_balance(2000, 21354645))
    print()

    # print(bank_acc.transfer_balance())
    print()

    # bank_acc.display_data()
    obj = Bank()
    obj.deposit()
    # obj.display_data()
    # obj.withdraw()






