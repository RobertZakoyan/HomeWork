from abc import ABC, abstractmethod
from typing import List, Union

class BankOperations(ABC):
    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass
    
    @abstractmethod
    def transfer(self, to_account: 'BankOperations', amount: float) -> None:
        pass
    
    @abstractmethod
    def get_balance(self) -> float:
        pass

    @abstractmethod
    def get_transactions(self) -> List[dict]:
        pass

    def __repr__(self):
        return self._acc_num


class Accounts(BankOperations):
    def __init__(self, acc_num: str, balance: float, acc_type: str) -> None:
        self._acc_num = acc_num
        self._balance = balance
        self._acc_type = acc_type
        self._transactions: List = []
    
    def deposit(self, amount: float) -> None:
        if amount >= 0:
            self._balance += amount
            self._transactions.append({"type": "deposit", "amount": amount})
            print(f"Deposited ${amount}. New Balance: ${self._balance}")
        else:
            print("You entered a negative amount.")

    def withdraw(self, amount: float) -> None:
        if amount <= self._balance:
            self._balance -= amount
            self._transactions.append({"type": "withdraw", "amount": amount})
            print(f"Withdrew ${amount}. New Balance: ${self._balance}")
        else:
            print("Insufficient funds.")

    def transfer(self, to_account: BankOperations, amount: float) -> None:
        if amount <= self._balance:
            self._balance -= amount
            to_account.deposit(amount)
            self._transactions.append({"type": "transfer", "to_account": f"{to_account}", "amount": amount})
            print(f"Transferred ${amount} to {to_account}. New Balance: ${self._balance}")
        else:
            print("Insufficient funds for transfer.")

    def get_balance(self) -> float:
        return self._balance

    def get_transactions(self) -> List[dict]:
        return self._transactions.copy()

class CheckingAccount(Accounts):
    def __init__(self, acc_num: str, balance: float = 0.0) -> None:
        super().__init__(acc_num=acc_num, balance=balance, acc_type="Checking")

class Customers:
    def __init__(self, name: str, contact_info: str, account: BankOperations) -> None:
        self._name = name
        self._contact_info = contact_info
        self._account = account
        self._account.owner = name

    def get_account_balance(self) -> float:
        return self._account.get_balance()

    def get_account_transactions(self) -> List[dict]:
        return self._account.get_transactions()
    
if __name__ == "__main__":

    checking_account = CheckingAccount(acc_num="CHK123", balance=3000)
    checking_account2 = CheckingAccount(acc_num="CKK122", balance=0)

    customer_1 = Customers(name="Rob", contact_info="+37498700822", account=checking_account)
    customer_2 = Customers(name="Davo", contact_info="+215125", account=checking_account2)

    print(customer_1.get_account_balance())

    customer_1._account.transfer(customer_2._account, 2000) 
    print(customer_1.get_account_balance())
    print(customer_2.get_account_balance())