class BankAccount:
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0

    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance

    def display_account(self):
        print(f"{self.name}'s balance: ${self.balance}")

    @classmethod
    def display_bank(cls, att: string):
        if att == "account":
            print(f"Total Accounts: {BankAccount.total_accounts}")
        else:
            print(f"Total Balance: ${BankAccount.total_balance}")


# TODO: Create two accounts
alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 2000)
alice.display_account()
bob.display_account()
BankAccount.display_bank("account")
BankAccount.display_bank("balance")
# TODO: Print the information using the mentioned format
