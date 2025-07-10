#ООП Class


BankAccount

owner_name

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f'Декпозит пополнен на сумму {amount}')
        else:
            print(f'Нельзя вносить отрицательную сумму на депозит.')

    def withdraw(self, amount):
        if 0 < amount < self._balance:
            self._balance -= amount
            print(f'С депозита снята сумма {amount}.')
        else:
            print(f'Не хвататет средств. Овердрафт не доступен.')

client = BankAccount('John')
client.deposit(500)
client.withdraw(600)
print('Остаток:', client1.get_balance())
















