class Account:
    def __init__(self, owner, balance = 0):
        self.__owner = owner
        self.__balance = balance

    def withdraw(self, amount):
        if amount > self.__balance:
            raise RuntimeError
        else:
            self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def __repr__(self):
        return f"Owener: {self.__owner}, Balance: {self.__balance}"

a = Account('Zixuan', 100)
print(a)
# print(a.__balance) # Error