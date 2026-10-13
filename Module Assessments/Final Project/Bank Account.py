import uuid
from datetime import datetime


class BankAccount(object):
    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = uuid.uuid4().hex[:8]

        # Filename format: account number, account type, and username
        self.filename = (
            str(self.accountNumber) + "_" +
            self.accountType + "_" +
            self.name + ".txt"
        )

        # Create the statement file and record the opening balance
        with open(self.filename, "w", encoding="utf-8") as statement:
            statement.write(
                f"{self._timestamp()} - Account opened with balance: "
                f"${self.balance:.2f}\n"
            )

    def _timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _record_transaction(self, description):
        with open(self.filename, "a", encoding="utf-8") as statement:
            statement.write(f"{self._timestamp()} - {description}\n")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        self._record_transaction(f"Deposit: +${amount:.2f}")
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            print("Withdrawal declined: insufficient funds.")
            return False

        self.balance -= amount
        self._record_transaction(f"Withdrawal: -${amount:.2f}")
        return self.balance

    def getBalance(self):
        return self.balance

    def getAccountNumber(self):
        return self.accountNumber

    def getName(self):
        return self.name

    def getAccountType(self):
        return self.accountType

    def getTransactionHistory(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as statement:
                return statement.read()
        except OSError as error:
            return f"Could not read the statement file: {error}"


# Create multiple accounts and apply transactions
account1 = BankAccount("Alex", "chequing")
account1.deposit(250)
account1.withdraw(40)

account2 = BankAccount("Jordan", "savings", 500)
account2.deposit(100)
account2.withdraw(75)

# Display account details and transaction histories
for account in (account1, account2):
    print(f"\nName: {account.getName()}")
    print(f"Account type: {account.getAccountType()}")
    print(f"Account number: {account.getAccountNumber()}")
    print(f"Balance: ${account.getBalance():.2f}")
    print("Transaction history:")
    print(account.getTransactionHistory())